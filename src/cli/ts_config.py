import argparse
from shutil import copyfile

import os

DEBUG = False

SUMO_DIRECTORY = "Fakepath"
DEFAULT_NODE_FILE = "defaultnodes.xml"
DEFAULT_EDGE_FILE = "defaultedges.xml"
NODE_FILE_LOCATION = SUMO_DIRECTORY + "/node.nod.xml"
EDGE_FILE_LOCATION = SUMO_DIRECTORY + "/edge.edg.xml"


def move_file(original_filename, new_filename):
    """

    :param original_filename:
    :param new_filename:
    :return:
    """
    copyfile(original_filename, new_filename)


def main(args):
    """
    Main function that parses the arguments and
    will (call functions that )creates all of the required files

    Parameters:
        args : ArgParse object with all the requirements
    Returns: None
    """
    if args.intersection:
        if DEBUG: print("intersection %s " % args.intersection)
        file_list = args.intersection.split(",")
        if not os.path.exists("SUMO_DIRECTORY"):
            print('SUMO Directory does not exist. Please run "--init"')
            return
        if args.intersection == "default":
            copyfile(DEFAULT_NODE_FILE, NODE_FILE_LOCATION)
            copyfile(DEFAULT_EDGE_FILE, EDGE_FILE_LOCATION)

        if len(file_list) == 2:
            copyfile(file_list[0], NODE_FILE_LOCATION)
            copyfile(file_list[1], EDGE_FILE_LOCATION)


    if args.driver_behavior:
        if DEBUG: print("driver_behavior %s" % args.driver_behavior)

    if args.vehicle_size_distribution:
        if DEBUG: print("vehicle_size_distribution %s" % args.vehicle_size_distribution)

    if args.traffic_demand:
        if DEBUG: print("traffic_demand %s" % args.traffic_demand)

    if args.accident_behavior:
        if DEBUG: print("accident_behavior %s" % args.accident_behavior)

    if args.v2i_distribution:
        if DEBUG: print("v2i_distribution %s" % args.v2i_distribution)

    if args.optimizer:  # C
        if DEBUG: print("optimizer %s" % args.optimizer)

    if args.route_weights:
        if DEBUG: print("route_weights %s" % args.route_weights)

    if args.initialize_directory:
        if DEBUG: print("initialize_directory %s" % args.initialize_directory)

        if not os.path.exists("SUMO_DIRECTORY"):
            os.makedirs("SUMO_DIRECTORY")

    if args.randomize:
        if DEBUG: print("randomize %s " % args.randomize)

    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--intersection", dest="intersection", help="defines the Intersection to generate")
    parser.add_argument("-d", "--driver_behav", dest="driver_behavior", default="default", help="Specify the driver behavior")
    parser.add_argument("-v", "--vehicle_size", dest="vehicle_size_distribution", default="", help="Vehicle size distribution")
    parser.add_argument("-t", "--traffic_demand", dest="traffic_demand", default="", help="")
    parser.add_argument("-a", "--accident_behavior", dest="accident_behavior", default="", help="")
    parser.add_argument("-v2i", "--v2i_distribution", dest="v2i_distribution", default="", help="")
    parser.add_argument("-o", "--optimizer", dest="optimizer", default="", help="")
    parser.add_argument("-r", "--route_weights", dest="route_weights", default="", help="")
    parser.add_argument("--init", dest="initialize_directory", action='store_true', help="Initializes the directory...")
    parser.add_argument("--randomize", dest="randomize", default=False, help="Makes the configs slightly randomized")
    arguments = parser.parse_args()
    main(arguments)


