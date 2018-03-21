import traci
import traci.constants as tc

class VariableDictionary():
    self.domains = {
        'edge':(self.edge, traci.edge),
        'gui': (self.gui, traci.gui),
        'induction loop': (self.inductionloop, traci.inductionloop),
        'junction': (self.junction, traci.junction),
        'lane': (self.lane, traci.lane),
        'lane area': (self.lanearea, traci.lanearea),
        'multi-entry-exit detector': (self.multientryexit, traci.multientryexit),
        'person': (self.person, traci.person),
        'poi': (self.poi, traci.poi),
        'polygon': (self.polygon, traci.polygon),
        'route': (self.route, traci.route),
        'simulation': (self.simulation, traci.simulation),
        'traffic light': (self.trafficlight, traci.trafficlight),
        'vehicle': (self.vehicle, traci.vehicle),        
        'vehicle type': (self.vehicletype, traci.vehicletype)
    }
    
    self.edge = {}
        # 'id list': traci.edge.getIDList,
        # 'count': traci.edge.getIDCount,
        # 'lane number': traci.edge.getLaneNumber,
        # 'current travel time': traci.edge.getTraveltime,
        # 'CO2 emissions': traci.edge.getCO2Emission,
        # 'CO emissions': traci.edge.getCOEmission,
        # 'HC emissions': traci.edge.getHCEmission,
        # 'PMx emissions': traci.edge.getPMxEmission,
        # 'NOx emissions': traci.edge.getNOxEmission,
        # 'fuel consumption': traci.edge.getFuelConsumption,
        # 'noise emission': traci.edge.getNoiseEmission,
        # 'electricity consumption': traci.edge.getElectricityConsumption,
        # 'last step vehicle number': traci.edge.getLastStepVehicleNumber,
        # 'last step mean speed': traci.edge.getLastStepMeanSpeed,
        # 'last step vehicle ids': traci.edge.getLastStepVehicleIDs,
        # 'last step occupancy': traci.edge.getLastStepOccupancy,
        # 'last step mean vehicle length': traci.edge.getLastStepLength,
        # 'waiting time': traci.edge.getWaitingTime,
        # 'last step person ids': traci.edge.getLastStepPersonIDs,
        # 'last step halting number': traci.edge.getLastStepHaltingNumber} ]
        
    self.gui = {}
    self.inductionloop = {}
    self.junction = {}
    self.lane = {}
    self.lanearea = {}
    self.multientryexit = {}
    self.person = {}
    self.poi = {}
    self.polygon = {}
    self.route = {}
    self.simulation = {}
    self.trafficlight = {}
    
    self.vehicle = {
        'slope': tc.VAR_SLOPE,
        'speed': tc.VAR_SPEED,
        'max speed': tc.VAR_MAXSPEED,
        'position 2d': tc.VAR_POSITION,
        'position 3d': tc.VAR_POSITION3D,
        'angle': tc.VAR_ANGLE,
        'color': tc.VAR_COLOR,
        'max acceleration': tc.VAR_ACCEL,
        'road id': tc.VAR_ROAD_ID,
        'lane position': tc.VAR_LANEPOSITION}
        
    self.vehicletype = {}
    
    def get_var(self, domain_label, attribute_label):
        if domain_label in self.domains:
            try:
                return self.domains[domain][0][attribute]
            except KeyError:
                print('ERROR::VariableDictionary.get_var: key {} not found in {} dictionary.'.format(attribute_label, domain_label))
        else:
            print('ERROR::VariableDictionary:get_var: domain {} does not exist'.format(domain_label))
            
    def get_domain_dictionary(self, domain_label):
        try:
            return self.domains[domain_label]
        except KeyError:
            print('ERROR::VariableDictionary:get_var: domain {} does not exist'.format(domain_label))