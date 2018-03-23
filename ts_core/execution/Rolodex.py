import traci
import numpy as np
from pandas import Panel
from pandas import DataFrame
import VariableDictionary as vd
        
class DataBuffer():
    '''
    Buffers to hold simulation data
    
    '''
    #attributes = [(attribute label, [id list], sampling frequency), ...]
    def __init__(self, buffer_length, domain, attributes=None, dumpfile=None, id_update_frequency=None):
        self.domain = domain #e.g.: traci.junction
        self.attributes = attributes #(attribute label, [id list], sampling frequency)
        self.buffer_length = buffer_length
        self.dumpfile = dumpfile
        self.subscription_ledger = {}
        self.id_table = {}
        self.attribute_table = {}
        
        #create subscription ledger and attribute table
        # 'car100':[(attribute_label,sampling_frequency,simulation_ticks_since_last_update), ...]
        for attribute in self.attributes:
            self.attribute_table[attribute[0]] = attribute[1]
            if not attribute[1]:
                #empty ID list, get current list from domain
                ids = self.domain.getIDList()#VERIFY OUTPUT
            else:
                ids = attribute[1]
            for id in ids:
                try:
                    if self.subscription_ledger[id]:
                        self.subscription_ledger[id].append((attribute[0],attribute[2],0))
                except KeyError:
                    self.subscription_ledger[id] = [(attribute[0],attribute[2],0)]            

        #create ID look-up table
        index = 0
        for id in self.subscription_ledger.keys():
            self.id_table[id] = [index]
            for attribute in id:
                self.id_table[id].append(attribute[0])
            index += 1
        self.num_ids = index
            
        #zeros len(attributes) x len(IDs) x buffer_len
        z = np.zeros(len(self.attributes), self.num_ids, self.buffer_length)
        
        # Panel = collection of DataFrames:
        # Each DataFrame corresponds with an ID:
        #
        #              'car100'         |         'car101'              |
        #               ------          |          ------               |
            #          Attribute:       |                               |
            #          lane    speed    |        travel time    speed   |
            #Tick   3   5a      29      |   131       52          32    |
            #       2   5a      27      |   130       51          31    |  
            #       1   5a      23      |   129       50          30    |
            #       0   4a      16      |   128       49          31    |
        panel_frames = {}
        for id in self.id_table:
            (self.id_table[id])
            frame_dict = {}
            for attribute in id_table[id]:
                frame_dict[attribute] = np.zeros(self.buffer_length)
            panel_frames[id] = DataFrame(frame_dict)
        self.buffer = Panel(data = panel_frames)
        #self.buffer = Panel(data=z, major_axis=self.attribute_table.keys().sorted(), minor_axis=self.id_table.keys().sorted())
            
            
    #id = 'car100'
    #data = {'lane position':123.12345123451234, ...}
    def update(self, id, data):
        rbuffer = self.buffer[id]
        oldest_data = rbuffer.loc[self.buffer_len-1,slice(None)]
        for attribute in data:
            self.buffer[id].loc[self.buffer_len-1,attribute] = data[attribute]
        self.buffer[id] = self.buffer[id].reindex(rbuffer.axes[0]._cache['_data'])
        return oldest_data
                    
    def add(self, id_table):
        return
        
    #attribute can be name string or buffer index
    #example remove ids 1,2,3 of attributes 'a','b','c':
    #   [('a', [1,2,3]),
    #    ('b', [1,2,3]),
    #    ('c', [1,2,3])]
    #example remove all ids of attributes 'a','b','c':
    #   [('a', []),
    #    ('b', []),
    #    ('c', [])]
    def remove(self, attributes=None):
        for attribute in attributes:
            if attribute[1] == []:
                self.frame.remove_col
            else:
                pass
        
    def dump(self, dumpfile=None):
        if self.dumpfile:
            print('Changing dumpfile from {} to {}'.format(self.dumpfile.name, dumpfile.name))
        self.dumpfile = dumpfile
        self.dumpfile.write(self.frame.to_pickle())
        self.dumpfile.flush()
        
    def reset(self, attributes=None):
        if not attributes:
            self.__init__(attributes=self.attributes, buffer_length=self.buffer_length,
            frame_time=self.frame_time, dumpfile=self.dumpfile, ticks_per_second = self.ticks_per_second)
        else:
            for attribute in attributes:
                pass

class Rolodex():
    """
    Data buffer wrapper class
    
    Parameters
    ----------
    attributes - what data is needed to be collected, strings found in SumoAttributeDictionary
        An empty id list will gather the specified attribute data for every id available 
        at setup time
        Can specify unique sampling frequencies for each attribute/context id, or choose
        to use a global sampling frequency for all attributes
        
        (context, attribute label, [id list], sampling frequency)
        
    buffer_length - if a global buffer length is desired for all attributes
    
    dumpfile - file pointer to dump buffer contents to when requested / on fatal errors
    
    Returns
    -------
    Nothing
    """
   
    def __init__(self, attributes=None, buffer_length=None, frame_time=None, simulation_run_time=None, dumpfile=None, id_update_frequency=None, ticks_per_second=1):
        self.frame_time = frame_time
        self.simulation_run_time = simulation_run_time
        self.ticks_per_second = ticks_per_second
        self.default_buffer_length = 100
        self.buffers = {}
        
        self.context_domains = {}
        self.context_domains['edge'] = traci.edge
        self.context_domains['gui'] = traci.gui
        self.context_domains['induction loop'] = traci.inductionloop
        self.context_domains['junction'] = traci.junction
        self.context_domains['lane'] = traci.lane
        self.context_domains['lane area'] = traci.lanearea
        self.context_domains['multi-entry-exit detector'] = traci.multientryexit
        self.context_domains['person'] = traci.person
        self.context_domains['poi'] = traci.poi
        self.context_domains['polygon'] = traci.polygon
        self.context_domains['route'] = traci.route
        self.context_domains['simulation'] = traci.simulation
        self.context_domains['traffic light'] = traci.trafficlight
        self.context_domains['vehicle'] = traci.vehicle
        self.context_domains['vehicle type'] = traci.vehicletype
        
        self.domain_attributes = {}
        for domain in context_domains:
            self.domain_attributes[domain] = []

        for attribute in attributes:
            try:
                self.domain_attributes[attribute[0]].append(attribute[1:]) #verify appending a list for each attribute, not params of each
            except KeyError:
                print('ERROR:Rolodex:__init__:attributes :: attribute context: {} in {} not valid'.format(attribute[0], attribute))
        
        if buffer_length:
            self.buffer_length = buffer_length
        else:
            if self.frame_time:
                self.buffer_length = self.frame_time / self.ticks_per_second
            else:
                self.buffer_length = self.default_buffer_length
                print('WARNING:Rolodex:__init__: Using default buffer lengths of {} for {} domain'.format(self.default_buffer_length, domain))

        for domain in self.domain_attributes:
            if self.domain_attributes[domain]:
                context = self.context_domains[domain]
                self.buffers[domain] = DataBuffer(self.buffer_length, context, attributes=self.domain_attributes[domain], id_update_frequency=id_update_frequency)
                self.setup_subscription(context, self.buffers[domain].id_table)
        
    #id_table = 'car100':[attribute_label_0,attribute_label_1, ...]
    def setup_subscription(self, domain, id_table):
        for id in id_table:
            domain.subscribe(id, (id_table[id]))
            
    #id_table = 'car100':[attribute_label_0,attribute_label_1, ...]
    #also adds to DataBuffer
    def add_subscription(self, domain, id_table):
        for id in id_table:
            domain.subscribe(id, (id_table[id]))
            domain
        
    def list_context_domains(self):
        for context in self.context_domains:
            print('{}:{}'.format(context, context_domains[context]))
            
    #context_attributes = [(context_domain, contextID, attribute_domain, range, [attributes])]
    #example: [junctionID, tc.CMD_GET_VEHICLE_VARIABLE, 42, [tc.VAR_SPEED, tc.VAR_WAITING_TIME]]
    def setup_context_subscription(self, context_attributes=None):
        for context in context_attributes:
            if context[0] in self.context_domains:
                context_domains[context[0]].subscribe(context[1], context[2], context[3], context[4])
            else:
                print('Error: Invalid Context Domain: {}'.format(context[0]))
                
    #Ability to set the frequency of updates for each attribute after instantiation
    def set_update_frequency(self, attribute, num_simulation_ticks_between_samples, ids=[]):
        return
        
        
    #Update functions
    #Automatically update data at the specified frequency
    #Manually update when requested
    # domains = ['junction', 'vehicle', ...]
    #TODO: Implement frequency schedule updates
    def update_subscription_buffers(self, domains=[]):
        i = 0
        while i < 2:
            try:
                if not domains:
                domains = self.context_domains.keys()
                for domain in domains:
                    buffer = self.buffers[domain]
                    for id in buffer.id_table:
                        # buffer.id_table = {
                        #   'car100':[(attribute_label,sampling_frequency,simulation_ticks_since_last_update), ...],
                        #   'car101':[(attribute_label,sampling_frequency,simulation_ticks_since_last_update), ...]
                        #}       
                        data = self.context_domains[domain].getSubscriptionResults(id)
                        buffer.update(id, data)
                        #for attribute in id_table[id]:
                            #if attribute[2] == attribute[1]:#if time to sample, based on sampling frequency
                            #buffer.update(id, attribute[0], data[vd.get_var(domain, attribute[0])])                        
            except MemoryError as e:
                print(e)
                self.dump_to_file()
                if i == 1:
                    print('UPDATE ABORTED: MEMORY ERROR')
                    return
     
    # domain = 'junction'    
    # id_table = {
    #   'car100':[(attribute_label,sampling_frequency,simulation_ticks_since_last_update), ...],
    #   'car101':[(attribute_label,sampling_frequency,simulation_ticks_since_last_update), ...]
    #}       
    def update(self, domain, id_table=[]):
        buffer = self.buffers[domain]
        for id in id_table:
            if id not in buffer.id_table:
                print('WARNING::Rolodex.update_subscription_buffers: ID: {} not in {} Subscription ID Table, adding the following attribute subscriptions:'.format(id,domain))
                self.add_subscription(domain, {id:id_table[id]})# VERIFY behavior with customer
            data = self.context_domains[domain].getSubscriptionResults(id)
            for attribute in id_table[id]:
                #if attribute[2] == attribute[1]:#if time to sample, based on sampling frequency
                buffer.update(id, attribute[0], data[vd.get_var(domain, attribute[0])])
        
    #Returns a copy of the data buffers for the given domains
    #domains = ['vehicle', 'lane', ...]
    def get_data(self, domains=[]):
        data = {}
        for domain in domains:
            data[domain] = self.buffers[domain].buffer.values()
        return data

    #Option to dump buffers to file
    def dump_to_file(self, domain=None, dumpfile=None):
        if domain:
            self.buffers[domain].dump(dumpfile=dumpfile)
        else:
            for buffer in self.buffers:
                buffer.dump(dumpfile=dumpfile)
        
    #Function to retrieve the value of an attribute without a subscription
    def get_value(self, attributes=None, ids=[]):
        return
        
    def remove_subscription(self, attributes=[], ids=[]):
        pass
        
    #Function to clear and reset buffers
    def reset(self, attributes=None, ids=[]):
        pass

if __name__ == '__main__':
    buffers = Rolodex(attributes=attribute_frequency_list)
    #Or initialize without assigning attributes to set up collection of all available attributes. Can set global_sampling_frequency for all attributes/ids, or use default of updating every simulation tick
    buffers = Rolodex(global_sampling_frequency=60)