"""
``ts_runner`` is a WORK IN PROGRESS, current objective is to implement the traci_tls tutorial using our abstraction.

.. _ts_runner:


``ts_runner`` Overview
----------------------
``ts_runner`` manages the startup and execution of the SUMO runtime along with traffic light control and data collectio


Software Structure and Implementation
-------------------------------------

Light Control and Optimization
------------------------------
``ts_runner`` will accept an argument that specifies the file and class name to import at startup.  Messing with this
part of Python is tricky business.  

PaseBin:

    import importlib
    import sys
    
    def modify_and_import(module_name, package=None, modification_func):
        spec = importlib.util.find_spec(module_name, package)
        source = spec.loader.get_source(module_name)
        new_source = modification_func(source)
        module = importlib.util.module_from_spec(spec)
        codeobj = compile(new_source, module.__spec__.origin, 'exec')
        exec(codeobj, module.__dict__)
        sys.modules[module_name] = module
        return module


Output
------

Output from ts_runner is directed to ``<sumo_project_dir>/output/<YYYY_MM_DD_HH_MM_SS_dddddd>/'' which
contains:
    ``sutripinfo.xml``
    ``YYYY_MM_DD_HH_MM_SS_dddddd_ts_runner.log`` (Not yet implemented, writes to current dir)



"""

import argparse
from argparse import RawTextHelpFormatter
from ts_core.utils.argparse_utils import FullPaths, is_dir, is_file
from ts_core.execution.traci_loop import run_loop
from ts_core.utils.ts_logging import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

import sys
import time
import re
import datetime as dt
import os, shutil
import random
import traci
import sumolib

from six import string_types, integer_types

overwrite_output_help = \
    """
    Overwrite the output directory.  This will remove all previous runs and regenerate the folder.

    """


def run_loop():
    """execute the TraCI control loop"""
    tick = 0
    # from ts_core.optimization.optimizer_example import OptimizerExample
    # op = OptimizerExample()
    # op.train(tick)
    #traci.trafficlights.setPhase("0", 2)
    car_flag = False
    while traci.simulation.getMinExpectedNumber() > 1 or not car_flag:
        traci.simulationStep()
        if traci.simulation.getMinExpectedNumber() > 5:
            car_flag = True
        # op.train(tick)
        tick += 1
    traci.close()
    sys.stdout.flush()
    print()
    print("Simulation Took %s ticks" % tick)


def make_phase(light_array, default_time, min_time=None, max_time=None):
    """

    Parameters
    ----------
    light_array: String containing the light pattern for this phase  (i.e "GGrrGGrr)
    default_time: Number of ticks that this phase should be active
    min_time: Minimum number of ticks that this phase should be active
    max_time: maximum number of ticks that this phase should be active

    Returns
    -------
    Traci phase object with specified data
    """
    mult = 1000  # Multiplier (units are in mili ticks??) TODO Understand this
    if min_time is None or min_time > default_time:
        min_time = default_time
    if max_time is None or max_time < default_time:
        max_time = default_time
    return traci.trafficlight.Phase(default_time*mult, min_time*mult, max_time*mult, light_array)


def make_and_set_program(program_name, phases, starting_phase=0, tl_type=0, traffic_light_ids=()):
    """

    Parameters
    ----------
    program_name: Name for this program. Use this when setting the programs
    phases: List/tuple of Traci phase objects demoting the various phases for this program
    starting_phase: Integer: When this program is set, this phase ID will be active first
    tl_type: ---DOES NOT WORK. ALWAYS STATIC--- 0: static, 1: delay_based, 2: actuated

    traffic_light_ids: ID of Traffic lights to set to this program. If empty, does not set any traffic lights
            Accepts String, integer, or list (of mixed strings or integers)

    Returns
    -------
    Traci Program object
    """
    new_program = traci.trafficlight.Logic(program_name, tl_type, 0, starting_phase, phases)
    if traffic_light_ids != ():
        if isinstance(traffic_light_ids, string_types):     # If given as a single string
            traffic_light_ids = [traffic_light_ids]
        elif isinstance(traffic_light_ids, integer_types):  # IF given as a single integer
            traffic_light_ids = [traffic_light_ids]

        for light_id in traffic_light_ids:
            traci.trafficlight.setCompleteRedYellowGreenDefinition(str(light_id), new_program)

    return new_program


def main():
    """
    Initializes sumo to run using given files

    Returns
    -------

    """
    # Initialize argument parser and declare arguments.
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, description=main.__doc__)

    """ Argument Definitions """
    parser.add_argument('sumo_config_dir', action=FullPaths, type=is_dir,
                        help='Specify the target directory from which to load config files')

    parser.add_argument('--gui', action='store_false', help='Toggle the use of the SUMO GUI')

    parser.add_argument('--overwrite_output', action='store_true', help=overwrite_output_help)

    args = parser.parse_args()

    # A handy variable with the datetime object at the time when the run started
    run_start_dt = dt.datetime.now()
    run_start_dt_str = re.sub('[^A-Za-z0-9]+', '_', run_start_dt.isoformat())
    output_dir = args.sumo_config_dir + "/output/" + run_start_dt_str

    """ Output Directory Handling """

    # Wipe out the output directory if instructed by command line argument
    if args.overwrite_output:
        shutil.rmtree(args.sumo_config_dir + "/output", ignore_errors=True)  # Dont crash if there is no directory

    # Create the output director if it does not exist
    if not os.path.isdir(args.sumo_config_dir + "/output"):
        os.mkdir(args.sumo_config_dir + "/output")

    # Create the directory for this run's output
    os.mkdir(output_dir)

    # Checking the binary for both the GUI and non-gui alternatives
    if args.gui:
        sumoBinary = sumolib.checkBinary('sumo')
    else:
        sumoBinary = sumolib.checkBinary('sumo-gui')

    for file in os.listdir(args.sumo_config_dir):
        if file.lower().endswith(".sumocfg"):
            sumo_cfg_file = file
            # sumo_cfg_name = file.split('.')[0]
            # print("Configuration name: %s" % sumo_cfg_name)
            # print("Found .sumocfg file: %s" % file)
            break
    else:
        print("No .sumocfg file found in %s" % args.sumo_config_dir)
        print("***EXITING***")
        return

    """ SUMO Startup """
    # Start up the SUMO binary as specified by the SUMO_HOME environment variable
    traci.start([sumoBinary, "-c", args.sumo_config_dir + '/' + sumo_cfg_file,
                 "--tripinfo-output", output_dir + "/sutripinfo.xml"])
    
    """ Engage the SUMO event loop """
    run_loop()

    return


if __name__ == "__main__":
    main()
