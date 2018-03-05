import jsmin
import json
from ts_core.config.config_helpers import *
from ts_core.config.config_exceptions import *


def transform_parsed_excel(parsed):
    if "SUMOCFG" not in parsed:
        raise
    mk_sumocfg(parsed["SUMOCFG"])


if __name__ == "__main__":
    with open('parser_output.json', 'r') as _bad_json:
        parsed = jsmin.jsmin(_bad_json.read())
        parsed = json.loads(parsed)
        transform_parsed_excel(parsed)


        print(json.dumps(parsed, indent=3))
