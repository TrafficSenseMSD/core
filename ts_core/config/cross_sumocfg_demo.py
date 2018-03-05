import ts_core.config.bindings.sumocfg as sumocfg


cfg = sumocfg.configuration()

# Working with the inputs block
input_ = sumocfg.inputType()
input_.__setattr__("net_file", sumocfg.fileOptionType(value_="cross.net.xml"))
input_.__setattr__("route_files", sumocfg.fileOptionType(value_="cross5.rou.xml"))
cfg.append(input_)

# Working with the time block
time_ = sumocfg.timeType()
#time_.__setattr__("begin", sumocfg.timeOptionType(value_=0))
#time_.__setattr__("end", sumocfg.timeOptionType(value_=20000))
#time_.__setattr__("end", 20000)


#print(time_)
cfg.append(time_)


import pprint
pprint.pprint(input_.__getattribute__("_inputType__load_state").__dict__)
pprint.pprint(sumocfg.inputType.__dict__)
#pprint.pprint(sumocfg.configurationType.__dict__['_ElementMap'])
#pprint.pprint(dir(getattr(sumocfg, 'timeType').__dict__['begin']))


# gui_only params
# gui_ = sumocfg.gui_onlyType()
# gui_.__setattr__("gui_settings_file", sumocfg.fileOptionType(value_="cross.settings.xml"))
# cfg.append(gui_)

output_ = sumocfg.outputType()


#output_.__setattr__("vehroute_output_write_unfinished", True)
cfg.append(output_)

from xml.dom import minidom

xmlstr = minidom.parseString(cfg.toxml("utf-8").decode('utf-8')).toprettyxml(indent="   ")
print(xmlstr)

