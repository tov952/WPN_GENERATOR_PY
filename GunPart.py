import enum
import hou

class GPType(enum.Enum):
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


class gunpart():

    def __init__(self, name, GPType):

        name = name
        nodeType = "Jason_GunPart"
        GPType = GPType
        node = None
        container = name+"_CONTAINER"


    def createGunpartNode(self):
        HDA = hou.pwd()
        HDA.node(self.container).createNode(self.nodeType, self.name)



'''
barrel = gunpart("Barrel", GPType.BRRL)
triggerGuard = gunpart("Trigger_Guard", GPType.TRGR_GRD)
trigger = gunpart("Trigger", GPType.TRGR)
grip = gunpart("Grip", GPType.GRIP)
magazine = gunpart("Magazine", GPType.MGZN)
magwell = gunpart("Magwell", GPType.MGWL)
handguard = gunpart("Handguard", GPType.HDGRD)
chamber = gunpart("Chamber", GPType.CHMBR)
muzzle = gunpart("Muzzle", GPType.MZZL)
carryingHandle = gunpart("Carrying_Handle", GPType.CRRY_HNDLE)
rearSight = gunpart("Rear Sight", GPType.REAR_SGHT)
frontSight = gunpart("Front_Sight", GPType.FRNT_SGHT)
bufferTube = gunpart("Buffer_Tube", GPType.BFFR_TUBE)
chargingHandle = gunpart("Charging_Handle", GPType.CHRG_HNDLE)
stock = gunpart("Stock", GPType.STCK)
buttplate = gunpart("Butt_Plate", GPType.BUTT_PLT)
receiver = gunpart  ("Receiver", GPType.RCVR)
'''




