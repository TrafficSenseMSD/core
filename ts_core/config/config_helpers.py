import re
import ts_core.config.bindings.sumocfg as sumocfg
from ts_core.config.config_exceptions import *
import ts_core.config.bindings.nodes_xml as nodes
from xml.dom import minidom
import numpy as np


def _sind(x, places):
    return round(np.sin( x * np.pi / 180), places)


def _cosd(x, places):
    return round(np.cos(x * np.pi / 180), places)


def mk_node(intersections: dict, branches: dict):
    """
    
    Let's do an example...
    
    
    Parameters
    ----------
    intersections
    branches

    Returns
    -------

    """
    n = nodes.nodes()

    _branch_validation = [
        'id',
        'type',
        'theta',
        'Length',
    ]

    _intersection_validation = [
        'id',
        'type'
    ]

    branch_metadata = {}

    # Iterate intersections
    # NOTE: Will only generate the intersection with id == 0 until multiple intersection
    # support is added.
    for inter in intersections:
        if not all(field in intersections[inter] for field in _intersection_validation):
            raise ParsedSchemaError("All of the fields in the list {} must be in each branch".format(
                str(_branch_validation))
            )
        if intersections[inter]['id'] != 0:
            continue

        n.append(nodes.nodeType(id=intersections[inter]['id'], x=0, y=0, type=intersections[inter]['type']))

    for branch in branches:
        # Make sure each branch has all the keys that are about to be called
        if not all(field in branches[branch] for field in _branch_validation):
            raise ParsedSchemaError("All of the fields in the list {} must be in each branch".format(str(_branch_validation)))

        # branch_metadata[branches[branch]['id']] = {}


        # print(branches[branch]['id'])
        # if branches[branch]['id'] == 1:
        #     pass
        n.append(nodes.nodeType(id=branches[branch]['id'],
                                x=branches[branch]['Length']*_cosd(branches[branch]['theta'], 2),
                                y=branches[branch]['Length']*_sind(branches[branch]['theta'], 2),
                                type=branches[branch]['type']))
    #

    xmlstr = minidom.parseString(n.toxml("utf-8").decode('utf-8')).toprettyxml(indent="   ")

    return xmlstr

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

    xmlstr = minidom.parseString(cfg.toxml("utf-8").decode('utf-8')).toprettyxml(indent="   ")
    return xmlstr


