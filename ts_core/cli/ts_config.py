"""

.. _ts_config_cli:

``ts_config`` Overview
======================
``ts_config`` manages the build of SUMO configuration files from an Excel sheet. 

The user should understand that, because we have simplified configuration, not all SUMO features are supported 
out of the box. 


"""
import argparse
from shutil import copyfile
from ..excel_parser import parser
from ..config.config_gen import transform_parsed_excel

from ..utils.argparse_utils import FullPaths, is_dir, is_file

import os

DEBUG = False

SUMO_DIRECTORY = "Fakepath"
DEFAULT_NODE_FILE = "defaultnodes.xml"
DEFAULT_EDGE_FILE = "defaultedges.xml"
NODE_FILE_LOCATION = SUMO_DIRECTORY + "/node.nod.xml"
EDGE_FILE_LOCATION = SUMO_DIRECTORY + "/edge.edg.xml"


def move_file(original_filename, new_filename):
    """
    
    Parameters
    ----------
    original_filename
    new_filename

    Returns
    -------

    """
    copyfile(original_filename, new_filename)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--project_path", action=FullPaths)
    subparsers = parser.add_subparsers(title="subcommands", help="choose one")

    # init = subparsers.add_parser('init', help="", description="")
    # init.add_argument("-p", "--project_path", action=FullPaths)
    # init.set_defaults(which='init')

    build = subparsers.add_parser('build', help="subcommand to build the configuration", description="Run the configuration build.")
    build.add_argument("-c", "--config", action=FullPaths)#, action=FullPaths)

    build.set_defaults(which='build')

    parser.add_argument("--init", dest="initialize_directory", action='store_true', help="Initializes the directory...")
    # parser.add_argument("--randomize", dest="randomize", default=False, help="Makes the configs slightly randomized")
    arguments = parser.parse_args()
    return arguments



def main():
    """
    Main function that parses the arguments and
    will (call functions that )creates all of the required files

    Parameters
    ----------
    args - ArgParse object with all the requirements

    Returns
    -------
    Nothing
    """
    args = parse_args()

    if args.which == 'build':
        conf_file_path = args.project_path + "/" + args.config_file
        config_name, parsed_excel, stats_xml = parser.run_parser(conf_file_path, args.project_path)

        transform_parsed_excel(parsed_excel, args.project_path, stats_xml, config_name)

    # elif args.which == 'init':
    #     pass
    else:
        raise ValueError("Invalid subcommand somehow passed Argparse, please try again.")

if __name__ == "__main__":
    main()