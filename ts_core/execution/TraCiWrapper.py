"""

.. _ts_runner_traci:

``ts_runner`` TRACI Interface 
=============================


"""
import traci
import traci.constants as tc
import runner


class TraCiWrapper():
    def __init__(self, optimizer, simulation):
        self.optimizer = optimizer
        # self.start_simulation()
        # SUMO simulation network must first be initialized
        self.lane_ids = traci.getIDList()
        self.variable_subscription_polling_rate = 30  # frequency of variable polling (sample/time steps)
        self.final_iteration = simulation.final_iteration
        self.lane_variables = (tc.VAR_CO2EMISSION, tc.VAR_COEMISSION,
                               tc.VAR_HCEMISSION, tc.VAR_PMXEMISSION, tc.VAR_NOXEMISSION)

    # def establish_lane_subscriptions(self):
    #     begin_time = self.variable_subscription_polling_rate
    #     end_time = self.final_iteration
    #     for lane_id in self.lane_ids:
    #         traci.lane.subscribe(lane_id, self.lane_variables)
    #
    # def get_lane_subscription_results(self, lane_id=None):
    #     if lane_id:
    #         return traci.lane.getSubscriptionResults(lane_id)
    #     else:
    #         results = {}
    #         for lane_id in self.lane_ids:
    #             results[lane_id] = traci.lane.getSubscriptionResults(lane_id)
    #         return results

    def get_emissions_values(self, lane_id=None):
        if lane_id:
            co2 = traci.lane.getCO2Emmission(lane_id)
            co = traci.lane.getCOEmission(lane_id)
            hc = traci.lane.getHCEmission(lane_id)
            nox = traci.lane.getNOxEmission(lane_id)
            pmx = traci.lane.getPMxEmission(lane_id)
            return [co2, co, hc, pmx, nox]
        else:
            emissions_values = {}
            for lane_id in self.lane_ids:
                co2 = traci.lane.getCO2Emmission(lane_id)
                co = traci.lane.getCOEmission(lane_id)
                hc = traci.lane.getHCEmission(lane_id)
                nox = traci.lane.getNOxEmission(lane_id)
                pmx = traci.lane.getPMxEmission(lane_id)
                emissions_values[lane_id] = [co2, co, hc, pmx, nox]
            return emissions_values

    def get_lane_occupancy_statistics(self, lane_id=None):
        if lane_id:
            num_vehicles = traci.lane.getLastStepVehicleNumber(lane_id)
            waiting_time = traci.lane.getWaitingTime(lane_id)
            travel_time = traci.lane.getTravelTime(lane_id)
            number_halted = traci.lane.getLastStepHaltingNumber(lane_id)
            return [num_vehicles, waiting_time, travel_time, number_halted]
        else:
            stats = {}
            for lane_id in self.lane_ids:
                num_vehicles = traci.lane.getLastStepVehicleNumber(lane_id)
                waiting_time = traci.lane.getWaitingTime(lane_id)
                travel_time = traci.lane.getTravelTime(lane_id)
                number_halted = traci.lane.getLastStepHaltingNumber(lane_id)
                stats[lane_id] = [num_vehicles, waiting_time, travel_time, number_halted]
            return stats

    def start_simulation(self):
        runner.run()
