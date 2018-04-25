import jsmin
import json
import pyxb
import os
import warnings

import subprocess
import sumolib
pyxb._CorruptionDetectionEnabled = False
from ts_core.config.config_helpers import *
from ts_core.config.config_exceptions import *
from ts_core.utils.ts_logging import setup_logging
import logging

setup_logging()

logger = logging.getLogger()


def transform_parsed_excel(parsed, project_path, stats_file, config_name):
    """
    This is the manager function transforming
    
    There is a lot more to talk about but right now I have other things to do. 
    
    Parameters
    ----------
    parsed

    Returns
    -------
    None
    
    """
    if "SUMOCFG" not in parsed:
        raise ParsedSchemaError("Key 'SUMOCFG' is not in top level dict")


    # Generate each of the files from the parsed config sheet

    sumocfg_xml = mk_sumocfg(parsed["SUMOCFG"])
    node_xml = mk_node(parsed['Intersections'], parsed['Branches'])
    edge_xml = mk_edge(parsed['Intersections'], parsed['Branches'])
    additional_xml = mk_add(parsed['Intersections'], parsed['Branches'])

    # Write SUMO config XML

    sumocfg_file_path = project_path+ "/" + config_name + ".sumocfg"
    logger.info("Writing SUMO Config File to {}".format(sumocfg_file_path))
    with open(sumocfg_file_path                              , "w") as cfg_file:
        cfg_file.write(sumocfg_xml)

    # White nodes XML
    node_file_path = project_path + "/" + config_name + ".nod.xml"
    logger.info("Writing Node File to {}".format(node_file_path))
    with open(node_file_path, "w") as cfg_file:
        cfg_file.writelines(node_xml)

    # Write edges XML
    edge_file_path = project_path + "/" + config_name + ".edg.xml"
    logger.info("Writing Edge File to {}".format(edge_file_path))
    with open(edge_file_path, "w") as cfg_file:
        cfg_file.writelines(edge_xml)

    # Write stats XML
    stat_file_path = project_path + "/" + config_name + ".stat.xml"
    logger.info("Writing Stats File to {}".format(stat_file_path))
    with open(stat_file_path, "w") as cfg_file:
        cfg_file.writelines(stats_file)

    # Write additional XML
    additional_file_path = project_path + "/" + config_name + ".add.xml"
    logger.info("Writing Additional XML File to {}".format(additional_file_path))
    with open(additional_file_path, "w") as cfg_file:
        cfg_file.writelines(additional_xml)


    logger.info("******** ASSUMING NETCONVERT, ACTIVITYGEN, DUAROUTER ACCESSIBLE TO SHELL ********")

    # ##### NETCONVERT HANDLING #######

    net_file_path = project_path + "/" + config_name + ".net.xml"
    netconvert = "netconvert --node-files=" + node_file_path + \
                 " --edge-files=" + edge_file_path + \
                 " --output-file=" + net_file_path

    logger.info("EXECUTING NETCONVERT")
    logger.debug("EXECUTING: {}".format(netconvert))


    try:
        completed = subprocess.run(
            netconvert,
            check=True,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError as err:
        print('ERROR:', err)
    else:
        stderr = completed.stderr.decode('utf-8')
        if len(stderr) > 0:
            warnings.warn(stderr)

        if completed.returncode != 0:
            raise RuntimeError("SUMO SUBPROCESS CALLS FAILED! EXIT TO SAFETY")

        logger.info("NETCONVERT Completed Successfully")

    # ##### ACTIVITYGEN HANDLING #######

    activity_trips_file_path = project_path + "/" + config_name + ".trips.rou.xml"

    activitygen = "activitygen --net-file " + net_file_path + \
           " --stat-file " + stat_file_path + \
           " --output-file " + activity_trips_file_path + \
           " --random"

    logger.info("EXECUTING ACTIVITYGEN")
    logger.debug("EXECUTING: {}".format(activitygen))

    try:
        completed = subprocess.run(
            activitygen,
            check=True,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError as err:
        print('ERROR:', err)
    else:
        # print('returncode:', completed.returncode)
        print(completed.stderr.decode('utf-8'))

        stderr = completed.stderr.decode('utf-8')
        if len(stderr) > 0:
            warnings.warn(stderr)

        if completed.returncode != 0:
            raise RuntimeError("SUMO SUBPROCESS CALLS FAILED! EXIT TO SAFETY")

        logger.info("ACTIVITYGEN Completed Successfully")


    # ##### DUAROUTER HANDLING #######

    route_file_path = project_path + "/" + config_name + ".rou.xml"

    duarouter = "duarouter --net-file " + net_file_path + \
        " --route-files " + activity_trips_file_path + \
        " -o " + route_file_path

    logger.info("EXECUTING DUAROUTER")
    logger.debug("EXECUTING: {}".format(activitygen))

    try:
        completed = subprocess.run(
            duarouter,
            check=True,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError as err:
        print('ERROR:', err)
    else:
        # print('returncode:', completed.returncode)
        print(completed.stderr.decode('utf-8'))

        stderr = completed.stderr.decode('utf-8')
        if len(stderr) > 0:
            warnings.warn(stderr)

        if completed.returncode != 0:
            raise RuntimeError("SUMO SUBPROCESS CALLS FAILED! EXIT TO SAFETY")

        logger.info("DUAROUTER Completed Successfully")


    return