import sys
import hou
import pprint
import itertools
from WPN_GENERATOR_PY import WPN_Enums
from WPN_GENERATOR_PY import WPN_Utils
sys.path.append(r"E:\Users\Jason\Documents\houdini18.5\python3.7libs\WPN_GENERATOR_PY\venv\Lib\site-packages")

from WPN_GENERATOR_PY import GunPart
from WPN_GENERATOR_PY import gunPartParmTemplatesGRP as GPpT

import fnmatch
from psd_tools import PSDImage

GEO_CONTAINER = "GEO_CONTAINER"

debug = True

gunPartList = []   #Stores instances of generated gunparts
parentChildDict = {} #Stores dict of <Group> : <Layer>/<Group> Children[]
psd = None #stores PSD
savedPSD = None #Stores the saved PSD
groupParentDict = {} #Stores dict of <Group> : str parentName


def rebuild(this_node):
    global savedPSD
    print("Build Grp")
    geoContainer = this_node.node(GEO_CONTAINER)

    print("---------------------Removing all Spare Parms------------------------")
    this_node.removeSpareParms()
    print("---------------------Cleaning Geo Container--------------------------")
    # Cleans Geo Container
    for child in geoContainer.children():
        child.destroy()
    print("---------------------Get Parent-Child Dict----------------------------")
    PCDict = getPSDGrpAndChildren(this_node)

    #print(PCDict)
    savedPSDPath = renameChildLayersAndSave(PCDict)
    savedPSD = PSDImage.open(savedPSDPath)

    #ptg = this_node.parmTemplateGroup()
    #folder = hou.FolderParmTemplate("folder", "My Parms")

    groupParentDict = getGroupParentDict()
    pprint.pprint(groupParentDict)
    #print(folder)
    #ptg.append(folder)
    parmName = []
    pprint.pprint(parentChildDict)
    for parent, children in parentChildDict.items():
        containingFolder = ()
        parmNames = [ parm.name() for parm in this_node.parms()]
        #print(parent.name)
        #print(parmNames)
        if parent.name not in parmNames:
            parentParmTemplate = buildParmTemplates(this_node, parent.name, Group = True)
        else:
            i = parmNames.index(parent.name)
            parentParmTemplate = this_node.parms()[i].parmTemplate()
        #print(parentParmTemplate)
        #ptg.append(parentParmTemplate)
        for child in children:
            if child.is_group() != True:
                splitChildName = child.name.split("_")
                if "SIDE" in splitChildName or "CUTOUT" in splitChildName:
                    parentParmTemplate.addParmTemplate(buildParmTemplates(this_node, child.name))
        if parentParmTemplate != None:
            if parent.is_group:
                containingFolder = groupParentDict[parent]
                print(containingFolder)
            this_node.addSpareParmTuple(parentParmTemplate, in_folder = containingFolder)
    #print(ptg.parmTemplates())



    print("---------------------Getting Valid PSD Layer Names-------------------")
    #validPSDLayerNames, layerNameCountDict = getValidPSDLayerNames(this_node)
    print("---------------------Building Parm Templates-------------------------")
    #buildParmTemplates(this_node, validPSDLayerNames)
    print("---------------------Setting MultiParmNums---------------------------")
    #SetMultiParmNums(layerNameCountDict, this_node)
    print("---------------------Generating Gun Parts----------------------------")
    #genGunPartNodes(geoContainer, this_node)
    print("---------------------Setting Layer Names-----------------------------")
    #SetValidLayerName(this_node, validPSDLayerNames)
    print("---------------------Setting Gun Part Shape--------------------------")
    #for gunpart in gunPartList:
        #gunpart.setValidLayerName()
        #gunpart.setShapeType()

def removeNone(list):
    strList = []
    if list == None or isinstance(list, str):
        #print(list + " is a string")
        return strList
    else:
        for sublist in list:
            #print(list)
            if isinstance(sublist, str):
                #print(sublist)
                strList.append(sublist)
            else:
                strList.append(removeNone(sublist))
    return strList

def flatten(A):
    rt = []
    for i in A:
        if isinstance(i,list): rt.extend(flatten(i))
        else: rt.append(i)
    return rt

def getGroupParentDict():
    for parent, child in parentChildDict.items():
        parentList = getParentOfLayer(parent)
        cleanParentlist = removeNone(parentList)
        flatParentList = flatten(cleanParentlist)
        flatParentList.reverse()
        pop = flatParentList.pop(0)
        print(flatParentList)
        groupParentDict[parent] = tuple(flatParentList)

    return groupParentDict
    #print(groupParentDict)

def getParentOfLayer(layer):
    #print(layer.name)
    if layer.parent:
        return [layer.parent.name] + [getParentOfLayer(layer.parent)]



def SetValidLayerName(this_node, validPSDLayerNames):
    for validLayerName in validPSDLayerNames:
        noShapeName = WPN_Utils.getNoShapeSuffixName(validLayerName)
        #print(noShapeName + "_layer_name1")
        try:
            this_node.parm(noShapeName + "_layer_name1").set(validLayerName)
        except:
            print("ERROR: Setting " + noShapeName + "_layer_name1 failed, Check LayerName Conventions; [gunPart]#_[shapeType]")


def renameChildLayersAndSave(PCDict):
    psdPath = "E:/psdTest.psd"
    for parent, children in PCDict.items():
        for child in children:
            ogChildName = child.name
            newChildName = parent.name + "_" + child.name
            child.name = newChildName
    #print(psd)
    psd.save(psdPath)
    return psdPath



def genGunPartNodes(geoContainer, this_node):
    # Gen Gunpart Nodes as needed
    gpTypes = WPN_Enums.GPTypes
    for gpType in gpTypes:
        multiparm = this_node.parm("numOf_" + gpType.name)
        if multiparm != None:
            #print(gpType.name + " multiparm found :" + multiparm.name())
            #print("MultiParm Length :" + str(multiparm.eval()))
            multiparmLen = multiparm.eval()
            for i in range(multiparmLen):
                gunPartNodeName = gpType.name
                gunPart = GunPart.gunpart(gunPartNodeName, gpType, i)
                gunPartNode = gunPart.createGunpartNode()
                gunPartList.append(gunPart)
                #print(gunPartNode)
                gunPartNode.parm("file").set(WPN_Utils.linkExpressionSTR("file", True, True))
                linkParms(this_node, gunPartNode, gunPart.parmPrefix)

    geoContainer.layoutChildren()
    for child in geoContainer.children():
        child.layoutChildren()





def SetMultiParmNums(layerNameCountDict, this_node):
    for key, value in layerNameCountDict.items():
        multiParmName = "numOf_" + key
        print("Setting " + multiParmName + " to " + str(value))
        this_node.parm(multiParmName).set(value)


def buildParmTemplates(this_node, layerName, Group = False):
    if Group == True:
        parmFolderTemplate = GPpT.genGunpartParentTemplates(layerName)
    else:
        parmFolderTemplate = GPpT.genGunpartParmTemplates(layerName)
    # print(this_node.parms())
    return parmFolderTemplate






def getPSDGrpAndChildren(this_node):
    # Gets list of Grps
    global psd
    filepath = this_node.parm("file").eval()
    psd = PSDImage.open(filepath)
    #print(psd)
    layerNames = []
    validLayerNames = []
    # print(gpTypesNames)

    for i, layer in enumerate(psd):
        getChildOfLayer(layer)
    #print(parentChildDict)




    return parentChildDict
    #print(parentChildDict)


def getChildOfLayer(layer):
    if layer.is_group():
        print(layer.name + "is Group")
        for childLayer in layer:
            parentName = layer.name
            if debug == True:
                print("DEBUG: Child of " + parentName + " is " + childLayer.name)
            getChildOfLayer(childLayer)
            if parentChildDict.get(layer) == None: #if non-existent key
                parentChildDict[layer] = [childLayer] #make new parent:Child
            else:
                parentChildDict[layer].append(childLayer) #append to child list if not group
        #parentChildDict[layer].append(layer.parent.name)







def getValidPSDLayerNames(this_node):
    global savedPSD
    # Gets list of valid layers based on enum and not empty layers.
    gpTypesNames = [gpType.name for gpType in WPN_Enums.GPTypes]
    layerNames = []
    validLayerNames = []
    # print(gpTypesNames)

    for i, layer in enumerate(savedPSD):
        for child in layer.descendants():
            #print(child.name)
        #print(layer.name.split(' '))
        #if layer.size != (0, 0):
            #if len(layer.name.split(' ')) > 1:
                #print(layer.name + " removed because it contained spaces")
            #else:
                #layerNames.append(layer.name)
        #else:
            #print(layer.name + " removed because layer empty")
            layerNames.append(child.name)

    if debug:
        print("DEBUG: LayerNames")
        print(layerNames)
        #print("DEBUG: gpTypeNames ")
        #print(gpTypesNames)
    layerNameCountDict = {}
    for gpTypesName in gpTypesNames:

        layerNameCount = 0
        matchList = fnmatch.filter(layerNames, gpTypesName + "*")
        if len(matchList) != 0:
            layerNameCount = len(matchList)
            if debug:
                print("DEBUG: " + gpTypesName +" MatchList:")
                print(matchList)
                #print("LayerNameCount: " +layerNameCount)
            validLayerNames += fnmatch.filter(layerNames, gpTypesName + "*")
        if layerNameCount != 0:
            layerNameCountDict[gpTypesName] = layerNameCount
    for validLayerName in validLayerNames:
        print("Found " + validLayerName)

    #print(layerNameCountDict)
    #print(list(set(validLayerNames)))
    return list(set(validLayerNames)), layerNameCountDict



def linkParms(this_node, gunPartNode, gunPartPrefix):
    gunPartParms = this_node.globParms(gunPartPrefix + "_*")
    unprefixedParmsName = [parm.name().replace(gunPartPrefix + "_", "") for parm in gunPartParms]
    for i, unprefixedParmName in enumerate(unprefixedParmsName):
        parmSource = gunPartParms[i]
        parmTarget = gunPartNode.parm(unprefixedParmName)
        #print(parmTarget.parmTemplate().type())
        if parmTarget.parmTemplate().type() == hou.parmTemplateType.String:
            #print(parmTarget.parmTemplate().type)
            parmTarget.set(WPN_Utils.linkExpressionSTR(parmSource.name(), True, True))
        elif "crveShpProfile" in parmTarget.name():
            pass
        else:
            parmTarget.setExpression(WPN_Utils.linkExpressionSTR(parmSource.name()))
    # print(gunPartParmsNameOnly)
