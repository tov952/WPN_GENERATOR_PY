from WPN_GENERATOR_PY import PSDAssetClasses as psdAsset
from WPN_GENERATOR_PY import WPN_Utils

import fnmatch
import pprint
import imp
import inspect
from functools import wraps
imp.reload(psdAsset)

gunPartHDAName = "GUNPART_ASSET"
cutoutHDAName = "CUTOUT_ASSET"

debug = False



class GunPartContainer(psdAsset.Container):
    def childAssetDefinition(self, childLayerName, childlayer):
        if childLayerName == "SIDE":
            #print(childlayer.name + " is SIDE! Creating GunPartAsset")
            childAsset = GunPartAsset(childlayer, self)
        elif childLayerName == "CUTOUT":
            #print(childlayer.name + " is CUTOUT! Creating CutoutAsset")
            childAsset = CutoutAsset(childlayer, self)
        else:
            childAsset = None
        return childAsset



class GunPartAsset(psdAsset.ChildAsset):
    def __init__(self, *args, **kwargs):
        super( GunPartAsset, self).__init__(*args, **kwargs)
        self.nodeType = gunPartHDAName
        self.frontLayer = self.setToSameDepthLayer(self.layerPrefix + "_FRONT")
        self.spineLayer = self.setToSameDepthLayer(self.layerPrefix + "_SPINE")
        self.topLayer = self.setToSameDepthLayer(self.layerPrefix + "_TOP" )
        self.cylShape = self.setToSameDepthLayer(self.layerPrefix + "_CYL")
        self.cutoutObjs = []


        self.parmLayerDict = { "layer_name1": self.layer,
                          "FRONT_layer_name1": self.frontLayer,
                          "TOP_layer_name1": self.topLayer,
                          "SPINE_layer_name1": self.spineLayer,
                          }
        self.flatParmMods = ["zThickness"]
        self.parmModFactor = {"zThickness": 0.85} #Parms to mult modify (mult)


    def setToSameDepthLayer(self, layerName):
        if debug:
            print("DEBUG: Finding: " + layerName)
        foundLayer = None
        for layer in self.parentObj.PSDGroup.descendants():
            #print("parentObj.psdGroup :" + layer.name)
            if fnmatch.fnmatch(layer.name, layerName):
                foundLayer = layer
                if debug:
                    print("DEBUG: " + self.name + " Found " + layer.name)
                return foundLayer
        if foundLayer == None:
            if debug:
                print("No " + layerName + " layer found!" )


    def getCutoutObjs(self):
        if debug:
            print("DEBUG: Finding Cutouts for :" + self.name)
        for layer in self.parentObj.PSDGroup.descendants():
            #print("Hue" + self.layerPrefix+"_CUTOUT*")
            #print("que? " + layer.name)
            if fnmatch.fnmatch(layer.name, self.layerPrefix+"_CUTOUT*"):
                if debug:
                    print("DEBUG: " + self.name + " Found " + layer.name)
                for parentObjChild in self.parentObj.childAssetObjs:
                    if parentObjChild.layer.name == layer.name:
                        self.cutoutObjs.append(parentObjChild)
                        break
        if debug:
            print("DEBUG: " + self.name + " CutoutObjs is :")
            pprint.pprint(self.cutoutObjs)
        #if len(self.cutoutObjs) == 0:
            #print("No Cutout Objects Found!")


    def linkCutoutObj(self):
        #print("DEBUG: Linking CutoutObj to " + self.name)
        for cutoutObj in self.cutoutObjs:
            cutoutObj.ObjToCutout = self

    def triggerCutoutObjLink(self):
        for cutoutObj in self.cutoutObjs:
            cutoutObj.linkCutoutParentThickness()


    def setCarvedShape(self):

        if self.frontLayer != None and self.topLayer != None:
            if debug:
                print("DEBUG: Both Front and Top Layer Exists! Setting Shape Profile to Both")
            self.node.parm("crveShp").set(3)
        elif self.frontLayer != None:
            if debug:
                print("DEBUG: Front Layer Exists! Setting Shape Profile to FRONT")
            self.node.parm("crveShp").set(1)
        elif self.frontLayer != None:
            if debug:
                print("DEBUG: Top Layer Exists! Setting Shape Profile to TOP")
                self.node.parm("crveShp").set(2)

    def setUseDrawnSpine(self):

        if self.spineLayer != None:
            if debug:
                print("DEBUG: Spine Layer Exists! Setting Shape Profile to True")
            self.node.parm("contourBased").set(1)
            self.node.parm("useDrawnSpine").set(1)

    def setShape(self):
        if self.cylShape != None:
            if debug:
                print("DEBUG: Cyl Layer Exists! Setting Shape Switch to Cylindrical")
            self.node.parm("shpSwitch").set(0)

    def setCutoutPattern(self):
        if len(self.cutoutObjs) != 0:
            if debug:
                print("DEBUG: CutoutObjs Exists! Setting CutoutPattern")
            CutoutPattern = ''.join([i for i in self.cutoutObjs[0].name if not i.isdigit()])+"*"
            self.node.parm("cutoutPattern").set(CutoutPattern)

    def postNodeCreation(self, *args, **kwargs):
        super( GunPartAsset, self).postNodeCreation(*args, **kwargs)
        self.setLayerNameParms()
        self.setCarvedShape()
        self.setUseDrawnSpine()
        self.setShape()







class CutoutAsset(psdAsset.ChildAsset):
    def __init__(self, *args, **kwargs):
        super( CutoutAsset, self).__init__(*args, **kwargs)
        self.nodeType = cutoutHDAName
        self.parmLayerDict = { "layer_name1": self.layer}
        self.ObjToCutout = None

    def linkCutoutParentThickness(self):
        print("Linking parent thickness of " + self.name )
        print(self.ObjToCutout.name)
        thicknessParm = self.ObjToCutout.node.parm("zThickness")
        self.node.parm("prntThickness").set(thicknessParm)

    def postNodeCreation(self, *args, **kwargs):
        super(CutoutAsset, self).postNodeCreation(*args, **kwargs)
        self.node.setDisplayFlag(False)




