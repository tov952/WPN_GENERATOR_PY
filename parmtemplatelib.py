import hou 
def createPTG():
    hou_parm_template_group = hou.ParmTemplateGroup()
    # Code for parameter template
    hou_parm_template = hou.FolderParmTemplate("assetInfo_exclude", "Asset Info", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template.setTags({"group_type": "simple"})
    # Code for parameter template
    hou_parm_template2 = hou.StringParmTemplate("file", "File", 1, default_value=(["$JOB/test2.psd"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.FileReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
    hou_parm_template2.setJoinWithNext(True)
    hou_parm_template2.setTags({"autoscope": "0000000000000000", "filechooser_pattern": "*.psd"})
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.ButtonParmTemplate("reload", "Reload PSD")
    hou_parm_template2.setTags({"autoscope": "0000000000000000"})
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.StringParmTemplate("layer_name1", "Layer Name", 1, default_value=(["LWR_RCVR"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="opmenu -l -a trace_psd_file1 layer_name1", item_generator_script_language=hou.scriptLanguage.Hscript, menu_type=hou.menuType.StringReplace)
    hou_parm_template2.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template2.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template.addParmTemplate(hou_parm_template2)
    hou_parm_template_group.append(hou_parm_template)
    # Code for parameter template
    hou_parm_template = hou.FolderParmTemplate("cutoutName", "Cutout Name", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
    # Code for parameter template
    hou_parm_template2 = hou.FolderParmTemplate("trcCTRLs", "Trace Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template2.setTags({"group_type": "simple"})
    # Code for parameter template
    hou_parm_template3 = hou.FloatParmTemplate("thresh1", "Brightness Threshold", 1, default_value=([0.01]), min=0, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template3.setTags({"autoscope": "0000000000000000"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.FloatParmTemplate("step1", "Resample Step", 1, default_value=([0.52]), min=0.001, max=10, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template3.setTags({"autoscope": "0000000000000000"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.FolderParmTemplate("genShpCTRLs", "General Shape Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template2.setTags({"group_type": "simple"})
    # Code for parameter template
    hou_parm_template3 = hou.FloatParmTemplate("prntThickness", "ParentThickness", 1, default_value=([0.012]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.MenuParmTemplate("shpSwitch", "Shape Switch", menu_items=(["0","1"]), menu_labels=(["Cylindrical","Flat"]), default_value=1, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.IntParmTemplate("leftRight", "LEFT/RIGHT", 1, default_value=([0]), min=0, max=1, min_is_strict=True, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.ToggleParmTemplate("mirrored", "Mirrored", default_value=True)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.FolderParmTemplate("cylCTRLs", "Cylindrical Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ shpSwitch != 0 }")
    hou_parm_template2.setTags({"group_type": "simple"})
    # Code for parameter template
    hou_parm_template3 = hou.FloatParmTemplate("scale2", "Scale", 3, default_value=([1, 1, 1]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.IntParmTemplate("sides", "Sides", 1, default_value=([12]), min=1, max=50, min_is_strict=True, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.FloatParmTemplate("WallThickness", "Wall Thickness", 1, default_value=([0]), min=-0.2, max=0.2, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.FloatParmTemplate("cylThickness", "Cylindrical Thickness", 1, default_value=([0]), min=-10, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.FolderParmTemplate("flatCTRLs", "Flat Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ shpSwitch != 1 }")
    hou_parm_template2.setTags({"group_type": "simple"})
    # Code for parameter template
    hou_parm_template3 = hou.FloatParmTemplate("zThickness", "Z-Thickness", 1, default_value=([0.012]), min=0, max=0.05, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.FolderParmTemplate("bvlCTRLs", "Bevel Controls", folder_type=hou.folderType.Simple, default_value=0, ends_tab_group=False)
    hou_parm_template2.setTags({"group_type": "simple"})
    # Code for parameter template
    hou_parm_template3 = hou.FloatParmTemplate("bvlFlatAngle", "Bevel Flat Angle", 1, default_value=([51.8]), min=0, max=180, min_is_strict=True, max_is_strict=True, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    # Code for parameter template
    hou_parm_template3 = hou.FloatParmTemplate("bvlWidth", "Bevel Width", 1, default_value=([0.002]), min=0, max=0.01, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
    hou_parm_template3.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    hou_parm_template3.setTags({"autoscope": "0000000000000000", "script_callback_language": "python"})
    hou_parm_template2.addParmTemplate(hou_parm_template3)
    hou_parm_template.addParmTemplate(hou_parm_template2)
    hou_parm_template_group.append(hou_parm_template)
    return hou_parm_template_group
    
