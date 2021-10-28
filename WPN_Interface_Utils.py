def empty(this_node):
    geoCon = this_node.node("GEO_CONTAINER")
    for child in geoCon.children():
        child.destroy()
    this_node.removeSpareParms()

def reload(this_node):
    geoCon = this_node.node("GEO_CONTAINER")
    containers = geoCon.glob("*_CONTAINER")
    for container in containers:
        nodes = container.children()
        for node in nodes:
            node.parm("reload").pressButton()


def setRamp(this_parm, this_node, targetNodePath):
    this_parmNameSplit = this_parm.name().split("_")
    this_parmPrefix = '_'.join(this_parmNameSplit[0:-1])
    targetParmName = this_parmNameSplit[-1]
    print(targetNodePath)
    targetNode = this_node.node(targetNodePath)
    target = targetNode.parm(targetParmName)

    this_ramp = this_parm.eval()
    #print(this_ramp.keys())
    #print(this_ramp.values())
    #print(target.eval())
    target.set(this_parm.evalAsRampAtFrame(0))

def refreshRamps(this_node):
    rampParms = getAllRampParms(this_node)
    for rampParm in rampParms:
        rampParm.pressButton()


def getAllRampParms(this_node):
    rampParms = []
    parms = this_node.parms()
    for parm in parms:
        try:
            parm.evalAsRamp()
            rampParms.append(parm)
        except:
            pass

    return rampParms