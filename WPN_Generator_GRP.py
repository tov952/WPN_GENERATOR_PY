import sys
import hou
import pprint
import os
import itertools
from WPN_GENERATOR_PY import WPN_Enums
from WPN_GENERATOR_PY import WPN_Utils
sys.path.append(r"E:\Users\Jason\Documents\houdini18.5\python3.7libs\WPN_GENERATOR_PY\venv\Lib\site-packages")

from WPN_GENERATOR_PY import GunPart_GRP as GunPart
from WPN_GENERATOR_PY import gunPartParmTemplatesGRP as GPpT

import fnmatch
from psd_tools import PSDImage
from psd_tools.constants import Resource


#GLOBALS
GEO_CONTAINER = "GEO_CONTAINER"
debug = True

gunPartList = []   #Stores instances of generated gunparts
parentChildDict = {} #Stores dict of <Group> : <Layer>/<Group> Children[]

psdFilepath = ""
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
    print("---------------------Get Parent-Child Dict---------------------------")
    PCDict = getPSDGrpAndChildren(this_node)
    print("---------------------Saving Renamed PSDs-----------------------------")
    savedPSDPath = renameChildLayersAndSave(PCDict)
    savedPSD = PSDImage.open(savedPSDPath)
    print("---------------------Get Group:Parent Dict---------------------------")
    groupParentDict = getGroupParentDict()

    print("---------------------Building Parm Templates-------------------------")
    BuildParmTemplateHeirarchy(groupParentDict, this_node)
    print("---------------------Generating Gun Parts----------------------------")
    genGunPartNodes(geoContainer, this_node)
    print("---------------------Setting Layer Names-----------------------------")
    #SetValidLayerName(this_node, validPSDLayerNames)
    print("---------------------Setting Gun Part Shape--------------------------")
    #for gunpart in gunPartList:
        #gunpart.setValidLayerName()
        #gunpart.setShapeType()


def BuildParmTemplateHeirarchy(groupParentDict, this_node):
    #Build Parent Parm Templates
    for parent, children in parentChildDict.items():
        containingFolder = ()
        parmNames = [parm.name() for parm in this_node.parms()]
        if parent.name not in parmNames:
            parentParmTemplate = buildParmTemplates(this_node, parent.name, Group=True)
        else:
            i = parmNames.index(parent.name)
            parentParmTemplate = this_node.parms()[i].parmTemplate()

        #Build Child Templates
        for child in children:
            if child.is_group() != True:
                splitChildName = child.name.split("_")
                if "SIDE" in splitChildName or "CUTOUT" in splitChildName:
                    parentParmTemplate.addParmTemplate(buildParmTemplates(this_node, child.name))
                print("Parenting " + child.name + " Parms into " + parent.name + " ParmFolder")
        if parentParmTemplate != None:
            if parent.is_group:
                containingFolder = groupParentDict[parent]
                if len(containingFolder) != 0:
                    parentFolder = containingFolder[-1] + " ParmFolder"
                else:
                    parentFolder = "Root"
                print("Parenting " + parent.name + " ParmFolder into " + parentFolder)

            this_node.addSpareParmTuple(parentParmTemplate, in_folder=containingFolder)



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
        groupParentDict[parent] = tuple(flatParentList)
        if len(flatParentList) != 0:
            printParentList = ", ".join(flatParentList) + " ParmFolders" #Only for printing
        else:
            printParentList = "None" #Only for printing
        print(parent.name + " ParmFolder's Ancestors are: " + printParentList)
    if debug:
        print("DEBUG: Group Parent Dict  ( <Group> : Tuple of all Parents.name ) ")
        pprint.pprint(groupParentDict)
    return groupParentDict

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
    (dirname, filename) = os.path.split(psdFilepath)
    (filename, ext) = os.path.splitext(filename)
    psdPath = dirname + "/" + filename + "_renamed" + ext
    for parent, children in PCDict.items():
        for child in children:
            ogChildName = child.name
            newChildName = parent.name + "_" + child.name
            child.name = newChildName
            if debug:
                print("DEBUG: Renaming " + ogChildName + " to " + newChildName)
    psd.save(psdPath)
    print("Saved Renamed PSD into: " + psdPath)
    return psdPath



def genGunPartNodes(geoContainer, this_node):
    # Gen Gunpart Nodes as needed

    for group in groupParentDict.keys():
        gunPartNodeName = group.name
        gunPart = GunPart.gunpart(gunPartNodeName)
        gunPartNode = gunPart.createGunpartNode()
        gunPartList.append(gunPart)
        #print(gunPartNode)
        gunPartNode.parm("file").set(WPN_Utils.linkExpressionSTR("file", True, True))
        linkParms(this_node, gunPartNode, gunPart.parmPrefix)

    # for gpType in gpTypes:
    #     multiparm = this_node.parm("numOf_" + gpType.name)
    #     if multiparm != None:
    #         #print(gpType.name + " multiparm found :" + multiparm.name())
    #         #print("MultiParm Length :" + str(multiparm.eval()))
    #         multiparmLen = multiparm.eval()
    #         for i in range(multiparmLen):
    #             gunPartNodeName = gpType.name
    #             gunPart = GunPart.gunpart(gunPartNodeName, gpType, i)
    #             gunPartNode = gunPart.createGunpartNode()
    #             gunPartList.append(gunPart)
    #             #print(gunPartNode)
    #             gunPartNode.parm("file").set(WPN_Utils.linkExpressionSTR("file", True, True))
    #             linkParms(this_node, gunPartNode, gunPart.parmPrefix)

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
    global psdFilepath
    psdFilepath = this_node.parm("file").eval()
    psd = PSDImage.open(psdFilepath)
    for i, layer in enumerate(psd):
        getChildOfLayer(layer)
    if debug:
        print("DEBUG: ParentChildDict ( Parent <Group> : Child <Group>/<Layer> )")
        pprint.pprint(parentChildDict)


    return parentChildDict


def getChildOfLayer(layer):
    if layer.is_group():
        if debug:
            print( "DEBUG: " + layer.name + " is Group")
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
