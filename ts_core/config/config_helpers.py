import jsmin
import json
import re
import pprint
import ts_core.config.bindings.sumocfg as sumocfg
from ts_core.config.config_exceptions import *


def mk_sumocfg(parsed_data: dict):
    """
    Helper function to process the SUMOCFG key of the parsed Excel config file
    into XML. 
    
    Parameters
    ----------
    parsed_data : dictionary
        The "SUMOCFG" key of the parsed Excel file.

    Returns
    -------

    """

    underscore = re.compile(r'_')
    cfg = sumocfg.configuration()
    _implemented = {'input', 'time', 'gui_only'}

    # Identify if any of the params passed are not implemented
    # by this function.
    _not_implemented = set(parsed_data.keys()) - _implemented

    if len(_not_implemented) > 0:
        raise  ParsedConfigNotImplementedError

    if "input" in parsed_data:
        _input = getattr(sumocfg, 'inputType')()
        for attr, value in parsed_data['input'].items():
            attr_type = _input.__getattribute__("_inputType__"+attr).__dict__['_ElementDeclaration__elementBinding']
            _input.__setattr__(attr, attr_type(value_=value))
        cfg.append(_input)

    # Working with the
    if "time" in parsed_data:
        _time = getattr(sumocfg, 'timeType')()
        for attr, value in parsed_data['time'].items():
            attr_type = _time.__getattribute__("_timeType__"+attr).__dict__['_ElementDeclaration__elementBinding']
            _time.__setattr__(attr, attr_type(value_=value))
        cfg.append(_time)

    if "gui_only" in parsed_data:
        _gui = getattr(sumocfg, 'gui_onlyType')()
        for attr, value in parsed_data['gui_only'].items():
            # Some wizardry to find the right option type
            attr_type = _gui.__getattribute__("_gui_onlyType__"+attr).__dict__['_ElementDeclaration__elementBinding']
            # Setting the tag and attributes correctly.
            _gui.__setattr__(attr, attr_type(value_=value))

        cfg.append(_gui)

    from xml.dom import minidom
    xmlstr = minidom.parseString(cfg.toxml("utf-8").decode('utf-8')).toprettyxml(indent="   ")
    print(xmlstr)



