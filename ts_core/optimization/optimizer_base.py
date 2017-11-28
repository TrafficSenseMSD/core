import traci
import logging
logger = logging.getLogger('ts_core')

class OptimizerBase(object):
    def __init__(self):
        pass

class LightControl(object):
    def __init__(self):
        pass

    def get_command(self):
        return self._controller()

    def _controller(self,):
        logger.info("TrafficLight Phase: " + str(traci.trafficlight.getPhase("0")))
        logger.info(traci.trafficlight)
        if traci.trafficlight.getPhase("0") == 2:
            # we are not already switching
            if traci.inductionloop.getLastStepVehicleNumber("0") > 0:
                return 3
            else:
                return 2

