#!/usr/bin/python


SUMO_ATTR_COLUMN = 0    # Column A
SUMO_FILE_COLUMN = 1    # Column B
CLASS_COLUMN = 2
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
    "stats": {},
}