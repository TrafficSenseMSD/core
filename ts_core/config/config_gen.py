import jsmin
import json
import pyxb
pyxb._CorruptionDetectionEnabled = False
from ts_core.config.config_helpers import *
from ts_core.config.config_exceptions import *


def transform_parsed_excel(parsed):
    """
    This is the manager function transforming
    
    Parameters
    ----------
    parsed

    Returns
    -------
    None
    
    """
    if "SUMOCFG" not in parsed:
        raise ParsedSchemaError("Key 'SUMOCFG' is not in top level dict")

    sumocfg_xml = mk_sumocfg(parsed["SUMOCFG"])
    node_xml = mk_node(parsed['Intersections'], parsed['Branches'])

    print(sumocfg_xml)
    print(node_xml)

# if __name__ == "__main__":
#     with open('/Users/eilifm/github/eilifm/trafficsense/core/ts_core/excel_parser/parser_output_em.txt', 'r') as _bad_json:
#         parsed = jsmin.jsmin(_bad_json.read())
#         parsed = json.loads(parsed)
#         transform_parsed_excel(parsed)
#
#     with open("/Users/eilifm/github/eilifm/trafficsense/core/ts_core/excel_parser/parser_output.txt", 'w') as outfile:
#         json.dump(parsed, outfile, indent=4)
