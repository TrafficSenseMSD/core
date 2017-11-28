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

def generate_routefile(ts_sumo_dir):
    random.seed(42)  # make tests reproducible
    N = 3600  # number of time steps
    # demand per second from different directions
    pWE = 1. / 10
    pEW = 1. / 11
    pNS = 1. / 30
    with open(ts_sumo_dir+"/data/cross.rou.xml", "w") as routes:
        print("""<routes>
        <vType id="typeWE" accel="0.8" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="16.67" guiShape="passenger"/>
        <vType id="typeNS" accel="0.8" decel="4.5" sigma="0.5" length="7" minGap="3" maxSpeed="25" guiShape="bus"/>

        <route id="right" edges="51o 1i 2o 52i" />
        <route id="left" edges="52o 2i 1o 51i" />
        <route id="down" edges="54o 4i 3o 53i" />""", file=routes)
        lastVeh = 0
        vehNr = 0
        for i in range(N):
            if random.uniform(0, 1) < pWE:
                print('    <vehicle id="right_%i" type="typeWE" route="right" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1
                lastVeh = i
            if random.uniform(0, 1) < pEW:
                print('    <vehicle id="left_%i" type="typeWE" route="left" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1
                lastVeh = i
            if random.uniform(0, 1) < pNS:
                print('    <vehicle id="down_%i" type="typeNS" route="down" depart="%i" color="1,0,0"/>' % (
                    vehNr, i), file=routes)
                vehNr += 1
                lastVeh = i
        print("</routes>", file=routes)

overwrite_output_help = \
    """
    Overwrite the output directory.  This will remove all previous runs and regenerate the folder.

    """


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

    generate_routefile(args.sumo_config_dir)

    """ SUMO Startup """
    # Start up the SUMO binary as specified by the SUMO_HOME environment variable
    traci.start([sumoBinary, "-c", args.sumo_config_dir+"/data/cross.sumocfg",
                             "--tripinfo-output", output_dir+"/sutripinfo.xml"])

    """ Engage the SUMO event loop """
    run_loop()

    return


if __name__ == "__main__":
    main()
