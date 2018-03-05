

from openpyxl import *


MIN_COLUMN = 2

MIN_ROW = 3  # Minimum row number where config information CAN be stored


# List of file extensions
ROUTE = "rou"
NET = "net"


TAB_NAMES = ["Vehicle Type Customization", "General Settings", "Intersection Definition", "Branch Settings"]


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


def get_input_from_row(sheet, row_num):
    """

    Parameters
    ----------
    sheet
    row_num

    Returns
    -------

    """
    row = sheet.get_squared_range(min_col=MIN_COLUMN, min_row=row_num, max_col=8, max_row=row_num)

    for row0 in row:
        sumo_attr = row0[0].value
        sumo_file = row0[1].value
        user_value = row0[5].value
        units = row0[4].value  # TODO check if user entered units


        return sumo_attr, sumo_file, user_value


def main():

    output_dict = {}  # [[FILE, attribute, user response1, user_response2], ... ]

    wb = load_workbook(filename='Configuration_template.xlsx')

    sheet_ranges = wb['General Settings']

    output_dict = parse_vehicles(wb["Vehicle Type Customization"])


if __name__ == "__main__":
    main()
