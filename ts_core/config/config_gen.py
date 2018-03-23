import jsmin
import json
import pyxb
pyxb._CorruptionDetectionEnabled = False
from ts_core.config.config_helpers import *
from ts_core.config.config_exceptions import *


def transform_parsed_excel(parsed, project_path, stats_file):
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

    import pprint
    pprint.pprint(parsed)
    sumocfg_xml = mk_sumocfg(parsed["SUMOCFG"])
    node_xml = mk_node(parsed['Intersections'], parsed['Branches'])
    edge_xml = mk_edge(parsed['Intersections'], parsed['Branches'])

    # Write SUMO config XML
    with open(project_path+"/config.sumocfg", "w") as cfg_file:
        cfg_file.write(sumocfg_xml)

    # White nodes XML
    with open(project_path + "/node.nod.xml", "w") as cfg_file:
        cfg_file.writelines(node_xml)

    # Write edges XML
    with open(project_path + "/edge.edg.xml", "w") as cfg_file:
        cfg_file.writelines(edge_xml)

    # Write stats XML
    with open(project_path + "/activity.stats.xml", "w") as cfg_file:
        cfg_file.writelines(stats_file)



# if __name__ == "__main__":
#     with open('/Users/eilifm/github/eilifm/trafficsense/core/ts_core/excel_parser/parser_output_em.txt', 'r') as _bad_json:
#         parsed = jsmin.jsmin(_bad_json.read())
#         parsed = json.loads(parsed)
#         transform_parsed_excel(parsed)
#
#     with open("/Users/eilifm/github/eilifm/trafficsense/core/ts_core/excel_parser/parser_output.txt", 'w') as outfile:
#         json.dump(parsed, outfile, indent=4)
