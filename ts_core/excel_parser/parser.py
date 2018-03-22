from openpyxl import *
import json

SUMO_ATTR_COLUMN = 0    # Column A
SUMO_FILE_COLUMN = 1    # Column B
CATEGORY_COLUMN = 2
UNITS_COLUMN = 4        # Column E
VALUE_COLUMN = 5        # Column F for single entry data

MIN_ROW = 3  # Minimum row number where config information CAN be stored
MAX_ROW = 20    # Max row where data is stored TODO update?
MIN_COLUMN = 2

UNIT_CONVERT = {
    "time": {"Hours": 60*60, "Days": 60*60*24,
                "Months": 60*60*24*30.41,
                "Years": 60*60*24*30.41*12},  # How many seconds per time unit

    "angle": {"N": 90, "NE": 45, "E": 0, "SE": 315,
              "S": 270, "SW": 225, "W": 180, "NW": 135, },

}
# List of file extensions
ROUTE = "rou"
NET = "net"

SUMOFILE = 0
SUMOATTR = 1
USERVAL = 3  # First user_val
VALUNITS = 2

TAB_NAMES = ["Vehicle Type Customization", "General Settings", "Intersection Definition", "Branch Settings"]

ITYPE_BRANCHES = {
    "Cross": 4,
    "T": 3,
    "Y": 3,
}

OUTPUT_DICT = {
    "SUMOCFG": {},
    "Branches": {},
    "Intersections": {},
}


def parse_general(sheet):
    """
    Parses the General Settings Tab

    Fills out OUTPUT_DICT
    :param sheet: openpyxl sheet - The General Settings tab
    :return: None
    """
    # Get the Configuration name.
    input_config_name = get_input_from_row(sheet, MIN_ROW)     # Configuration Name
    # Write Config names to the output dict
    if input_config_name[SUMOFILE] == "SUMOCFG" and input_config_name[SUMOATTR] == "input":
        config_name = input_config_name[USERVAL]
        OUTPUT_DICT["SUMOCFG"]["input"] = {"net_file": "%s.net.xml" % config_name,
                                           "route_files": "%s.rou.xml" % config_name}
    else:
        print("Config name Error")  # TODO fill out

    # Simulation length
    input_runtime_length = get_input_from_row(sheet, MIN_ROW+1)

    if input_runtime_length[SUMOFILE] == "SUMOCFG" and input_runtime_length[SUMOATTR] == "time.end":
        sim_seconds = input_runtime_length[USERVAL] * UNIT_CONVERT["time"][
            input_runtime_length[VALUNITS]]  # TODO check if units is in time_convert?
        OUTPUT_DICT["SUMOCFG"]["time"] = {"begin": "0", "end": "%d" % sim_seconds}
    else:
        print("TIME ERROR", input_runtime_length)  # TODO fill out

    # Overall Traffic Demand
    # TODO Where does this go in the xmls if anywhere?
    input_traffic_demand = get_input_from_row(sheet, MIN_ROW+2)


def parse_intersection(sheet):
    """
    Parse the Intersection Tab

    :param sheet: openpyxl sheet - The General Intersection Settings tab
    :return: String - The selected intersection type. Key in ITYPE_BRANCHES

    """
    # Intersection type (Cross, T, Y, etc)
    input_intersection_type = get_input_from_row(sheet, MIN_ROW)
    intersection_type = input_intersection_type[USERVAL]
    if intersection_type not in ITYPE_BRANCHES.keys():
        print("Unrecognized Intersection type: %s" % intersection_type)
        return None
    OUTPUT_DICT["Intersections"]["I0"] = {}

    # TODO Add in support for multiple intersections.
    # Initialize the intersection in The output Dict
    intersection_name = "I%d" % 0
    OUTPUT_DICT["Intersections"][intersection_name]["id"] = 0
    OUTPUT_DICT["Intersections"][intersection_name]["type"] = "traffic_light"

    return intersection_type


def parse_branches(sheet, intersection_type):
    """
    Parse the Branch Settings tab

    Fills out OUTPUT_DICT with all information needed to parse the branches of the intersection.
    :param sheet:
    :param intersection_type: The intersection Type (Cross, T, Y, etc. Needs to be a key in ITYPE_BRANCHES
    :return: None
    """
    # Get the number of branches
    num_branches = ITYPE_BRANCHES[intersection_type]

    # Initialize the output dictionary with the branches
    for branch_num in range(1, num_branches+1):
        b_name = "B%d" % branch_num # Branch name is Bn where n is the branches ID
        OUTPUT_DICT["Branches"][b_name] = {}

    for row in range(MIN_ROW, MAX_ROW):  # For each row that may contain data
        if row_has_data(sheet, row):        # Check if this row has data
            input_data = get_input_from_row(sheet, row, num_branches)   # Get the data
            units = input_data[VALUNITS].lower()


            # Fill out OUTPUT_DICT with data from each branch for this attribute
            for branch_num in range(0, num_branches):
                b_name = "B%d" % (branch_num+1)
                user_value = input_data[USERVAL+branch_num]
                if units in UNIT_CONVERT.keys():
                    user_value = UNIT_CONVERT[units][user_value]
                # TODO normalize the data using the units
                # TODO verify inbound lanes sum up to numLanes

                # write to output
                OUTPUT_DICT["Branches"][b_name][input_data[SUMOATTR]] = user_value


def row_has_data(sheet, row_num):
    """
    Checks whether or not this row contains a user-entered value
    :param sheet: openpyxl sheet - The sheet to use
    :param row_num: The row to analyze
    :return: Boolean - True if there is data, False otherwise
    """

    # Get the data from the row
    rows = sheet.iter_rows(min_col=1, min_row=row_num, max_col=15, max_row=row_num)
    for row in rows:    # FIXME Is there a better way to look at just 1 row
        # if there is no SUMO Attribute specified, then there is no user entered data available
        sumo_attr = row[SUMO_ATTR_COLUMN].value
        if sumo_attr is None:
            return False
        else:
            return True

    # should not be executed
    print("ERROR - row_has_data() did not find row")
    return False


def parse_stats(sheet):
    current_category = None
    for row in range(MIN_ROW, 100):
        if row_has_category(sheet, row) is not None:
            current_category = row_has_category(sheet, row)
            if current_category is not None:
                current_category = current_category.lower()
                OUTPUT_DICT["stats"][current_category] = {}
            continue
        else:
            if current_category in ["general", "parameters"]:
                if row_has_data(sheet, row):
                    input_data = get_input_from_row(sheet, row, cols=1)
                    OUTPUT_DICT["stats"][current_category][input_data[SUMOATTR]] = input_data[USERVAL]
            else:
                if current_category == "population":
                    sub_tag = "bracket"
                    num_entries = 100
                    data = None
                    if row_has_data(sheet, row):
                        input_data = get_input_from_row(sheet, row, cols=100)
                        num_entries = min(num_entries, len(input_data)-3)
                        if data is None:
                            data = {}
                            for i in range(0, num_entries):
                                data["%s_%d" % (sub_tag, i)] = {}  # Bracket_0: {}, Bracket_1: {} etc
                        for i in range(0, num_entries):
                            data["%s_%d" % (sub_tag, i)][input_data[SUMOATTR]] = input_data[USERVAL+i]
                    print(data)
                    if sub_tag not in OUTPUT_DICT["stats"][current_category].keys():
                        OUTPUT_DICT["stats"][current_category][sub_tag] = {}

                    OUTPUT_DICT["stats"][current_category][sub_tag][input_data[SUMOATTR]] = data
                    print(input_data)


def row_has_category(sheet, row_num):
    """
    Checks to see if this row starts a new category
    :param sheet: openpyxl sheet - The sheet to use
    :param row_num: The row to analyze
    :return: Boolean - True if there is a new category, False otherwise
    """

    # Get the data from the row
    rows = sheet.iter_rows(min_col=1, min_row=row_num, max_col=15, max_row=row_num)
    for row in rows:    # FIXME Is there a better way to look at just 1 row
        # If there is text in the Category Column then it is a new category
        class_name = row[CATEGORY_COLUMN].value
        if class_name is None:
            return None
        else:
            return class_name

    # should not be executed
    print("ERROR - row_has_category() did not find any rows")
    return None


def get_input_from_row(sheet, row_num, cols=1):
    """
    Retrieves the input from the row and returns a tuple of all the relevant data
    :param sheet:
    :param row_num:
    :param cols:
    :return: Tupple containing the data -
              formatted as (sumo_file, sumo_attribute, units, user_val1, user_val2...)
    """
    output = []
    rows = sheet.iter_rows(min_col=1, min_row=row_num, max_col=VALUE_COLUMN+cols, max_row=row_num)

    for row in rows:
        # Determine the SUMO_FILE attribute
        sumo_file = row[SUMO_FILE_COLUMN].value
        if sumo_file is None: sumo_file = "N/A"
        output.append(sumo_file)

        # Determine the SUMO_ATTR attribute
        sumo_attr = row[SUMO_ATTR_COLUMN].value
        if sumo_attr is None: sumo_attr = "N/A"
        output.append(sumo_attr)

        # Determine the units
        units = row[UNITS_COLUMN].value  # TODO check if user entered units
        if units is None: units = "N/A"
        output.append(units)

        # Determine all user entered values
        for col in range(VALUE_COLUMN, VALUE_COLUMN+cols):
            user_value = row[col].value
            if user_value is None: break
            output.append(user_value)

        return tuple(output)


def run_parser(excel_file_path, outpath):
    wb = load_workbook(filename=excel_file_path, data_only=True)

    parse_general(wb["General Settings"])
    type = parse_intersection(wb["Intersection Settings"])
    if parse_intersection is None:
        print("ERROR")
        return -1
    parse_branches(wb["Branch Settings"], type)
    # parse_stats(wb["Advanced Customization"])


#    print(OUTPUT_DICT)

    # Context manager to dump parsed config to json
    with open(outpath+"/parser_output.json", 'w') as outfile:
        json.dump(OUTPUT_DICT, outfile, indent=4,)

    return OUTPUT_DICT


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
