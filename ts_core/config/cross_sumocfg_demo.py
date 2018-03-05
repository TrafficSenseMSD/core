import ts_core.config.bindings.sumocfg as sumocfg


cfg = sumocfg.configuration()

# Working with the inputs block
input_ = sumocfg.inputType()
input_.__setattr__("net_file", sumocfg.fileOptionType(value_="cross.net.xml"))
input_.__setattr__("route_files", sumocfg.fileOptionType(value_="cross5.rou.xml"))
cfg.append(input_)

# Working with the time block
time_ = sumocfg.timeType()
time_.__setattr__("begin", sumocfg.timeOptionType(value_=0))
time_.__setattr__("end", sumocfg.timeOptionType(value_=20000))
cfg.append(time_)


# gui_only params
gui_ = sumocfg.gui_onlyType()
gui_.__setattr__("gui_settings_file", sumocfg.fileOptionType(value_="cross.settings.xml"))
cfg.append(gui_)

output_ = sumocfg.outputType()
#print(getattr(getattr(sumocfg, 'outputType'), 'vehroute_output_write_unfinished'))

#output_.__setattr__("vehroute_output_write_unfinished", True)
cfg.append(output_)

from xml.dom import minidom

xmlstr = minidom.parseString(cfg.toxml("utf-8").decode('utf-8')).toprettyxml(indent="   ")
print(xmlstr)

