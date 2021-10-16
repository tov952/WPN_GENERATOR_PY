import sys
sys.path.append(r"E:\Users\Jason\Documents\houdini18.5\python3.7libs\WPN_GENERATOR_PY\venv\Lib\site-packages")

import enum
from WPN_GENERATOR_PY import GunPart

import fnmatch
from psd_tools  import PSDImage



GEO_CONTAINER = "GEO_CONTAINER"

class GPTypes(enum.Enum):

    BRRL = 1
    TRGR_GRD = 2
    TRGR =3
    GRIP = 4
    MGZN = 5
    MGWL = 6
    HDGRD = 8
    CHMBR = 9
    MZZL = 10
    CRRY_HNDLE = 11
    REAR_SGHT = 12
    FRNT_SGHT = 13
    BFFR_TUBE = 14
    CHRG_HNDLE = 15
    STCK = 16
    BUTT_PLT = 17
    RCVR = 18

GPTypesNiceName = {    GPTypes.BRRL: "Barrel",
                        GPTypes.TRGR_GRD: "TriggerGuard",
                        GPTypes.TRGR: "Trigger",
                        GPTypes.GRIP: "Grip",
                        GPTypes.MGZN: "Magazine",
                        GPTypes.MGWL: "Magwell",
                        GPTypes.HDGRD: "Handguard",
                        GPTypes.CHMBR: "Chamber",
                        GPTypes.MZZL: "Muzzle",
                        GPTypes.CRRY_HNDLE: "CarryingHandle",
                        GPTypes.REAR_SGHT: "RearSight",
                        GPTypes.FRNT_SGHT: "FrontSight",
                        GPTypes.BFFR_TUBE: "BufferTube",
                        GPTypes.CHRG_HNDLE: "ChargingHandle",
                        GPTypes.STCK: "Stock",
                        GPTypes.BUTT_PLT: "ButtPlate",
                        GPTypes.RCVR: "Receiver"}


def rebuild(this_node):

    #Gets list of valid layers based on enum and not empty layers.
    filepath = this_node.parm("file").eval()
    psd = PSDImage.open(filepath)
    gpTypesNames = [gpType.name for gpType in GPTypes]
    layerNames = []
    validLayerNames = []
    #print(gpTypesNames)
    for i, layer in enumerate(psd):
        #print(layer.name)
        if layer.size != (0,0):
            layerNames.append(layer.name)
            #print("layer empty")
    print("..............")
    for gpTypesName in gpTypesNames:
        #print(gpTypesName)
        if len(fnmatch.filter(layerNames, gpTypesName+"*")) != 0:
            validLayerNames += fnmatch.filter(layerNames, gpTypesName+"*")
    print(list(set(validLayerNames)))



    #print(layerNames)



    geoContainer = this_node.node(GEO_CONTAINER)

    #Cleans Geo Container
    for child in geoContainer.children():
        child.destroy()

    #Gen Gunpart Nodes as needed
    gpTypes = GPTypes
    for gpType in gpTypes:
        multiparm = this_node.parm("numOf_" + gpType.name)
        if multiparm != None:
            print(gpType.name + " multiparm found :" + multiparm.name() )
            print("MultiParm Length :" + str(multiparm.eval()))
            multiparmLen = multiparm.eval()
            for i in range(multiparmLen):
                gunPartNodeName =GPTypesNiceName[gpType]
                gunPart = GunPart.gunpart(gunPartNodeName,gpType, i)
                gunPartNode = gunPart.createGunpartNode()
                print(gunPartNode)
                gunPartNode.parm("layer_name1").set(gunPart.parmPrefix)
                gunPartNode.parm("file").set(linkExpressionSTR("file", True, True))
                linkParms(this_node, gunPartNode, gunPart.parmPrefix)
    geoContainer.layoutChildren()
    for child in geoContainer.children():
        child.layoutChildren()


def linkExpressionSTR(parmSource, force_evaluate = False, string = False):
    ch = "ch"
    if force_evaluate == True:
        ch = "`ch"
    if string == True:
        ch += "s"
    return ch+"('../../../" + parmSource + "')"

def linkParms(this_node, gunPartNode, gunPartPrefix):
    gunPartParms = this_node.globParms(gunPartPrefix + "_*")
    unprefixedParmsName = [parm.name().replace(gunPartPrefix + "_", "") for parm in gunPartParms]
    for i, unprefixedParmName in enumerate(unprefixedParmsName):
        parmSource = gunPartParms[i]
        parmTarget = gunPartNode.parm(unprefixedParmName)

        parmTarget.setExpression(linkExpressionSTR(parmSource.name()))
    #print(gunPartParmsNameOnly)

