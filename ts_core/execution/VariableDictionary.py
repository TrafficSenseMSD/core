import traci
import traci.constants as tc

class VariableDictionary():
    def __init__(self):
        
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
        self.lane = {
        'waiting time': tc.VAR_WAITING_TIME}
        self.lanearea = {}
        self.multientryexit = {}
        self.person = {}
        self.poi = {}
        self.polygon = {}
        self.route = {}
        self.simulation = {}
        #self.trafficlight = {}
        
        self.vehicle = {
            'slope': tc.VAR_SLOPE,
            'speed': tc.VAR_SPEED,
            'position 2d': tc.VAR_POSITION,
            'position 3d': tc.VAR_POSITION3D,
            'angle': tc.VAR_ANGLE,
            'color': tc.VAR_COLOR,
            'max acceleration': tc.VAR_ACCEL,
            'max comfortable deceleration': tc.VAR_DECEL,
            'max possible deceleration': tc.VAR_EMERGENCY_DECEL,
            'driver imperfection': tc.VAR_IMPERFECTION,
            'speed factor': tc.VAR_SPEED_FACTOR,
            'speed deviation': tc.VAR_SPEED_DEVIATION,
            'road id': tc.VAR_ROAD_ID,
            'lane position': tc.VAR_LANEPOSITION,
            'type id': tc.VAR_TYPE,
            'lane id': tc.VAR_LANE_ID,
            'lane index': tc.VAR_LANE_INDEX,
            'route id': tc.VAR_ROUTE_ID,
            'edges': tc.VAR_EDGES,
            'route': tc.VAR_ROUTE,
            'travel time information': tc.VAR_EDGE_TRAVELTIME,
            'effort information': tc.VAR_EDGE_EFFORT,
            'signals state': tc.VAR_SIGNALS,
            'new lane/position along': tc.VAR_MOVE_TO,
            'routing mode': tc.VAR_ROUTING_MODE,
            'best lanes': tc.VAR_BEST_LANES,
            'how speed is set': tc.VAR_SPEEDSETMODE,
            'stopped?': tc.VAR_STOPSTATE,
            'lane changing mode': tc.VAR_LANECHANGE_MODE,
            'max allowable speed': tc.VAR_ALLOWED_SPEED,
            'position (lateral)': tc.VAR_LANEPOSITION_LAT,
            'prefered lateral alignment': tc.VAR_LATALIGNMENT,
            'max lateral speed': tc.VAR_MAXSPEED_LAT,
            'min lateral gap': tc.VAR_MINGAP_LAT,
            'vehicle height': tc.VAR_HEIGHT,
            'current CO2 emission': tc.VAR_CO2EMISSION,
            'current CO emission': tc.VAR_COEMISSION,
            'current HC emission': tc.VAR_HCEMISSION,
            'current PMx emission': tc.VAR_PMXEMISSION,
            'current NOx emission': tc.VAR_NOXEMISSION,
            'current fuel consumption': tc.VAR_FUELCONSUMPTION,
            'current noise emission': tc.VAR_NOISEEMISSION,
            'current person number': tc.VAR_PERSON_NUMBER,
            'current leader together with gap': tc.VAR_LEADER,
            'edge index in current route': tc.VAR_ROUTE_INDEX,
            'current waiting time': tc.VAR_WAITING_TIME,
            'upcoming traffic lights': tc.VAR_NEXT_TLS,
            'current electricity consumption of a node': tc.VAR_ELECTRICITYCONSUMPTION}
            
        self.vehicletype = {
            'max speed': tc.VAR_MAXSPEED,
            'angle': tc.VAR_ANGLE,
            'length': tc.VAR_LENGTH,
            'color': tc.VAR_COLOR,
            'max acceleration': tc.VAR_ACCEL,
            'max comfortable deceleration': tc.VAR_DECEL,
            'max possible deceleration': tc.VAR_EMERGENCY_DECEL,
            'drivers desired headway': tc.VAR_TAU,
            'vehicle class': tc.VAR_VEHICLECLASS,
            'emission class': tc.VAR_EMISSIONCLASS,
            'shape class': tc.VAR_SHAPECLASS,
            'minimum gap': tc.VAR_MINGAP,
            'width': tc.VAR_WIDTH,
            'max lateral speed': tc.VAR_MAXSPEED_LAT,
            'vehicle height': tc.VAR_HEIGHT}
        
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
            #'traffic light': (self.trafficlight, traci.trafficlight),
            'vehicle': (self.vehicle, traci.vehicle),        
            'vehicle type': (self.vehicletype, traci.vehicletype)
        }
    
    #will make a new table for quicker lookup, but quick soln for now:
    def get_attribute_label(self, domain_label, code):
        for key in self.domains[domain_label][0]:
            if self.domains[domain_label][0][key] == code:
                return key
    
    def get_var(self, domain_label, attribute_label):
        if domain_label in self.domains:
            try:
                return self.domains[domain_label][0][attribute_label]
            except KeyError:
                print('ERROR::VariableDictionary.get_var: key {} not found in {} dictionary.'.format(attribute_label, domain_label))
        else:
            print('ERROR::VariableDictionary:get_var: domain {} does not exist'.format(domain_label))
            
    def get_domain_dictionary(self, domain_label):
        try:
            return self.domains[domain_label]
        except KeyError:
            print('ERROR::VariableDictionary:get_var: domain {} does not exist'.format(domain_label))