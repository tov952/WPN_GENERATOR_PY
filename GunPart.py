import hou


class gunpart():

    def __init__(self, name, GPType,  index):


        self.name = name + "_" + str(index+1)
        self.parmPrefix = GPType.name + str(index+1)
        self.nodeType = "Jason_GunPart"
        self.GPType = GPType
        self.node = None
        self.containerName = name+"_CONTAINER"
        self.container = None


    def createGunpartNode(self):
        #print(self.containerName)
        HDA = hou.pwd()
        geoContainer = HDA.node("GEO_CONTAINER")
        inputGeoContainer1 = geoContainer.indirectInputs()[0]
        self.container = geoContainer.node(self.containerName)
        if self.container == None:
            self.container = geoContainer.createNode("subnet", self.containerName)
            self.container.setInput(0, inputGeoContainer1)
            self.container.moveToGoodPosition()
        input1 = self.container.indirectInputs()[0]
        gunpartNode = self.container.createNode(self.nodeType, self.name)
        gunpartNode.setInput(0, input1)
        gunpartNode.moveToGoodPosition()
        print("Created: " + gunpartNode.name())
        return gunpartNode




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




