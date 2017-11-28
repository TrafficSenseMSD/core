import sys
import os
import random
import traci
import sumolib
from ts_core.utils.ts_logging import setup_logging
from ts_core.optimization.optimizer_base import LightControl

import logging
logger = logging.getLogger('ts_core')


def make_d_objs() -> dict():
    out = {
        "trafficlight": traci.trafficlight
    }

def run_loop():
    """
    Returns
    -------

    """
    lc = LightControl()

    step = 0
    # we start with phase 2 where EW has green
    traci.trafficlight.setPhase("0", 2)
    while traci.simulation.getMinExpectedNumber() > 0:
        logger.debug("Step: %s" % step)
        traci.simulationStep()

        command = lc.get_command()
        if command:
            traci.trafficlight.setPhase("0", command)

        step += 1
    traci.close()
    sys.stdout.flush()
