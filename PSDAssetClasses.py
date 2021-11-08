from WPN_GENERATOR_PY import WPN_Utils

import hou
import fnmatch
import pprint
import pathlib
import imp


debug = False

class Generator(object):

    def __init__(self, PSD):
        self.node = hou.pwd()
        self.psd = PSD
        self.AllChildAssetsObjs = []
        self.AllContainerObjs = []


    def genContainerObjs(self, containerClass):
        #print("Enter createAssetObjs")
        container = None
        for layer in self.psd.descendants():
            if layer.is_group():
                group = layer
                groupName = group.name
                #print(layer.name + " is group! Creating Container!")
                container = containerClass(group, self)
                self.AllContainerObjs.append(container)
        self.genContainerAssetObjs()

    def genContainerAssetObjs(self):
        for container in self.AllContainerObjs:
            print(container.name)
            container.createAssetObjs()

            self.AllChildAssetsObjs += container.childAssetObjs

        self.postCreation()

    def postCreation(self):
        self.AllChildAssetsNames = [childAsset.name for childAsset in self.AllChildAssetsObjs]



class Container(object):

    def __init__(self,psdGroup, generator):

        self.generator = generator
        self.PSDGroup = psdGroup
        self.name = self.PSDGroup.name
        self.subnetNodeName = self.PSDGroup.name +"_CONTAINER"
        self.childAssetObjs = []
        self.subnetContainerNode = None
        #self.directChildLayers = []
        self.containerParent = self.PSDGroup.parent

        #self.getDirectChildLayer()

    # def getDirectChildLayer(self):
    #     for layer in self.PSDGroup:
    #         self.directChildLayers.append(layer)
    #     if debug:
    #         print("DEBUG: DirectChildLayers of " +  self.PSDGroup.name)
    #         pprint.pprint(self.directChildLayers)

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

    def createAssetObjs(self):
        for childlayer in self.PSDGroup:
            if not childlayer.is_group():
                childlayerName = childlayer.name.split("_")[-1]
                # print("childlayerName is " + childlayerName)
                childAsset = self.childAssetDefinition(childlayerName, childlayer)
                if childAsset != None:
                    self.childAssetObjs.append(childAsset)
                else:
                    pass

                # if childlayerName == "SIDE":
                #     # print(childlayer.name + " is SIDE! Creating GunPartAsset")
                #     childAsset = wpnAsset.GunPartAsset(childlayer, gunPartContainer)
                # elif childlayerName == "CUTOUT":
                #     # print(childlayer.name + " is CUTOUT! Creating CutoutAsset")
                #     childAsset = wpnAsset.CutoutAsset(childlayer, gunPartContainer)
                # if childAsset != None:
                #     gunPartContainer.childAssetObjs.append(childAsset)
                # else:
                #     pass

    def childAssetDefinition(self, childlayerName, childlayer):
        print(" No Child Asset Definition Logic!")
        return None

class ChildAsset(object):

    def __init__(self, layer, containerObj):

        self.layer = layer
        self.name = self.layer.name
        self.layerPrefix = "_".join(self.name.split("_")[0:-1])
        self.layerSuffix = self.name.split("_")[-1]
        self.containerObj = containerObj
        self.parentLayer = self.layer.parent
        self.parentObj = None
        self.childObjs = []


        self.nodeType = ""
        self.node = None
        self.parentContainerNode = self.containerObj.subnetContainerNode
        self.parmSources = None
        self.parmTargets = None
        self.parentNode = hou.pwd()
        self.parmSourceTargetDict = {}
        self.parmLayerDict = {}
        self.PTG = None
        self.flatParmMods = {}  #Parms to add modify (add)
        self.parmModFactor = {} #Parms to mult modify (mult)
        self.factorParmNames = {}
        self.flatParmTarget = {}
        self.masterGroup = self.setMasterGroup()
        self.directChildLayers = self.setDirectChildLayers()

    def setParentObj(self):
        #print("--------------set parent obj for " + self.name + "----------")
        for i, childAssetName in enumerate(self.containerObj.generator.AllChildAssetsNames):
            #print(childAssetName)
            parentLayerName = self.layer.parent.parent.name + "_" + self.layerSuffix
            #print(parentLayerName)
            if fnmatch.fnmatch(childAssetName, parentLayerName ) :
                #print("MATCH")
                self.parentObj = self.containerObj.generator.AllChildAssetsObjs[i]
                break
        if self.parentObj != None:
            print(self.name + " parent obj is " + self.parentObj.name)
        else:
            print(self.name + " parent obj is Root")
        # if self.parentObj == None:
        #     print(self.name + " parent obj is Root ")



    def setDirectChildLayers(self):
        directChildLayers = []
        parentGRP = self.layer.parent
        for layer in parentGRP:
            if layer.is_group():
                #childNode = self.parentNode.glob(layer.name)
                #print(self.name + "directChildLayer is " + layer.name)
                directChildLayers.append(layer)
        return directChildLayers

    def appendSelfToParent(self):
        #if self.parentObj != self:
        if self.parentObj != None:
            #print("Appending " + self.name + " to " + self.parentObj.name)
            self.parentObj.childObjs.append(self)

    def setChildrenFactorParmNames(self):
        for child in self.childObjs:
            child.factorParmNames = self.factorParmNames

    def debugPrintParentChildObjs(self):
        print("-------------------------")
        print(self.name )
        if self.parentObj != None:
            print("Parent Objs: " + self.parentObj.name)
        else:
            print("Parent Objs: Root ")
        print("Child Objs: ")
        pprint.pprint( [o.name for o in self.childObjs])
        print("-----------------------")


    def setMasterGroup(self):
        #print(self.containerObj.containerParent.name)
        if self.containerObj.containerParent.name == "Root":
            #print(self.layer.name + "is under a master Group")
            return True

    def setLayerNameParms(self):
        for parm, layer in self.parmLayerDict.items():
            try:
                self.node.parm(parm).set(layer.name)
            except:
                pass
                #print("Skipping " +self.node.name()+ "'s " + parm + " assignment, as layer doesn't exist")

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

    def genOverallMods(self):
        overallCTRLFolderPT = self.PTG.findFolder("Overall")
        if len(self.flatParmMods) > 0 and self.masterGroup == True:
            modifierFolderPT = hou.FolderParmTemplate(self.layerPrefix + "Modifiers",self.layerPrefix + " Modifiers", folder_type=hou.folderType.Simple)
            modifierFolderName = modifierFolderPT.name()
            self.PTG.appendToFolder(overallCTRLFolderPT, modifierFolderPT)
            self.parentNode.setParmTemplateGroup(self.PTG, rename_conflicting_parms= True)
            for parmToModName, defaultValue in self.flatParmMods.items():
                modifierFolder= self.PTG.find(modifierFolderName)
                #print(modifierFolder)
                parmTemplateToMod = self.PTG.find(self.name + "_" + parmToModName)
                parmModName = parmTemplateToMod.name() + "_MOD"
                self.flatParmTarget[parmModName] = parmToModName
                parmTemplateToMod.setName(parmModName)
                parmTemplateToMod.setDefaultValue((defaultValue,))
                self.PTG.appendToFolder(modifierFolder, parmTemplateToMod)
            for parmToModName, factor in self.parmModFactor.items():
                modifierFolder= self.PTG.find(modifierFolderName)
                factorParmName = self.name + "_" + parmToModName + "_FACTOR"
                factorParmLabel = parmToModName + " Factor"
                factorPT = hou.FloatParmTemplate(factorParmName,factorParmLabel, 1, default_value=(factor,))
                #print(modifierFolderPT.name())
                self.factorParmNames[factorParmName] = parmToModName
                self.PTG.appendToFolder(modifierFolder, factorPT)
            self.parentNode.setParmTemplateGroup(self.PTG, rename_conflicting_parms= True)


    def linkflatParmMods(self):
        for parmModName, targetName in self.flatParmTarget.items():
            sourceParm = self.parentNode.parm(parmModName)
            targetParm = self.node.parm(targetName)
            ogTargetExpression = targetParm.expression()
            modTargetExpression = ogTargetExpression + "+" + WPN_Utils.linkExpressionParentParmToParm(sourceParm)
            targetParm.setExpression(modTargetExpression)

    def linkFactorParmMods(self):
        #print("linking factor parm mods for" + self.name)

        for parmModName, parmTargetName in self.factorParmNames.items():
            #print("gothere")
            sourceParm = self.parentNode.parm(parmModName)
            for childObj in self.childObjs:
                node = childObj.node
                targetParm = node.parm(parmTargetName)
                parmModBase = self.node.parm(parmTargetName)
                ogTargetExpression = targetParm.expression()
                parmModBaseExpr = WPN_Utils.getlinkExpression(targetParm, parmModBase)

                modTargetExpression = ogTargetExpression + "+" + parmModBaseExpr + "*" + WPN_Utils.linkExpressionParentParmToParm(sourceParm)
                targetParm.setExpression(modTargetExpression)
                #print("linked Parm Factors for " + self.name + " to " + childObj.name)
            #print("--------------------------------------------------")
            #print(self.name + " direct child layers in : " + parmModName)
            #print(self.directChildLayers)
            #print("-------------------------------------------------")
            # for i in range(len(self.directChildLayers)):
            #     print("Finding " + self.directChildLayers[i].name + "_" + self.layerSuffix )
            #     #pprint.pprint(allChildAssetNames)
            #     matchedObjs = fnmatch.filter(allChildAssetNames, self.directChildLayers[i].name + "_" + self.layerSuffix)
            #
            #     for matchedObj in matchedObjs:
            #         index = allChildAssetNames.index(matchedObj)
            #         asset = self.containerObj.generator.AllChildAssetsObjs[index]
            #         node = asset.node
            #         targetParm = node.parm(parmTargetName)
            #         parmModBase = self.node.parm(parmTargetName)
            #         ogTargetExpression = targetParm.expression()
            #         parmModBaseExpr = WPN_Utils.getlinkExpression(targetParm, parmModBase)
            #
            #         modTargetExpression = ogTargetExpression + "+" + parmModBaseExpr + "*" + WPN_Utils.linkExpressionParentParmToParm(sourceParm)
            #         targetParm.setExpression(modTargetExpression)
            #         print("linked Parm Factors for " + self.name + " to " + asset.name)

        #pass

    def linkParmSourcesToTargets(self):
        if debug:
            print("DEBUG: Linking Parm Sources to Targets for " + self.node.name())
        for source, target in self.parmSourceTargetDict.items():
            if debug:
                print("DEBUG: Linking " + source.name() + " to " + target.name())
            target.setExpression(WPN_Utils.linkExpressionParentParmToParm(source))



    def createNode(self):
        if self.parentContainerNode == None:
            self.parentContainerNode = self.containerObj.subnetContainerNode
        #print(self.name + " ParentContainerNode is " + self.containerObj.name)
        #input1 = self.parentContainerNode.indirectInputs()[0]
        #print("createNode")
        #print(self.layer.name)
        self.node = self.parentContainerNode.createNode(self.nodeType, self.layer.name)
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
        advancedFolderPT = hou.FolderParmTemplate("advanced", "Advanced", folder_type = hou.folderType.Collapsible)
        if self.PTG.findFolder("Advanced") != None:
            advancedFolder = self.PTG.findFolder("Advanced")
        else:
            self.PTG.append(advancedFolderPT)
            print("Appended PTG with Advanced folder")
        for parmTemplate in genPTG.entries():
            if not fnmatch.fnmatch(parmTemplate.name(), "*exclude*"):
                #print(parmTemplate.name())
                #newParmTemplate = newPTG.entryAtIndices((,))
                #print(self.name + "_" + parmTemplate.name())
                parmTemplate.setName(self.name)
                parmTemplate.setLabel(self.name)
                advancedFolder = self.PTG.findFolder("Advanced")
                #print("advanced folder is :" + advancedFolder.name())
                self.PTG.appendToFolder(advancedFolder, parmTemplate)
                #self.PTG.append(parmTemplate)
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
        self.replicateParmsInHDA()
        self.genOverallMods()
        self.parmSources = self.getParmsOfPrefix(self.parentNode, self.name)
        self.parmTargets = self.getParmsOfPrefix(self.node, self.name)
        self.parmSourceTargetDict = self.getParmSourceTargetDict(self.node, self.name)
        self.linkParmSourcesToTargets()
        self.linkFile()
        self.setLayerNameParms()
        self.linkflatParmMods()
        #self.linkFactorParmMods()

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








