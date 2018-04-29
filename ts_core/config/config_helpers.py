"""
This module contains a series of functions that transform the parsed excel document into SUMO conpatible XML. 



"""
import re
import ts_core.config.bindings.sumocfg as sumocfg
from ts_core.config.config_exceptions import *
import ts_core.config.bindings.nodes_xml as nodes
import ts_core.config.bindings.edges_xml as edges
import ts_core.config.bindings.additional_xml as additional
from xml.dom import minidom
import numpy as np
from pyxb import BIND

_lanes_fields = [
    'L_lanes',
    'R_lanes',
    'S_lanes',
    'RS_lanes',
    'LS_lanes'
]



def _sind(x, places):
    return round(np.sin( x * np.pi / 180), places)


def _cosd(x, places):
    """
    Helper function for doing degree 
    Parameters
    ----------
    x
    places

    Returns
    -------

    """
    return round(np.cos(x * np.pi / 180), places)


def mk_add(intersections: dict, branches: dict):
    """
    Generate the additional attributes XML file. 
    
    This file handles, among other things, traffic detectors. 
    
    Lane Area Detectors
    -------------------
    
    So far the only implemented option is a set of lane area detectors on
    all lanes for each branch. For each branch the start and end points of the detector
    are defined in the Excel configuration as the distance from the intersection. 
    
    
    Parameters
    ----------
    intersections
    branches

    Returns
    -------

    """

    _branch_validation = [
        'id',
        'L_lanes',
        'R_lanes',
        'S_lanes',
        'RS_lanes',
        'LS_lanes',
        'priority',
        'sensor_start',
        'sensor_end'
    ]

    ad1 = additional.additionalType()

    for branch in branches:
        numlanes = sum([branches[branch][l] for l in _lanes_fields])
        if not all(field in branches[branch] for field in _branch_validation):
            raise ParsedSchemaError("All of the fields in the list {} must be in each branch".format(str(_branch_validation)))

        for lane in range(numlanes):
            tmp = additional.e2DetectorType(
                id="Area" + str(branches[branch]['id']) + "i" + "_" + str(lane),
                lane=str(branches[branch]['id']) + "i" + "_" + str(lane),
                pos=str(-branches[branch]['sensor_end']),
                endPos=str(-branches[branch]['sensor_start']),
                freq="10",
                file="test_area.xml"
            )
            ad1.laneAreaDetector.append(tmp)

    xmlstr = minidom.parseString(ad1.toxml("utf-8", element_name='additional').decode('utf-8')).toprettyxml(indent="   ")
    return xmlstr

def mk_edge(intersections: dict, branches: dict):

    edge = edges.edges()


    _branch_validation = [
        'id',
        'L_lanes',
        'R_lanes',
        'S_lanes',
        'RS_lanes',
        'LS_lanes',
        'priority'
    ]

    for branch in branches:
        numlanes = sum([branches[branch][l] for l in _lanes_fields])

        # Make sure each branch has all the keys that are about to be called
        if not all(field in branches[branch] for field in _branch_validation):
            raise ParsedSchemaError("All of the fields in the list {} must be in each branch".format(str(_branch_validation)))


        inbound_edge = edges.edgeType(
            id=str(branches[branch]['id'])+"i",
            priority=branches[branch]['priority'],
            from_=str(branches[branch]['id']),
            to=0,
            numLanes=numlanes,
            speed=str(branches[branch]['speed'])
        )

        outbound_edge = edges.edgeType(
            id=str(branches[branch]['id'])+"o",
            priority=branches[branch]['priority'],
            to=str(branches[branch]['id']),
            from_=0,
            numLanes=numlanes,
            speed=str(branches[branch]['speed'])
        )
        edge.append(inbound_edge)
        edge.append(outbound_edge)

    xmlstr = minidom.parseString(edge.toxml("utf-8").decode('utf-8')).toprettyxml(indent="   ")
    return xmlstr


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


        try:
            n.append(nodes.nodeType(id=branches[branch]['id'],
                                x=branches[branch]['Length']*_cosd(branches[branch]['theta'], 2),
                                y=branches[branch]['Length']*_sind(branches[branch]['theta'], 2),
                                type=str.lower(branches[branch]['type'])))
        except Exception as e:
            print(branches[branch])
            print(e)

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

    for tag in _implemented:
        try:
            parsed_data[tag]
        except KeyError:
            continue

        _input = getattr(sumocfg, tag+'Type')()
        for attr, value in parsed_data[tag].items():
            attr_type = _input.__getattribute__("_"+tag+"Type__"+attr).__dict__['_ElementDeclaration__elementBinding']
            _input.__setattr__(attr, attr_type(value_=value))
        cfg.append(_input)


    xmlstr = minidom.parseString(cfg.toxml("utf-8").decode('utf-8')).toprettyxml(indent="   ")
    return xmlstr


