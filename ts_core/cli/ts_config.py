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
    subparsers = parser.add_subparsers(title="subcommands", help="choose one")

    init = subparsers.add_parser('init', help="", description="")
    init.add_argument("--project_path", action=FullPaths)
    init.set_defaults(which='init')

    build = subparsers.add_parser('build', help="", description="")
    build.add_argument("config_file", action=FullPaths)
    build.add_argument("--project_path", action=FullPaths)
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
        parsed_excel = parser.run_parser(args.config_file, args.project_path)
        transform_parsed_excel(parsed_excel)
    elif args.which == 'init':
        pass
    else:
        raise ValueError("Invalid subcommand somehow passed Argparse, please try again.")

    # if args.intersection:
    #     if DEBUG: print("intersection %s " % args.intersection)
    #     file_list = args.intersection.split(",")
    #     if not os.path.exists("SUMO_DIRECTORY"):
    #         print('SUMO Directory does not exist. Please run "--init"')
    #         return
    #     if args.intersection == "default":
    #         copyfile(DEFAULT_NODE_FILE, NODE_FILE_LOCATION)
    #         copyfile(DEFAULT_EDGE_FILE, EDGE_FILE_LOCATION)
    #
    #     if len(file_list) == 2:
    #         copyfile(file_list[0], NODE_FILE_LOCATION)
    #         copyfile(file_list[1], EDGE_FILE_LOCATION)

    # parser.run_parser()

    # if args.driver_behavior:
    #     if DEBUG: print("driver_behavior %s" % args.driver_behavior)
    #
    # if args.vehicle_size_distribution:
    #     if DEBUG: print("vehicle_size_distribution %s" % args.vehicle_size_distribution)
    #
    # if args.traffic_demand:
    #     if DEBUG: print("traffic_demand %s" % args.traffic_demand)
    #
    # if args.accident_behavior:
    #     if DEBUG: print("accident_behavior %s" % args.accident_behavior)
    #
    # if args.v2i_distribution:
    #     if DEBUG: print("v2i_distribution %s" % args.v2i_distribution)
    #
    # if args.optimizer:  # C
    #     if DEBUG: print("optimizer %s" % args.optimizer)
    #
    # if args.route_weights:
    #     if DEBUG: print("route_weights %s" % args.route_weights)
    #
    # if args.initialize_directory:
    #     if DEBUG: print("initialize_directory %s" % args.initialize_directory)
    #
    #     if not os.path.exists("SUMO_DIRECTORY"):
    #         os.makedirs("SUMO_DIRECTORY")
    #
    # if args.randomize:
    #     if DEBUG: print("randomize %s " % args.randomize)
    #
    # return
    #

