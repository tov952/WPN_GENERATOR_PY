from WPN_GENERATOR_PY import WPN_Utils

import hou
import fnmatch
import pprint
import pathlib
import imp


debug = False

class Container(object):

    def __init__(self,psdGroup):

        self.PSDGroup = psdGroup
        self.name = self.PSDGroup.name
        self.subnetNodeName = self.PSDGroup.name +"_CONTAINER"
        self.childAssetObjs = []
        self.subnetContainerNode = None
        self.directChildLayers = []
        self.containerParent = self.PSDGroup.parent

        self.getDirectChildLayer()

    def getDirectChildLayer(self):
        for layer in self.PSDGroup:
            self.directChildLayers.append(layer)
        if debug:
            print("DEBUG: DirectChildLayers of " +  self.PSDGroup.name)
            pprint.pprint(self.directChildLayers)

    def populateContainerWithChildAssets(self):
        for childAsset in self.childAssetObjs:
            childAsset.createNode()

    """Creates childAssetObjs Flat"""
    def populateChildAssetsOfNodeType(self, ChildAssetClass,layerNames = []):
        if debug:
            print("DEBUG: Creating " + ChildAssetClass.__name__ + " Objs of " + self.name)
        PSDGrpDesc = []
        layersToChild = []
        for desc in self.PSDGroup.descendants():
            PSDGrpDesc.append(desc)

        if len(layerNames) != 0:
            descendantLayerNames = [childLayer.name for childLayer in PSDGrpDesc]
            for layerName in layerNames:
                layerNamePattern = "*_"+layerName+"*"
                for i, layerName in enumerate(descendantLayerNames):
                    if fnmatch.fnmatch(layerName, layerNamePattern):
                        layersToChild.append(PSDGrpDesc[i])
        else:
            layersToChild = PSDGrpDesc

        #print(layersToChild)


        for childlayer in layersToChild:
            childGunPart = ChildAssetClass(childlayer, self)
            self.childAssetObjs.append(childGunPart)
        if debug:
            print("childAssetObjs of "+ self.name)
            pprint.pprint(self.childAssetObjs)


    def createContainer(self):
        #print(self.containerName)
        HDA = hou.pwd()
        geoContainer = HDA.node("GEO_CONTAINER")
        inputGeoContainer1 = geoContainer.indirectInputs()[0]
        self.subnetContainerNode = geoContainer.node(self.subnetNodeName)
        if self.subnetContainerNode == None:
            self.subnetContainerNode = geoContainer.createNode("geo", self.subnetNodeName)
            #self.subnetContainerNode.setInput(0, inputGeoContainer1)
            self.subnetContainerNode.moveToGoodPosition()
        #input1 = self.subnetContainerNode.indirectInputs()[0]
        print("Created: " + self.subnetNodeName)
        return self.subnetContainerNode

class ChildAsset(object):

    def __init__(self, layer, containerObj):

        self.layer = layer
        self.name = self.layer.name
        self.layerPrefix = "_".join(self.name.split("_")[0:-1])
        self.parentObj = containerObj
        self.childLayers = []
        self.nodeType = ""
        self.node = None
        self.parentContainerNode = self.parentObj.subnetContainerNode
        self.parmSources = None
        self.parmTargets = None
        self.parentNode = hou.pwd()
        self.parmSourceTargetDict = {}
        self.parmLayerDict = {}
        self.PTG = None

    def setLayerNameParms(self):
        for parm, layer in self.parmLayerDict.items():
            try:
                self.node.parm(parm).set(layer.name)
            except:
                print("Skipping " +self.node.name()+ "'s " + parm + " assignment, as layer doesn't exist")

    def linkFile(self):
        if debug:
            print("DEBUG: Linking File Parm from: " + self.parentNode.name() + " to " + self.node.name())
        fileParm = self.parentNode.parm("renamedFile")
        self.node.parm("file").set(WPN_Utils.linkExpressionParentParmToParm(fileParm, force_evaluate = True, string = True))

    def getParmsOfPrefix(self, node, parmPrefix):
        if debug:
            print("DEBUG: Getting Parms in " + node.name() + " for " + parmPrefix)
        return node.globParms(parmPrefix+"*")

    def getParmSourceTargetDict(self, node, parmPrefix):
        parmSourceTargetDict = {}
        #parmNames = [ parmSource.name().split(parmPrefix+"_")[-1] for parmSource in self.parmSources]
        parmSourceNames = [ parmSource.name() for parmSource in self.parmSources]
        #print("parmName is:")
        if debug:
            print("Getting ParmSourceTargetDict in " + node.name() + " for " + parmPrefix)
            pprint.pprint(parmSourceNames)
        for parm in node.parms():
            matchParmList = fnmatch.filter(parmSourceNames, "*" + parm.name())
            if len(matchParmList)>0:
                #print("matched" + matchParmList[0] + " with " + parm.name())
                matchedParm = self.parentNode.parm(matchParmList[0])
                if "crveShpProfile" in matchedParm.name():
                    pass
                else:
                    parmSourceTargetDict[matchedParm] = parm
        return parmSourceTargetDict



    def linkParmSourcesToTargets(self):
        if debug:
            print("DEBUG: Linking Parm Sources to Targets for " + self.node.name())
        for source, target in self.parmSourceTargetDict.items():
            if debug:
                print("DEBUG: Linking " + source.name() + " to " + target.name())
            target.setExpression(WPN_Utils.linkExpressionParentParmToParm(source))



    def createNode(self):
        if self.parentContainerNode == None:
            self.parentContainerNode = self.parentObj.subnetContainerNode
        #print(self.name + " ParentContainerNode is " + self.parentObj.name)
        #input1 = self.parentContainerNode.indirectInputs()[0]
        self.node = self.parentContainerNode.createNode(self.nodeType, self.name)
        #self.node.setInput(0, input1)
        self.node.moveToGoodPosition()
        print("Created: " + self.node.name())
        self.postNodeCreation()
        return self.node

    def replicateParmsInHDA(self):
        #print("Getting PTG As Code for: " + self.name)
        self.ptg = self.node.parmTemplateGroup()
        code = "import hou \n"
        code += self.ptg.asCode(function_name = "createPTG")
        parmTemplateLibPath = str(pathlib.Path(__file__).parent.resolve()) + "/parmTemplatelib.py"
        #print(code)
        source_file = open(
            parmTemplateLibPath,
            "w")
        source_file.write(code)
        source_file.close()
        from WPN_GENERATOR_PY import parmtemplatelib as PTL
        imp.reload(PTL)
        genPTG = PTL.createPTG()
        self.PTG = self.parentNode.parmTemplateGroup()
        for parmTemplate in genPTG.entries():
            if not fnmatch.fnmatch(parmTemplate.name(), "*exclude*"):
                print(parmTemplate.name())
                #newParmTemplate = newPTG.entryAtIndices((,))
                print(self.name + "_" + parmTemplate.name())
                parmTemplate.setName(self.name)
                parmTemplate.setLabel(self.name)
                self.PTG.append(parmTemplate)
                self.recursiveSetParmPrefixAndConditionals(parmTemplate)
        self.parentNode.setParmTemplateGroup(self.PTG, rename_conflicting_parms= True)

    def recursiveSetParmPrefixAndConditionals(self, parmTemplate):

        """Sets parm prefix + conditionals"""
        #print("recursive set for : " + parmTemplate.name())
        for parmTemplate in parmTemplate.parmTemplates():
            #print(parmTemplate.name())
            #print(parmTemplate.type())
            if parmTemplate.type() == hou.parmTemplateType.Folder:
                #print(parmTemplate.conditionals())
                renamedParmTemplateFolder = self.PTG.find(parmTemplate.name())
                renamedParmTemplateFolder.setName(self.name + "_" + parmTemplate.name())
                for conditionalType, condition in renamedParmTemplateFolder.conditionals().items():
                    #print("condition start: " + condition)
                    conditionSplit = condition.split(" ")
                    conditionReplaced = self.name + "_" + conditionSplit[1]
                    conditionSplit[1] = conditionReplaced
                    condition = " ".join(conditionSplit)
                    #print("condition end: " + condition)

                    renamedParmTemplateFolder.setConditional(conditionalType, condition)
                self.PTG.replace(parmTemplate.name(), renamedParmTemplateFolder)
                self.recursiveSetParmPrefixAndConditionals(parmTemplate)
            else:
                #print("name to set : " + self.name + "_" + parmTemplate.name())
                renamedParmTemplate = self.PTG.find(parmTemplate.name())
                renamedParmTemplate.setName(self.name + "_" + parmTemplate.name())
                self.PTG.replace(parmTemplate.name(), renamedParmTemplate)
                #pprint.pprint(renamedParmTemplate.conditionals())
                #parmTemplate.setName(self.name + "_" + parmTemplate.name())
                #print("now name: " + parmTemplate.name())







    def postNodeCreation(self):
        self.parmSources = self.getParmsOfPrefix(self.parentNode, self.name)
        self.parmTargets = self.getParmsOfPrefix(self.node, self.name)
        self.parmSourceTargetDict = self.getParmSourceTargetDict(self.node, self.name)
        self.linkParmSourcesToTargets()
        self.linkFile()
        self.setLayerNameParms()
        self.replicateParmsInHDA()
        #self.addSpareParmTupleIntoParentNode()
        self.debug()


    def debug(self):
        if debug:
            print("DEBUG: Parm Sources for " + self.name + " is:")
            pprint.pprint(self.parmSources)
            print("DEBUG: Parm Targets for " + self.name + " is:")
            pprint.pprint(self.parmTargets)
            print("DEBUG: ParmSourceTargetDict for " + self.name + " is:")
            pprint.pprint(self.parmSourceTargetDict)








