# Code for parameter template
hou_parm_template = hou.FolderSetParmTemplate("stdswitcher", folder_names=(["","",""]), folder_type=hou.folderType.Tabs)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("xOrd", "Transform Order", menu_items=(["srt","str","rst","rts","tsr","trs"]), menu_labels=(["Scale Rot Trans","Scale Trans Rot","Rot Scale Trans","Rot Trans Scale","Trans Scale Rot","Trans Rot Scale"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.setJoinWithNext(True)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("rOrd", "Rotate Order", menu_items=(["xyz","xzy","yxz","yzx","zxy","zyx"]), menu_labels=(["Rx Ry Rz","Rx Rz Ry","Ry Rx Rz","Ry Rz Rx","Rz Rx Ry","Rz Ry Rx"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.hideLabel(True)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("t", "Translate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 0)", "script_action_help": "Select an object to match the translation with.", "script_action_icon": "BUTTONS_match_transform"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("t", "Translate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 0)", "script_action_help": "Select an object to match the translation with.", "script_action_icon": "BUTTONS_match_transform"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("t", "Translate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 0)", "script_action_help": "Select an object to match the translation with.", "script_action_icon": "BUTTONS_match_transform"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("r", "Rotate", 3, default_value=([0, 0, 0]), min=0, max=360, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 1)", "script_action_help": "Select an object to match the rotation with.", "script_action_icon": "BUTTONS_match_rotation"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("r", "Rotate", 3, default_value=([0, 0, 0]), min=0, max=360, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 1)", "script_action_help": "Select an object to match the rotation with.", "script_action_icon": "BUTTONS_match_rotation"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("r", "Rotate", 3, default_value=([0, 0, 0]), min=0, max=360, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 1)", "script_action_help": "Select an object to match the rotation with.", "script_action_icon": "BUTTONS_match_rotation"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("s", "Scale", 3, default_value=([1, 1, 1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 2)", "script_action_help": "Select an object to match the scale with.", "script_action_icon": "BUTTONS_match_scale"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("s", "Scale", 3, default_value=([1, 1, 1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 2)", "script_action_help": "Select an object to match the scale with.", "script_action_icon": "BUTTONS_match_scale"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("s", "Scale", 3, default_value=([1, 1, 1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 2)", "script_action_help": "Select an object to match the scale with.", "script_action_icon": "BUTTONS_match_scale"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("p", "Pivot Translate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 3)", "script_action_help": "Select an object to match the pivot with.", "script_action_icon": "BUTTONS_match_pivot"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("p", "Pivot Translate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 3)", "script_action_help": "Select an object to match the pivot with.", "script_action_icon": "BUTTONS_match_pivot"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("p", "Pivot Translate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 3)", "script_action_help": "Select an object to match the pivot with.", "script_action_icon": "BUTTONS_match_pivot"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("pr", "Pivot Rotate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 4)", "script_action_help": "Select an object to match the pivot rotation with.", "script_action_icon": "BUTTONS_match_pivot_rotation"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("pr", "Pivot Rotate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 4)", "script_action_help": "Select an object to match the pivot rotation with.", "script_action_icon": "BUTTONS_match_pivot_rotation"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("pr", "Pivot Rotate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 4)", "script_action_help": "Select an object to match the pivot rotation with.", "script_action_icon": "BUTTONS_match_pivot_rotation"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("scale", "Uniform Scale", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("pre_xform", "Modify Pre-Transform", menu_items=(["clean","cleantrans","cleanrot","cleanscales","extract","reset"]), menu_labels=(["Clean Transform","Clean Translates","Clean Rotates","Clean Scales","Extract Pre-transform","Reset Pre-transform"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("keeppos", "Keep Position When Parenting", default_value=False)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("childcomp", "Child Compensation", default_value=False)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("constraints_on", "Enable Constraints", default_value=False)
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("constraints_path", "Constraints", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setConditional(hou.parmCondType.HideWhen, "{ constraints_on == 0 }")
hou_parm_template.setTags({"opfilter": "!!CHOP", "oprelative": ".", "script_action": "import objecttoolutils\nobjecttoolutils.constraintsMenu(kwargs)", "script_action_help": "", "script_action_icon": "BUTTONS_add_constraints"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("lookatpath", "Look At", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.hide(True)
hou_parm_template.setTags({"opfilter": "!!OBJ!!", "oprelative": "."})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("lookupobjpath", "Look Up Object", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.hide(True)
hou_parm_template.setTags({"opfilter": "!!OBJ!!", "oprelative": "."})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("lookup", "Look At Up Vector", 1, default_value=(["on"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["off","on","quat","pos","obj"]), menu_labels=(["Don't Use Up Vector","Use Up Vector","Use Quaternions","Use Global Position","Use Up Object"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("pathobjpath", "Path Object", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.hide(True)
hou_parm_template.setTags({"opfilter": "!!SOP!!", "oprelative": "."})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("roll", "Roll", 1, default_value=([0]), min=-360, max=360, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Angle, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("pos", "Position", 1, default_value=([0]), min=0, max=10, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("uparmtype", "Parameterization", menu_items=(["uniform","arc"]), menu_labels=(["Uniform","Arc Length"]), default_value=1, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.IntParmTemplate("pathorient", "Orient Along Path", 1, default_value=([1]), min=0, max=1, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("up", "Orient Up Vector", 3, default_value=([0, 1, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Vector, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("up", "Orient Up Vector", 3, default_value=([0, 1, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Vector, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("up", "Orient Up Vector", 3, default_value=([0, 1, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Vector, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("bank", "Auto-Bank factor", 1, default_value=([0]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("shop_materialpath", "Material", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setTags({"opfilter": "!!CUSTOM/MATERIAL!!", "oprelative": "."})
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("shop_materialopts", "Options", menu_items=([]), menu_labels=([]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Mini, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("tdisplay", "Display", default_value=False)
hou_parm_template.setJoinWithNext(True)
# Code for parameter template
hou_parm_template = hou.IntParmTemplate("display", "Display", 1, default_value=([1]), min=0, max=1, min_is_strict=True, max_is_strict=True, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("use_dcolor", "Set Wireframe Color", default_value=False)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("dcolor", "Wireframe Color", 3, default_value=([1, 1, 1]), min=0, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.ColorSquare, naming_scheme=hou.parmNamingScheme.RGBA)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("dcolor", "Wireframe Color", 3, default_value=([1, 1, 1]), min=0, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.ColorSquare, naming_scheme=hou.parmNamingScheme.RGBA)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("dcolor", "Wireframe Color", 3, default_value=([1, 1, 1]), min=0, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.ColorSquare, naming_scheme=hou.parmNamingScheme.RGBA)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("picking", "Viewport Selecting Enabled", default_value=True)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("pickscript", "Select Script", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.FileReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
hou_parm_template.hide(True)
hou_parm_template.setTags({"filechooser_mode": "read"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("caching", "Cache Object Transform", default_value=True)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vport_shadeopen", "Shade Open Curves In Viewport", default_value=False)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vport_displayassubdiv", "Display as Subdivision in Viewport", default_value=False)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("vport_onionskin", "Onion Skinning", menu_items=(["off","xform","on"]), menu_labels=(["Off","Transform only","Full Deformation"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("renderable", "Renderable", default_value=True)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.FolderSetParmTemplate("parent", folder_names=(["parent","Transform"]), folder_type=hou.folderType.Tabs)
# Code for parameter template
hou_parm_template = hou.FolderSetParmTemplate("trcCTRLs", folder_names=(["Trace Controls"]), folder_type=hou.folderType.Simple)
hou_parm_template.setTags({"group_type": "simple"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("file", "File", 1, default_value=(["$JOB/test2.psd"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.FileReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
hou_parm_template.setJoinWithNext(True)
hou_parm_template.setTags({"autoscope": "0000000000000000", "filechooser_pattern": "*.psd"})
# Code for parameter template
hou_parm_template = hou.ButtonParmTemplate("reload", "Reload PSD")
hou_parm_template.setTags({"autoscope": "0000000000000000"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("layer_name1", "Layer Name", 1, default_value=(["LWR_RCVR"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="opmenu -l -a trace_psd_file1 layer_name1", item_generator_script_language=hou.scriptLanguage.Hscript, menu_type=hou.menuType.StringReplace)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("thresh1", "Brightness Threshold", 1, default_value=([0.139]), min=0, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setTags({"autoscope": "0000000000000000"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("step1", "Resample Step", 1, default_value=([0.52]), min=0.001, max=10, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setTags({"autoscope": "0000000000000000"})
# Code for parameter template
hou_parm_template = hou.FolderSetParmTemplate("genShpCTRLs", folder_names=(["General Shape Controls"]), folder_type=hou.folderType.Simple)
hou_parm_template.setTags({"group_type": "simple"})
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("shpSwitch", "Shape Switch", menu_items=(["0","1"]), menu_labels=(["Cylindrical","Flat"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FolderSetParmTemplate("cylCTRLs", folder_names=(["Cylindrical Controls"]), folder_type=hou.folderType.Simple)
hou_parm_template.setTags({"group_type": "simple"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("scale2", "Scale", 3, default_value=([1, 1, 1]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("scale2", "Scale", 3, default_value=([1, 1, 1]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("scale2", "Scale", 3, default_value=([1, 1, 1]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.IntParmTemplate("sides", "Sides", 1, default_value=([12]), min=1, max=50, min_is_strict=True, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("WallThickness", "Wall Thickness", 1, default_value=([0]), min=-0.2, max=0.2, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FolderSetParmTemplate("flatCTRLs", folder_names=(["Flat Controls"]), folder_type=hou.folderType.Simple)
hou_parm_template.setTags({"group_type": "simple"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("zThickness", "Z-Thickness", 1, default_value=([0.012]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("crveShp", "Carved Shape", default_value=False)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FolderSetParmTemplate("xShpCTRLs", folder_names=(["Cross-Section Controls"]), folder_type=hou.folderType.Simple)
hou_parm_template.setTags({"group_type": "simple"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("xChamfer", "Chamfer", 1, default_value=([0.096]), min=0, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.RampParmTemplate("crveShpProfile", "Carved Shape Profile", hou.rampParmType.Float, default_value=3, default_basis=None, color_type=None)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "rampfloatdefault": "1pos ( 0 ) 1value ( 0 ) 1interp ( linear ) 2pos ( 0.0066137565299868584 ) 2value ( 1 ) 2interp ( linear ) 3pos ( 1 ) 3value ( 1 ) 3interp ( linear )", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("contourBased", "Contour-based", default_value=False, default_expression='off', default_expression_language=hou.scriptLanguage.Hscript)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FolderSetParmTemplate("contourControls", folder_names=(["Contour Controls"]), folder_type=hou.folderType.Simple)
hou_parm_template.setTags({"group_type": "simple"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("yxAxis", "Y/X Axis", default_value=False, default_expression='off', default_expression_language=hou.scriptLanguage.Hscript)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("scaleY", "Carver Margin Scale ", 1, default_value=([4.06]), min=-10, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("scaleX", "Carver Thickness Scale", 1, default_value=([1]), min=-10, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("strength", "Carver Smoothness", 1, default_value=([0]), min=0, max=50, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.IntParmTemplate("segs", "Carver Resolution", 1, default_value=([9]), min=1, max=50, min_is_strict=True, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("bias", "Carver Spine Bias", 1, default_value=([1]), min=0, max=2, min_is_strict=True, max_is_strict=True, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FolderSetParmTemplate("bvlCTRLs", folder_names=(["Bevel Controls"]), folder_type=hou.folderType.Simple)
hou_parm_template.setTags({"group_type": "simple"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("bvlFlatAngle", "Bevel Flat Angle", 1, default_value=([51.8]), min=0, max=180, min_is_strict=True, max_is_strict=True, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("bvlWidth", "Bevel Width", 1, default_value=([0.002]), min=0, max=1, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FolderSetParmTemplate("parent_2", folder_names=(["Render"]), folder_type=hou.folderType.Tabs)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("viewportlod", "Display As", menu_items=(["full","points","box","centroid","hidden","subd"]), menu_labels=(["Full Geometry","Point Cloud","Bounding Box","Centroid","Hidden","Subdivision Surface / Curves"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.setHelp("Choose how the object's geometry should be rendered in the viewport")
hou_parm_template.setTags({"spare_category": "Render"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("vm_rendervisibility", "Render Visibility", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["*","primary","primary|shadow","-primary","-diffuse","-diffuse&-reflect&-refract",""]), menu_labels=(["Visible to all","Visible only to primary rays","Visible only to primary and shadow rays","Invisible to primary rays (Phantom)","Invisible to diffuse rays","Invisible to secondary rays","Invisible (Unrenderable)"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "rendervisibility", "spare_category": "Render"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_rendersubd", "Render Polygons As Subdivision (Mantra)", default_value=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "rendersubd", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("vm_subdstyle", "Subdivision Style", 1, default_value=(["mantra_catclark"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["mantra_catclark","osd_catclark"]), menu_labels=(["Mantra Catmull-Clark","OpenSubdiv Catmull-Clark"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 }")
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "subdstyle", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("vm_subdgroup", "Subdivision Group", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 }")
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "subdgroup", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("vm_osd_quality", "Open Subdiv Quality", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 vm_subdstyle != osd_catclark }")
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "osd_quality", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.IntParmTemplate("vm_osd_vtxinterp", "OSD Vtx Interp", 1, default_value=([2]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["No vertex interpolation","Edges only","Edges and Corners"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 vm_subdstyle != osd_catclark }")
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "osd_vtxinterp", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.IntParmTemplate("vm_osd_fvarinterp", "OSD FVar Interp", 1, default_value=([4]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2","3","4","5"]), menu_labels=(["Smooth everywhere","Sharpen corners only","Sharpen edges and corners","Sharpen edges and propagated corners","Sharpen all boundaries","Bilinear interpolation"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 vm_subdstyle != osd_catclark }")
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "osd_fvarinterp", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.FolderSetParmTemplate("folder0", folder_names=(["Shading","Sampling","Dicing","Geometry"]), folder_type=hou.folderType.Tabs)
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("categories", "Categories", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setHelp("A list of tags which can be used to select the object")
hou_parm_template.setTags({"spare_category": "Shading"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("reflectmask", "Reflection Mask", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReferenceList, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setHelp("Objects that will be reflected on this object.")
hou_parm_template.setTags({"opexpand": "1", "opfilter": "!!OBJ/GEOMETRY!!", "oprelative": "/obj", "spare_category": "Shading"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("refractmask", "Refraction Mask", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReferenceList, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setHelp("Objects that will be refracted on this object.")
hou_parm_template.setTags({"opexpand": "1", "opfilter": "!!OBJ/GEOMETRY!!", "oprelative": "/obj", "spare_category": "Shading"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("lightmask", "Light Mask", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReferenceList, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setHelp("Lights that illuminate this object.")
hou_parm_template.setTags({"opexpand": "1", "opfilter": "!!OBJ/LIGHT!!", "oprelative": "/obj", "spare_category": "Shading"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("lightcategories", "Light Selection", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setTags({"spare_category": "Shading"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("vm_lpetag", "LPE Tag", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "lpetag", "spare_category": "Shading"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("vm_volumefilter", "Volume Filter", 1, default_value=(["box"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["box","gaussian","bartlett","catrom","hanning","blackman","sinc"]), menu_labels=(["Box Filter","Gaussian","Bartlett (triangle)","Catmull-Rom","Hanning","Blackman","Sinc (sharpening)"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "filter", "spare_category": "Shading"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("vm_volumefilterwidth", "Volume Filter Width", 1, default_value=([1]), min=0.001, max=5, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "filterwidth", "spare_category": "Shading"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_matte", "Matte shading", default_value=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "matte", "spare_category": "Shading"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_rayshade", "Raytrace Shading", default_value=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "rayshade", "spare_category": "Shading"})
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("geo_velocityblur", "Geometry Velocity Blur", menu_items=(["off","on","accelblur"]), menu_labels=(["No Velocity Blur","Velocity Blur","Acceleration Blur"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.setConditional(hou.parmCondType.DisableWhen, "{ allowmotionblur == 0 }")
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("geo_accelattribute", "Acceleration Attribute", 1, default_value=(["accel"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setConditional(hou.parmCondType.HideWhen, "{ geo_velocityblur != accelblur }")
hou_parm_template.setTags({"spare_category": "Sampling"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("vm_shadingquality", "Shading Quality", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "shadingquality", "spare_category": "Dicing"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("vm_flatness", "Dicing Flatness", 1, default_value=([0.05]), min=0, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "flatness", "spare_category": "Dicing"})
# Code for parameter template
hou_parm_template = hou.IntParmTemplate("vm_raypredice", "Ray Predicing", 1, default_value=([0]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["Disable Predicing","Full Predicing","Precompute Bounds"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "raypredice", "spare_category": "Dicing"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_curvesurface", "Shade Curves As Surfaces", default_value=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "curvesurface", "spare_category": "Dicing"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_rmbackface", "Backface Removal", default_value=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "rmbackface", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("shop_geometrypath", "Procedural Shader", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setTags({"opfilter": "!!SHOP/GEOMETRY!!", "oprelative": ".", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_forcegeometry", "Force Procedural Geometry Output", default_value=True)
hou_parm_template.setTags({"spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_rendersubdcurves", "Render Polygon Curves As Subdivision (Mantra)", default_value=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "rendersubdcurves", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.IntParmTemplate("vm_renderpoints", "Render As Points (Mantra)", 1, default_value=([2]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["No Point Rendering","Render Only Points","Render Unconnected Points"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "renderpoints", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.IntParmTemplate("vm_renderpointsas", "Render Points As (Mantra)", 1, default_value=([0]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1"]), menu_labels=(["Spheres","Circles"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.setConditional(hou.parmCondType.DisableWhen, "{ vm_renderpoints == 0 }")
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "renderpointsas", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_usenforpoints", "Use N For Point Rendering", default_value=False)
hou_parm_template.setConditional(hou.parmCondType.DisableWhen, "{ vm_renderpoints == 0 }")
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "usenforpoints", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("vm_pointscale", "Point Scale", 1, default_value=([1]), min=0, max=10, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setConditional(hou.parmCondType.DisableWhen, "{ vm_renderpoints == 0 }")
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "pointscale", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_pscalediameter", "Treat Point Scale as Diameter Instead of Radius", default_value=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "pscalediameter", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_metavolume", "Metaballs as Volume", default_value=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "metavolume", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.IntParmTemplate("vm_coving", "Coving", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["Disable Coving","Coving for displacement/sub-d","Coving for all primitives"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "coving", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("vm_materialoverride", "Material Override", 1, default_value=(["compact"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["none","full","compact"]), menu_labels=(["Disabled","Evaluate for Each Primitve/Point","Evaluate Once"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setTags({"spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_overridedetail", "Ignore Geometry Attribute Shaders", default_value=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "overridedetail", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_procuseroottransform", "Proc Use Root Transform", default_value=True)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "procuseroottransform", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.FolderSetParmTemplate("parent_3", folder_names=(["Misc"]), folder_type=hou.folderType.Tabs)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("crveShpProfile1pos", "Position", 1, default_value=([0]), min=0, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("crveShpProfile1value", "Value", 1, default_value=([0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("crveShpProfile1interp", "Interpolation", menu_items=(["constant","linear","catmull-rom","monotonecubic","bezier","bspline","hermite"]), menu_labels=(["Constant","Linear","Catmull-Rom","Monotone Cubic","Bezier","B-Spline","Hermite"]), default_value=1, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("crveShpProfile2pos", "Position", 1, default_value=([0]), min=0, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("crveShpProfile2value", "Value", 1, default_value=([0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("crveShpProfile2interp", "Interpolation", menu_items=(["constant","linear","catmull-rom","monotonecubic","bezier","bspline","hermite"]), menu_labels=(["Constant","Linear","Catmull-Rom","Monotone Cubic","Bezier","B-Spline","Hermite"]), default_value=1, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("crveShpProfile3pos", "Position", 1, default_value=([0]), min=0, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("crveShpProfile3value", "Value", 1, default_value=([0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("crveShpProfile3interp", "Interpolation", menu_items=(["constant","linear","catmull-rom","monotonecubic","bezier","bspline","hermite"]), menu_labels=(["Constant","Linear","Catmull-Rom","Monotone Cubic","Bezier","B-Spline","Hermite"]), default_value=1, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
# Code for parameter template
hou_parm_template = hou.FolderSetParmTemplate("stdswitcher", folder_names=(["","",""]), folder_type=hou.folderType.Tabs)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("xOrd", "Transform Order", menu_items=(["srt","str","rst","rts","tsr","trs"]), menu_labels=(["Scale Rot Trans","Scale Trans Rot","Rot Scale Trans","Rot Trans Scale","Trans Scale Rot","Trans Rot Scale"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.setJoinWithNext(True)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("rOrd", "Rotate Order", menu_items=(["xyz","xzy","yxz","yzx","zxy","zyx"]), menu_labels=(["Rx Ry Rz","Rx Rz Ry","Ry Rx Rz","Ry Rz Rx","Rz Rx Ry","Rz Ry Rx"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.hideLabel(True)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("t", "Translate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 0)", "script_action_help": "Select an object to match the translation with.", "script_action_icon": "BUTTONS_match_transform"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("t", "Translate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 0)", "script_action_help": "Select an object to match the translation with.", "script_action_icon": "BUTTONS_match_transform"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("t", "Translate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 0)", "script_action_help": "Select an object to match the translation with.", "script_action_icon": "BUTTONS_match_transform"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("r", "Rotate", 3, default_value=([0, 0, 0]), min=0, max=360, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 1)", "script_action_help": "Select an object to match the rotation with.", "script_action_icon": "BUTTONS_match_rotation"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("r", "Rotate", 3, default_value=([0, 0, 0]), min=0, max=360, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 1)", "script_action_help": "Select an object to match the rotation with.", "script_action_icon": "BUTTONS_match_rotation"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("r", "Rotate", 3, default_value=([0, 0, 0]), min=0, max=360, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 1)", "script_action_help": "Select an object to match the rotation with.", "script_action_icon": "BUTTONS_match_rotation"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("s", "Scale", 3, default_value=([1, 1, 1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 2)", "script_action_help": "Select an object to match the scale with.", "script_action_icon": "BUTTONS_match_scale"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("s", "Scale", 3, default_value=([1, 1, 1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 2)", "script_action_help": "Select an object to match the scale with.", "script_action_icon": "BUTTONS_match_scale"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("s", "Scale", 3, default_value=([1, 1, 1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 2)", "script_action_help": "Select an object to match the scale with.", "script_action_icon": "BUTTONS_match_scale"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("p", "Pivot Translate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 3)", "script_action_help": "Select an object to match the pivot with.", "script_action_icon": "BUTTONS_match_pivot"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("p", "Pivot Translate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 3)", "script_action_help": "Select an object to match the pivot with.", "script_action_icon": "BUTTONS_match_pivot"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("p", "Pivot Translate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 3)", "script_action_help": "Select an object to match the pivot with.", "script_action_icon": "BUTTONS_match_pivot"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("pr", "Pivot Rotate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 4)", "script_action_help": "Select an object to match the pivot rotation with.", "script_action_icon": "BUTTONS_match_pivot_rotation"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("pr", "Pivot Rotate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 4)", "script_action_help": "Select an object to match the pivot rotation with.", "script_action_icon": "BUTTONS_match_pivot_rotation"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("pr", "Pivot Rotate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setTags({"script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 4)", "script_action_help": "Select an object to match the pivot rotation with.", "script_action_icon": "BUTTONS_match_pivot_rotation"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("scale", "Uniform Scale", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("pre_xform", "Modify Pre-Transform", menu_items=(["clean","cleantrans","cleanrot","cleanscales","extract","reset"]), menu_labels=(["Clean Transform","Clean Translates","Clean Rotates","Clean Scales","Extract Pre-transform","Reset Pre-transform"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("keeppos", "Keep Position When Parenting", default_value=False)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("childcomp", "Child Compensation", default_value=False)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("constraints_on", "Enable Constraints", default_value=False)
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("constraints_path", "Constraints", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setConditional(hou.parmCondType.HideWhen, "{ constraints_on == 0 }")
hou_parm_template.setTags({"opfilter": "!!CHOP", "oprelative": ".", "script_action": "import objecttoolutils\nobjecttoolutils.constraintsMenu(kwargs)", "script_action_help": "", "script_action_icon": "BUTTONS_add_constraints"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("lookatpath", "Look At", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.hide(True)
hou_parm_template.setTags({"opfilter": "!!OBJ!!", "oprelative": "."})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("lookupobjpath", "Look Up Object", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.hide(True)
hou_parm_template.setTags({"opfilter": "!!OBJ!!", "oprelative": "."})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("lookup", "Look At Up Vector", 1, default_value=(["on"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["off","on","quat","pos","obj"]), menu_labels=(["Don't Use Up Vector","Use Up Vector","Use Quaternions","Use Global Position","Use Up Object"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("pathobjpath", "Path Object", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.hide(True)
hou_parm_template.setTags({"opfilter": "!!SOP!!", "oprelative": "."})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("roll", "Roll", 1, default_value=([0]), min=-360, max=360, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Angle, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("pos", "Position", 1, default_value=([0]), min=0, max=10, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("uparmtype", "Parameterization", menu_items=(["uniform","arc"]), menu_labels=(["Uniform","Arc Length"]), default_value=1, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.IntParmTemplate("pathorient", "Orient Along Path", 1, default_value=([1]), min=0, max=1, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("up", "Orient Up Vector", 3, default_value=([0, 1, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Vector, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("up", "Orient Up Vector", 3, default_value=([0, 1, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Vector, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("up", "Orient Up Vector", 3, default_value=([0, 1, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Vector, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("bank", "Auto-Bank factor", 1, default_value=([0]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("shop_materialpath", "Material", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setTags({"opfilter": "!!CUSTOM/MATERIAL!!", "oprelative": "."})
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("shop_materialopts", "Options", menu_items=([]), menu_labels=([]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Mini, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("tdisplay", "Display", default_value=False)
hou_parm_template.setJoinWithNext(True)
# Code for parameter template
hou_parm_template = hou.IntParmTemplate("display", "Display", 1, default_value=([1]), min=0, max=1, min_is_strict=True, max_is_strict=True, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("use_dcolor", "Set Wireframe Color", default_value=False)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("dcolor", "Wireframe Color", 3, default_value=([1, 1, 1]), min=0, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.ColorSquare, naming_scheme=hou.parmNamingScheme.RGBA)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("dcolor", "Wireframe Color", 3, default_value=([1, 1, 1]), min=0, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.ColorSquare, naming_scheme=hou.parmNamingScheme.RGBA)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("dcolor", "Wireframe Color", 3, default_value=([1, 1, 1]), min=0, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.ColorSquare, naming_scheme=hou.parmNamingScheme.RGBA)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("picking", "Viewport Selecting Enabled", default_value=True)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("pickscript", "Select Script", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.FileReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
hou_parm_template.hide(True)
hou_parm_template.setTags({"filechooser_mode": "read"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("caching", "Cache Object Transform", default_value=True)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vport_shadeopen", "Shade Open Curves In Viewport", default_value=False)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vport_displayassubdiv", "Display as Subdivision in Viewport", default_value=False)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("vport_onionskin", "Onion Skinning", menu_items=(["off","xform","on"]), menu_labels=(["Off","Transform only","Full Deformation"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("renderable", "Renderable", default_value=True)
hou_parm_template.hide(True)
# Code for parameter template
hou_parm_template = hou.FolderSetParmTemplate("parent_1", folder_names=(["Transform"]), folder_type=hou.folderType.Tabs)
# Code for parameter template
hou_parm_template = hou.FolderSetParmTemplate("parent_2", folder_names=(["Render"]), folder_type=hou.folderType.Tabs)
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("viewportlod", "Display As", menu_items=(["full","points","box","centroid","hidden","subd"]), menu_labels=(["Full Geometry","Point Cloud","Bounding Box","Centroid","Hidden","Subdivision Surface / Curves"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.setHelp("Choose how the object's geometry should be rendered in the viewport")
hou_parm_template.setTags({"spare_category": "Render"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("vm_rendervisibility", "Render Visibility", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["*","primary","primary|shadow","-primary","-diffuse","-diffuse&-reflect&-refract",""]), menu_labels=(["Visible to all","Visible only to primary rays","Visible only to primary and shadow rays","Invisible to primary rays (Phantom)","Invisible to diffuse rays","Invisible to secondary rays","Invisible (Unrenderable)"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "rendervisibility", "spare_category": "Render"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_rendersubd", "Render Polygons As Subdivision (Mantra)", default_value=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "rendersubd", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("vm_subdstyle", "Subdivision Style", 1, default_value=(["mantra_catclark"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["mantra_catclark","osd_catclark"]), menu_labels=(["Mantra Catmull-Clark","OpenSubdiv Catmull-Clark"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 }")
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "subdstyle", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("vm_subdgroup", "Subdivision Group", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 }")
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "subdgroup", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("vm_osd_quality", "Open Subdiv Quality", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 vm_subdstyle != osd_catclark }")
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "osd_quality", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.IntParmTemplate("vm_osd_vtxinterp", "OSD Vtx Interp", 1, default_value=([2]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["No vertex interpolation","Edges only","Edges and Corners"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 vm_subdstyle != osd_catclark }")
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "osd_vtxinterp", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.IntParmTemplate("vm_osd_fvarinterp", "OSD FVar Interp", 1, default_value=([4]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2","3","4","5"]), menu_labels=(["Smooth everywhere","Sharpen corners only","Sharpen edges and corners","Sharpen edges and propagated corners","Sharpen all boundaries","Bilinear interpolation"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 vm_subdstyle != osd_catclark }")
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "osd_fvarinterp", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.FolderSetParmTemplate("folder0", folder_names=(["Shading","Sampling","Dicing","Geometry"]), folder_type=hou.folderType.Tabs)
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("categories", "Categories", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setHelp("A list of tags which can be used to select the object")
hou_parm_template.setTags({"spare_category": "Shading"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("reflectmask", "Reflection Mask", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReferenceList, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setHelp("Objects that will be reflected on this object.")
hou_parm_template.setTags({"opexpand": "1", "opfilter": "!!OBJ/GEOMETRY!!", "oprelative": "/obj", "spare_category": "Shading"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("refractmask", "Refraction Mask", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReferenceList, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setHelp("Objects that will be refracted on this object.")
hou_parm_template.setTags({"opexpand": "1", "opfilter": "!!OBJ/GEOMETRY!!", "oprelative": "/obj", "spare_category": "Shading"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("lightmask", "Light Mask", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReferenceList, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setHelp("Lights that illuminate this object.")
hou_parm_template.setTags({"opexpand": "1", "opfilter": "!!OBJ/LIGHT!!", "oprelative": "/obj", "spare_category": "Shading"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("lightcategories", "Light Selection", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setTags({"spare_category": "Shading"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("vm_lpetag", "LPE Tag", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "lpetag", "spare_category": "Shading"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("vm_volumefilter", "Volume Filter", 1, default_value=(["box"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["box","gaussian","bartlett","catrom","hanning","blackman","sinc"]), menu_labels=(["Box Filter","Gaussian","Bartlett (triangle)","Catmull-Rom","Hanning","Blackman","Sinc (sharpening)"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "filter", "spare_category": "Shading"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("vm_volumefilterwidth", "Volume Filter Width", 1, default_value=([1]), min=0.001, max=5, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "filterwidth", "spare_category": "Shading"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_matte", "Matte shading", default_value=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "matte", "spare_category": "Shading"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_rayshade", "Raytrace Shading", default_value=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "rayshade", "spare_category": "Shading"})
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("geo_velocityblur", "Geometry Velocity Blur", menu_items=(["off","on","accelblur"]), menu_labels=(["No Velocity Blur","Velocity Blur","Acceleration Blur"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.setConditional(hou.parmCondType.DisableWhen, "{ allowmotionblur == 0 }")
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("geo_accelattribute", "Acceleration Attribute", 1, default_value=(["accel"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setConditional(hou.parmCondType.HideWhen, "{ geo_velocityblur != accelblur }")
hou_parm_template.setTags({"spare_category": "Sampling"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("vm_shadingquality", "Shading Quality", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "shadingquality", "spare_category": "Dicing"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("vm_flatness", "Dicing Flatness", 1, default_value=([0.05]), min=0, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "flatness", "spare_category": "Dicing"})
# Code for parameter template
hou_parm_template = hou.IntParmTemplate("vm_raypredice", "Ray Predicing", 1, default_value=([0]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["Disable Predicing","Full Predicing","Precompute Bounds"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "raypredice", "spare_category": "Dicing"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_curvesurface", "Shade Curves As Surfaces", default_value=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "curvesurface", "spare_category": "Dicing"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_rmbackface", "Backface Removal", default_value=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "rmbackface", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("shop_geometrypath", "Procedural Shader", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setTags({"opfilter": "!!SHOP/GEOMETRY!!", "oprelative": ".", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_forcegeometry", "Force Procedural Geometry Output", default_value=True)
hou_parm_template.setTags({"spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_rendersubdcurves", "Render Polygon Curves As Subdivision (Mantra)", default_value=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "rendersubdcurves", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.IntParmTemplate("vm_renderpoints", "Render As Points (Mantra)", 1, default_value=([2]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["No Point Rendering","Render Only Points","Render Unconnected Points"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "renderpoints", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.IntParmTemplate("vm_renderpointsas", "Render Points As (Mantra)", 1, default_value=([0]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1"]), menu_labels=(["Spheres","Circles"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.setConditional(hou.parmCondType.DisableWhen, "{ vm_renderpoints == 0 }")
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "renderpointsas", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_usenforpoints", "Use N For Point Rendering", default_value=False)
hou_parm_template.setConditional(hou.parmCondType.DisableWhen, "{ vm_renderpoints == 0 }")
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "usenforpoints", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("vm_pointscale", "Point Scale", 1, default_value=([1]), min=0, max=10, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setConditional(hou.parmCondType.DisableWhen, "{ vm_renderpoints == 0 }")
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "pointscale", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_pscalediameter", "Treat Point Scale as Diameter Instead of Radius", default_value=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "pscalediameter", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_metavolume", "Metaballs as Volume", default_value=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "metavolume", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.IntParmTemplate("vm_coving", "Coving", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["Disable Coving","Coving for displacement/sub-d","Coving for all primitives"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "coving", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("vm_materialoverride", "Material Override", 1, default_value=(["compact"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["none","full","compact"]), menu_labels=(["Disabled","Evaluate for Each Primitve/Point","Evaluate Once"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template.setTags({"spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_overridedetail", "Ignore Geometry Attribute Shaders", default_value=False)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "overridedetail", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("vm_procuseroottransform", "Proc Use Root Transform", default_value=True)
hou_parm_template.setTags({"mantra_class": "object", "mantra_name": "procuseroottransform", "spare_category": "Geometry"})
# Code for parameter template
hou_parm_template = hou.FolderSetParmTemplate("parent_3", folder_names=(["Misc"]), folder_type=hou.folderType.Tabs)
# Code for parameter template
hou_parm_template = hou.FolderSetParmTemplate("trcCTRLs", folder_names=(["Trace Controls"]), folder_type=hou.folderType.Simple)
hou_parm_template.setTags({"group_type": "simple"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("file", "File", 1, default_value=(["$JOB/test2.psd"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.FileReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
hou_parm_template.setJoinWithNext(True)
hou_parm_template.setTags({"autoscope": "0000000000000000", "filechooser_pattern": "*.psd"})
# Code for parameter template
hou_parm_template = hou.ButtonParmTemplate("reload", "Reload PSD")
hou_parm_template.setTags({"autoscope": "0000000000000000"})
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("layer_name1", "Layer Name", 1, default_value=(["LWR_RCVR"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="opmenu -l -a trace_psd_file1 layer_name1", item_generator_script_language=hou.scriptLanguage.Hscript, menu_type=hou.menuType.StringReplace)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("thresh1", "Brightness Threshold", 1, default_value=([0.139]), min=0, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setTags({"autoscope": "0000000000000000"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("step1", "Resample Step", 1, default_value=([0.52]), min=0.001, max=10, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setTags({"autoscope": "0000000000000000"})
# Code for parameter template
hou_parm_template = hou.FolderSetParmTemplate("genShpCTRLs", folder_names=(["General Shape Controls"]), folder_type=hou.folderType.Simple)
hou_parm_template.setTags({"group_type": "simple"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("prntThickness", "ParentThickness", 1, default_value=([0.012]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.MenuParmTemplate("shpSwitch", "Shape Switch", menu_items=(["0","1"]), menu_labels=(["Cylindrical","Flat"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.IntParmTemplate("leftRight", "LEFT/RIGHT", 1, default_value=([0]), min=0, max=1, min_is_strict=True, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("mirrored", "Mirrored", default_value=True)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FolderSetParmTemplate("cylCTRLs", folder_names=(["Cylindrical Controls"]), folder_type=hou.folderType.Simple)
hou_parm_template.setTags({"group_type": "simple"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("scale2", "Scale", 3, default_value=([1, 1, 1]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("scale2", "Scale", 3, default_value=([1, 1, 1]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("scale2", "Scale", 3, default_value=([1, 1, 1]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.IntParmTemplate("sides", "Sides", 1, default_value=([12]), min=1, max=50, min_is_strict=True, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("WallThickness", "Wall Thickness", 1, default_value=([0]), min=-0.2, max=0.2, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("cylThickness", "Cylindrical Thickness", 1, default_value=([0]), min=-10, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FolderSetParmTemplate("flatCTRLs", folder_names=(["Flat Controls"]), folder_type=hou.folderType.Simple)
hou_parm_template.setTags({"group_type": "simple"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("zThickness", "Z-Thickness", 1, default_value=([0.012]), min=0, max=0.05, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FolderSetParmTemplate("bvlCTRLs", folder_names=(["Bevel Controls"]), folder_type=hou.folderType.Simple)
hou_parm_template.setTags({"group_type": "simple"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("bvlFlatAngle", "Bevel Flat Angle", 1, default_value=([51.8]), min=0, max=180, min_is_strict=True, max_is_strict=True, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("bvlWidth", "Bevel Width", 1, default_value=([0.002]), min=0, max=0.01, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.setScriptCallbackLanguage(hou.scriptLanguage.Python)
hou_parm_template.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
