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
    targetNodePath += this_parmPrefix
    #print(targetNodePath)
    targetNode = this_node.node(targetNodePath)
    target = targetNode.parm("crveShpProfile")

    this_ramp = this_parm.eval()
    #print(this_ramp.keys())
    #print(this_ramp.values())
    #print(target.eval())
    target.set(this_parm.evalAsRampAtFrame(0))