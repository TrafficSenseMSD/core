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



overwrite_output_help = \
    """
    Overwrite the output directory.  This will remove all previous runs and regenerate the folder.

    """


def run_loop():
    """execute the TraCI control loop"""
    tick = 0
    from ts_core.optimization.optimizer_example import OptimizerExample
    op = OptimizerExample()
    op.train(tick)
    #traci.trafficlights.setPhase("0", 2)
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        op.train(tick)
        input('Continue?')
        tick += 1
    traci.close()
    sys.stdout.flush()
    
def main():
    """
    
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
    output_dir = args.sumo_config_dir+"/output/"+run_start_dt_str


    """ Output Directory Handling """

    # Wipe out the output directory if instructed by command line argument
    if args.overwrite_output:
        shutil.rmtree(args.sumo_config_dir+"/output")

    # Create the output director if it does not exist
    if not os.path.isdir(args.sumo_config_dir+"/output"):
        os.mkdir(args.sumo_config_dir+"/output")

    # Create the directory for this run's output
    os.mkdir(output_dir)

    # Checking the binary for both the GUI and non-gui alternatives
    if args.gui:
        sumoBinary = sumolib.checkBinary('sumo')
    else:
        sumoBinary = sumolib.checkBinary('sumo-gui')

    """ SUMO Startup """
    # Start up the SUMO binary as specified by the SUMO_HOME environment variable
    traci.start([sumoBinary, "-c", args.sumo_config_dir+"/cross.sumocfg",
                             "--tripinfo-output", output_dir+"/sutripinfo.xml"])

    """ Engage the SUMO event loop """
    run_loop()

    return


if __name__ == "__main__":
    main()
