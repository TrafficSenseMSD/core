#!/usr/bin/python
from openpyxl import *
import json

SUMO_FILE_COLUMN = 1    # Column A
SUMO_ATTR_COLUMN = 0    # Column B
UNITS_COLUMN = 4        # Column E
VALUE_COLUMN = 5        # Column F for single entry data


MIN_ROW = 3  # Minimum row number where config information CAN be stored
MAX_ROW = 20    # Max row where data is stored TODO update?
MIN_COLUMN = 2

TIME_CONVERT = {"Hours": 60*60, "Days": 60*60*24,
                "Months": 60*60*24*30.41,
                "Years": 60*60*24*30.41*12}  # How many seconds per time unit

# List of file extensions
ROUTE = "rou"
NET = "net"

SUMOFILE = 0
SUMOATTR = 1
USERVAL = 3  # First user_val
VALUNITS = 2

TAB_NAMES = ["Vehicle Type Customization", "General Settings", "Intersection Definition", "Branch Settings"]

OUTPUT_DICT = {
    "SUMOCFG": {},
    "Branches": {},
    "Intersections": {},
}


def parse_general(sheet):

    # Configuration name
    input_config_name = get_input_from_row(sheet, MIN_ROW)     # Configuration Name
    config_name = input_config_name[USERVAL]
    if input_config_name[SUMOFILE] == "SUMOCFG" and input_config_name[SUMOATTR] == "input":
        OUTPUT_DICT["SUMOCFG"]["input"] = {"net_file": "%s.net.xml" % config_name,
                                           "route_file": "%s.rou.xml" % config_name}
    else: print("Config name Error")  # TODO fill out

    # Runtime
    input_runtime_length = get_input_from_row(sheet, MIN_ROW+1)     # Simulation runtime
    sim_seconds = input_runtime_length[USERVAL]*TIME_CONVERT[input_runtime_length[VALUNITS]]   # TODO check if units is in time_convert

    if input_runtime_length[SUMOFILE] == "SUMOCFG" and input_runtime_length[SUMOATTR] == "time.end":
        OUTPUT_DICT["SUMOCFG"]["time"] = {"start": "0", "end": "%d" % sim_seconds}
    else: print("TIME ERROR", input_runtime_length)  # TODO fill out

    # TODO Overall Traffic Demand
    input_traffic_demand = get_input_from_row(sheet, MIN_ROW+2)


def parse_intersection(sheet):
    input_intersection_type = get_input_from_row(sheet, MIN_ROW)     # Intersection type
    intersection_type = input_intersection_type[USERVAL]
    OUTPUT_DICT["Intersections"]["I0"] = {}

    # TODO Add in support for multiple intersections.
    intersection_name = "I%d" % 0
    OUTPUT_DICT["Intersections"][intersection_name]["id"] = 0
    OUTPUT_DICT["Intersections"][intersection_name]["type"] = "traffic_light"

    return intersection_type


def get_input_from_row(sheet, row_num, cols=1):
    """

    Parameters
    ----------
    sheet
    row_num

    Returns
    -------

    """

    output = []
    rows = sheet.iter_rows(min_col=1, min_row=row_num, max_col=VALUE_COLUMN+cols, max_row=row_num)

    for row in rows:
        sumo_file = row[SUMO_FILE_COLUMN].value
        if sumo_file is None: sumo_file = "N/A"
        output.append(sumo_file)

        sumo_attr = row[SUMO_ATTR_COLUMN].value
        if sumo_attr is None: sumo_attr = "N/A"
        output.append(sumo_attr)

        units = row[UNITS_COLUMN].value  # TODO check if user entered units
        if units is None: units = "N/A"
        output.append(units)

        for col in range(VALUE_COLUMN, VALUE_COLUMN+cols):
            user_value = row[col].value
            if user_value is None: user_value = "N/A"
            output.append(user_value)

        return tuple(output)


def parse_branches(sheet, intersection_type):
    num_branches = 4  # TODO check intersection type

    # Initialize the output dictionary
    for branch_num in range(1, num_branches+1):
        b_name = "B%d" % branch_num
        OUTPUT_DICT["Branches"][b_name] = {}

    for row in range(MIN_ROW, MAX_ROW):
        if row_has_data(sheet, row):
            input_data = get_input_from_row(sheet, row, num_branches)
            units = input_data[VALUNITS]
            for branch_num in range(0, num_branches):
                b_name = "B%d" % (branch_num+1)
                user_value = input_data[USERVAL+branch_num]

                # TODO check for units and convert them
                # TODO verify inbound lanes sum up to numLanes

                # write to output
                OUTPUT_DICT["Branches"][b_name][input_data[SUMOATTR]] = user_value


def row_has_data(sheet, row_num):
    rows = sheet.iter_rows(min_col=1, min_row=row_num, max_col=15, max_row=row_num)
    for row in rows:
        sumo_attr = row[SUMO_ATTR_COLUMN].value
        if sumo_attr is None:
            return False
        else:
            return True

    # should not be executed
    print("ERROR - row_has_data() did not find row")
    return False


def main():
    wb = load_workbook(filename='Configuration_template.xlsx', data_only=True)

    parse_general(wb["General Settings"])
    type = parse_intersection(wb["Intersection Settings"])
    # output_dict = parse_vehicles(wb["Vehicle Type Customization"])
    parse_branches(wb["Branch Settings"], type)

    parser_output_file = open("parser_output.txt", "w")
    print(OUTPUT_DICT)
    parser_output_file.write(json.dumps(OUTPUT_DICT))


if __name__ == "__main__":
    main()


def parse_vehicles(sheet):
    """

    Parameters
    ----------
    sheet - The vehicle definition sheet

    Returns
    -------
    dct: Dictionary containing all attributes for each Vehicle class
    """

    sheet_name = "Vehicle Type Customization"  # TODO Get from sheet parameter?

    vType_to_attr = {"Cars": "car", "Semi Trucks": "large vehicle???"}
    vehicle_type_info = {}  # {"car": [(accel, ROUTE, attr1), (decel, ROUTE, attr1, attr2...)]
    dct = {}

    # Initialize all vehicle classes that will be created
    for col in sheet.iter_cols(max_col=1):    # Go through all rows of Column A
        for vClass_col in col:
            if vClass_col.row >= MIN_ROW:    # Only look at usable columns
                col_value = vClass_col.value
                if col_value is not None:  # Check for value
                    # Check to see if it is a recognized vehicle class
                    if col_value in vType_to_attr.keys():
                        vehicle_type_info[col_value] = [vClass_col.row]
                    else:
                        print('Unknown Vehicle class: "%s"'
                              ' in entry "%s"'
                              ' in worksheet "%s"' % (col_value, vClass_col.coordinate, sheet_name))

    # Get all user inputs for each vehicle type
    for vClass in vehicle_type_info.keys():
        vClass_row_start = vehicle_type_info[vClass][0]
        for col in sheet.get_squared_range(min_col=2, min_row=vClass_row_start, max_col=8, max_row=vClass_row_start):
            for row in col:
                print(row.value)
    t = get_input_from_row(sheet, 7)
    return dct














































