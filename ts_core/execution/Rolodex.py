"""
.. _ts_runner_rolodex:


``Rolodex`` Overview
======================
``Rolodex`` handles data collection through TraCi variable subscriptions, data access, and supporting functions


Software Structure and Implementation
-------------------------------------

Light Control
-------------
``ts_runner`` will accept an argument that specifies the file and class name to import at startup.  Messing with this
part of Python is tricky business.

Optimization
------------
ts_runner looks for a file named optimizer_example to run
inside the optimizer_example file an OptimizerExample class is expected to exist with a function called ``train`` which is called after every simulation tick


Output
------

Output from ts_runner is directed to ``<sumo_project_dir>/output/<YYYY_MM_DD_HH_MM_SS_dddddd>/'' which
contains:
    ``sutripinfo.xml``
    ``YYYY_MM_DD_HH_MM_SS_dddddd_ts_runner.log`` (Not yet implemented, writes to current dir)



"""
import traci
import numpy as np
# from pandas import Panel
# from pandas import DataFrame
from ts_core.execution.VariableDictionary import VariableDictionary as vd


class DataBuffer():
    '''
    Buffers to hold simulation data collected by subscriptions

    '''

    def __init__(self, buffer_length, domain, attributes=None, dumpfile=None, id_update_frequency=None):
        """

        Parameters
        ----------
        buffer length: the number of values saved per attribute
        domain: the TraCi domain used e.g. 'Vehicle', 'lane'
        attributes: the attributes, ids, and sampling frequencies to be collected in the buffer e.g.
            attributes = [(attribute label, [id list], sampling frequency), ...]
            attributes = [('lane position', ['car100' 'car101'], 1), ('speed', [], 1)]
            an empty id list will collect the attribute for every object of the given domain that enters the simulation
        dumpfile: file to dump data to in case of memory overfill
        id_update_frequency: how often to update the list of objects in the simulation when auto-updating
        Returns
        -------
        The list of ids of objects of the given domain that are discovered when initializing the databuffer, if no ids are passed

        """
        self.domain = domain  # e.g.: traci.junction
        self.attributes = attributes  # (attribute label, [id list], sampling frequency)
        self.buffer_length = buffer_length
        self.dumpfile = dumpfile
        self.subscription_ledger = {}
        self.id_table = {}
        self.attribute_table = {}
        self.auto_update_attributes = []
        self.last_tick_num = 1

        self.generate_data_structures(self.last_tick_num)

    def generate_data_structures(self, tick_num):
        """
        Generates lookup tables for the buffer

        Parameters
        ----------
        tick_num: the tick number of the simulation

        Returns
        -------
        The list of ids of objects of the given domain that are discovered, if id_table is empty

        """
        self.last_tick_num = tick_num
        new_ids = []
        # create subscription ledger and attribute table
        # 'car100':[(attribute_label,sampling_frequency,simulation_ticks_since_last_update), ...]
        for attribute in self.attributes:
            self.attribute_table[attribute[0]] = attribute[1:]
            if not attribute[1]:
                if attribute[0] not in self.auto_update_attributes:
                    self.auto_update_attributes.append(attribute[0])
                # empty ID list, get current list from domain
                ids = self.domain.getIDList()
                new_ids = ids
            else:
                ids = attribute[1]
            for id in ids:
                # create subscription ledger
                try:
                    self.subscription_ledger[id].append((attribute[0], attribute[2], attribute[2]))
                except KeyError:
                    self.subscription_ledger[id] = [(attribute[0], attribute[2], attribute[2])]

                # create ID look-up table
                print('ID: {}, attribute: {}'.format(id, attribute[0]))
                try:
                    self.id_table[id].append(attribute[0])
                except KeyError:
                    self.id_table[id] = [attribute[0]]

        print('\n\nSubscription Ledger: {}'.format(self.subscription_ledger))
        print('ID table: {}'.format(self.id_table))

        # vehicle domain buffer:
        # 'car100' : { last_tick:{'lane':'0','speed':0} }
        # 'car101' : { last_tick:{'lane':'0','speed':0} }
        self.buffer = {}
        for id in self.id_table:
            tick_dict = {}
            frame_dict = {}
            for attribute in self.id_table[id]:
                frame_dict[attribute] = -1
            tick_dict[self.last_tick_num] = frame_dict
            self.buffer[id] = tick_dict

        return new_ids

    def update(self, id, data, tick_num=None):
        """
        Updates the data stored in the buffer for the given ID

        Parameters
        ----------
        id: the ID of the object in the buffer's domain e.g. 'car100'
        data: a dictionary containing the data to be put into the buffer e.g.
                data = {'lane position':123.12345123451234, ...}

        Returns
        -------
        any data removed from the buffer when inserting the new data

        """
        if not tick_num:
            tick_num = self.last_tick_num + 1
        self.last_tick_num = tick_num
        old_data = {}
        keylist = sorted(self.buffer[id].keys())
        for old in keylist[:-self.buffer_length]:
            old_data[old] = self.buffer[id].pop(old)
        self.buffer[id][tick_num] = data
        return old_data

    # does not support empty ID lists
    def add(self, attributes, tick_num):
        """
        Adds the given attributes to buffer

        Parameters
        ----------
        attributes: attributes/ids/sampling frequencies to be added to the buffer, same as __init__
        tick_num: the tick number of the simulation

        Returns
        -------
        Nothing

        """
        # update subscription ledger and attribute table
        # 'car100':[(attribute_label,sampling_frequency,simulation_ticks_since_last_update), ...]
        overall_new_ids = []
        overall_new_attributes = {}
        # print('attributes: {}'.format(attributes))
        for attribute in attributes:
            new_ids = []
            if attribute[0] in self.attribute_table:
                self.attribute_table[attribute[0]][0].extend(attribute[1])
                old_ids = self.attribute_table[attribute[0]]
                for id in attribute[1]:
                    if id not in old_ids:
                        new_ids.append(id)
            else:
                overall_new_attributes[attribute[0]] = attribute[1]
                self.attribute_table[attribute[0]] = attribute[1]
                new_ids = attribute[1]
            overall_new_ids.append(new_ids)
            # print('new IDs: {}'.format(len(overall_new_ids)))
            for id in new_ids:
                # update subscription ledger
                try:
                    self.subscription_ledger[id].append((attribute[0], attribute[2], attribute[2]))
                except KeyError:
                    self.subscription_ledger[id] = [(attribute[0], attribute[2], attribute[2])]

                # update ID look-up table
                try:
                    self.id_table[id].append(attribute[0])
                except KeyError:
                    self.id_table[id] = [attribute[0]]

        # vehicle domain buffer:
        # 'car100' : { last_tick:{'lane':'0','speed':0} }
        # 'car101' : { last_tick:{'lane':'0','speed':0} }
        for id_list in overall_new_ids:
            for id in id_list:
                frame_dict = {}
                for attribute in self.id_table[id]:
                    frame_dict[attribute] = -1
                if id not in self.buffer:
                    tick_dict = {}
                    tick_dict[tick_num] = frame_dict
                    self.buffer[id] = tick_dict
                else:
                    self.buffer[id][tick_num] = frame_dict

    def remove_id(self, id):
        """
        Removes the specified ID from the buffer

        Parameters
        ----------
        id: the ID of the object to be removed e.g. 'car100'

        Returns
        -------
        Nothing

        """
        sl = self.subscription_ledger.pop(id)
        it = self.id_table.pop(id)
        bd = self.buffer.pop(id)

    def dump(self, dumpfile=None):
        """
        Writes the pickle representation of the buffer to the dumpfile

        Parameters
        ----------
        dumpfile: file handle to write data to

        Returns
        -------
        Nothing

        """
        if self.dumpfile:
            print('Changing dumpfile from {} to {}'.format(self.dumpfile.name, dumpfile.name))
        self.dumpfile = dumpfile
        self.dumpfile.write(self.buffer.to_pickle())
        self.dumpfile.flush()

    def reset(self, attributes=None):
        """
        Resets the buffer (esentially calls __init__ again)

        Parameters
        ----------
        attributes: same as __init__

        Returns
        -------

        """
        if not attributes:
            self.__init__(attributes=self.attributes, buffer_length=self.buffer_length,
                          frame_time=self.frame_time, dumpfile=self.dumpfile, ticks_per_second=self.ticks_per_second)
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

    frame_time: the time period o collect data for
    simulation_run_time: the total time that the simulaion is run for
    dumpfile: the file to dump data to in case of a memory errors
    id_update_frequency: how often to update the the list of objects when auto-updating is used
    ticks_per_second: how many ticks per second of simulation time
    auto_removal_delay: how many simulation ticks to wait before removing the data for an object that has left the simulation

    Returns
    -------
    Nothing
    """

    def __init__(self, attributes=None, buffer_length=None, frame_time=None, simulation_run_time=None,
                 dumpfile=None, id_update_frequency=None, ticks_per_second=1, auto_removal_delay=10):
        self.frame_time = frame_time
        self.simulation_run_time = simulation_run_time
        self.dumpfile = dumpfile
        self.ticks_per_second = ticks_per_second
        self.default_buffer_length = 100
        self.auto_removal_delay = auto_removal_delay
        self.vehicles_to_remove = {}
        self.buffers = {}
        self.var_dict = vd()

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
        # self.context_domains['traffic light'] = traci.trafficlight
        self.context_domains['vehicle'] = traci.vehicle
        self.context_domains['vehicle type'] = traci.vehicletype

        self.domain_attributes = {}
        for domain in self.context_domains:
            self.domain_attributes[domain] = []

        for attribute in attributes:
            try:
                self.domain_attributes[attribute[0]].append(
                    attribute[1:])  # verify appending a list for each attribute, not params of each
            except KeyError:
                print(
                    '\nERROR:Rolodex:__init__:attributes :: attribute context: {} in {} not valid'.format(attribute[0],
                                                                                                          attribute))

        if buffer_length:
            self.buffer_length = buffer_length
        else:
            if self.frame_time:
                self.buffer_length = self.frame_time / self.ticks_per_second
            else:
                self.buffer_length = self.default_buffer_length
                print('\nWARNING:Rolodex:__init__: Using default buffer lengths of {} for {} domain'.format(
                    self.default_buffer_length, domain))

        for domain in self.context_domains:
            if domain in self.domain_attributes:
                print('\nDomain: {}, attributes: {}'.format(domain, self.domain_attributes[domain]))
                if self.domain_attributes[domain]:
                    context = self.context_domains[domain]
                    self.buffers[domain] = DataBuffer(self.buffer_length, context,
                                                      attributes=self.domain_attributes[domain],
                                                      id_update_frequency=id_update_frequency)
                    self.setup_subscription(context, self.buffers[domain].id_table)
            else:
                self.buffers[domain] = 0

    def setup_subscription(self, domain, id_table):
        """
        Sets up a TraCi subscription for the given IDs and attributes

        Parameters
        ----------
        domain: the label of the domain e.g. 'vehicle'
        id_table: a dictionary containing the IDs and the attributes to collect data for for them e.g.
            id_table = 'car100':[attribute_label_0,attribute_label_1, ...]

        Returns
        -------
        Nothing
        """
        for id in id_table:
            domain.subscribe(id, (id_table[id]))

    # id_table = 'car100':[attribute_label_0,attribute_label_1, ...]
    # also adds to DataBuffer
    def add_subscription(self, domain, id_table, ids=[]):
        """
        Adds a TraCi subscription for the given domain, IDs and attributes

        Parameters
        ----------
        domain: the label of the domain e.g. 'vehicle'
        id_table: a dictionary containing the IDs and the attributes to collect data for for them e.g.
            id_table = 'car100':[attribute_label_0,attribute_label_1, ...]
        ids: a list to specify which IDs within the id_table will be added

        Returns
        -------

        """
        if not ids:
            ids = id_table
        for id in ids:
            try:
                self.context_domains[domain].subscribe(id, self.attribute_to_var_tuple(domain, id_table[id]))
            except:
                print('WARNING:Rolodex::add_subscription: unable to add subscription for {} {}'.format(domain, id))
                import sys
                sys.exit()

    def list_context_domains(self):
        """
        prints the TraCi domains

        Parameters
        ----------
        Nothing

        Returns
        -------
        Nothing

        """
        for context in self.context_domains:
            print('{}:{}'.format(context, context_domains[context]))

    # context_attributes = [(context_domain, contextID, attribute_domain, range, [attributes])]
    # example: [junctionID, tc.CMD_GET_VEHICLE_VARIABLE, 42, [tc.VAR_SPEED, tc.VAR_WAITING_TIME]]
    def setup_context_subscription(self, context_attributes=None):
        """
        Not implemented

        Parameters
        ----------

        Returns
        -------

        """
        for context in context_attributes:
            if context[0] in self.context_domains:
                context_domains[context[0]].subscribe(context[1], context[2], context[3], context[4])
            else:
                print('Error: Invalid Context Domain: {}'.format(context[0]))

    # Ability to set the frequency of updates for each attribute after instantiation
    def set_update_frequency(self, attribute, num_simulation_ticks_between_samples, ids=[]):
        """
        Not implemented

        Parameters
        ----------

        Returns
        -------

        """
        return

    def attribute_to_var_tuple(self, domain, list):
        """
        Used to get the tuple of attributes for establishing a TraCi subscription

        Parameters
        ----------
        domain: the label of the domain e.g. 'vehicle'
        list: the list of attributes e.g. ['lane position', 'lane id', ...]

        Returns
        -------
        A tuple containing the TraCi hex codes for the given attributes

        """
        tp = []
        for item in list:
            tp.append(self.var_dict.get_var(domain, item))
        return tuple(tp)

    def convert_hex_to_attribute(self, domain, data):
        """
        Converts the data returned by a TraCi subscription from hex codes to attribute labels

        Parameters
        ----------
        domain: the label of the domain e.g. 'vehicle'
        data: the data returned by traci.{domain}.getSubscriptionResults()

        Returns
        -------
        A dictionary containing the attribute labels as keys and their data as values

        """
        converted = {}
        for item in data:
            converted[self.var_dict.get_attribute_label(domain, item)] = data[item]
        return converted

    # Update functions
    # Automatically update data at the specified frequency
    # Manually update when requested
    # TODO: Implement frequency schedule updates
    def update_subscription_buffers(self, tick_num, domains=None):
        """
        Updates the subscription buffers

        Parameters
        ----------
        tick_num: the current tick number of the simulation_run_time
        domains: used to specify which domains are updates e.g. ['junction', 'vehicle', ...]

        Returns
        -------
        Nothing

        """
        i = 0
        while i < 2:
            try:
                if not domains:
                    domains = self.context_domains
                for domain in domains:
                    try:
                        buffer = self.buffers[domain]
                        if buffer:
                            if domain == 'vehicle':
                                for arrived in self.vehicles_to_remove:
                                    if self.vehicles_to_remove[arrived] <= tick_num:
                                        buffer.remove_id(arrived)
                                        print('removed {}: {} data'.format(domain, arrived))
                                if buffer.auto_update_attributes:
                                    print('auatts: {}'.format(buffer.auto_update_attributes))
                                    arrived_vehicles = traci.simulation.getArrivedIDList()
                                    if arrived_vehicles:
                                        for arrived in arrived_vehicles:
                                            self.remove_subscription(arrived)
                                            print('removed {}: \'{}\' subscription'.format(domain, arrived))
                                    for arrived in arrived_vehicles:
                                        self.vehicles_to_remove[arrived] = tick_num + self.auto_removal_delay
                                    departed_vehicles = traci.simulation.getDepartedIDList()
                                    auto_attributes = []
                                    for attribute in buffer.auto_update_attributes:
                                        # attributes = [(attribute label, [id list], sampling frequency), ...]
                                        auto_attributes.append(
                                            (attribute, departed_vehicles, buffer.attribute_table[attribute][1]))
                                    buffer.add(auto_attributes, tick_num)
                                    if departed_vehicles:
                                        print(
                                            'Departed vehicles during tick #{}: {}'.format(tick_num, departed_vehicles))
                                        self.add_subscription(domain, buffer.id_table, ids=departed_vehicles)

                            if not buffer.id_table:
                                new_ids = buffer.generate_data_structures(tick_num)
                                if new_ids:
                                    self.add_subscription(domain, buffer.id_table)
                                    print('adding new vehicle ids: {}'.format(new_ids))
                            for id in buffer.id_table:
                                if id not in self.vehicles_to_remove:
                                    # buffer.id_table = {
                                    #   'car100':[(attribute_label,sampling_frequency,simulation_ticks_since_last_update), ...],
                                    #   'car101':[(attribute_label,sampling_frequency,simulation_ticks_since_last_update), ...]
                                    # }
                                    data = self.context_domains[domain].getSubscriptionResults(id)
                                    print('New data for ID {} : {}'.format(id, data))
                                    try:
                                        buffer.update(id, self.convert_hex_to_attribute(domain, data),
                                                      tick_num=tick_num)
                                    except TypeError:
                                        print('id: {}, subscription results: {}'.format(id, data))
                                        # for attribute in id_table[id]:
                                        # if attribute[2] == attribute[1]:#if time to sample, based on sampling frequency
                                        # buffer.update(id, attribute[0], data[vd.get_var(domain, attribute[0])])
                    except KeyError:
                        pass
                i = 3
            except MemoryError as e:
                print(e)
                self.dump_to_file()
                if i == 1:
                    print('UPDATE ABORTED: MEMORY ERROR')
                    return

    def update(self, domain, id_table=[]):
        """
        updates the buffer for the given domain and ids/attributes

        Parameters
        ----------
        domain: the label of the domain e.g. 'vehicle'
        id_table: a dictionary containing the IDs and the attributes to collect data for for them e.g.
            id_table = {
              'car100':[(attribute_label,sampling_frequency,simulation_ticks_since_last_update), ...],
              'car101':[(attribute_label,sampling_frequency,simulation_ticks_since_last_update), ...]
            }

        Returns
        -------

        """
        buffer = self.buffers[domain]
        for id in id_table:
            if id not in buffer.id_table:
                print(
                    '\nWARNING::Rolodex.update: ID: {} not in {} Subscription ID Table, adding the following attribute subscriptions:'.format(
                        id, domain))
                self.add_subscription(domain, {id: id_table[id]})  # VERIFY behavior with customer
            data = self.context_domains[domain].getSubscriptionResults(id)
            for attribute in id_table[id]:
                # if attribute[2] == attribute[1]:#if time to sample, based on sampling frequency
                buffer.update(id, attribute[0], data[vd.get_var(domain, attribute[0])])

    def get_data(self, domains=[]):
        """
        Returns a copy of the data buffers for the given domains

        Parameters
        ----------
        domains: ['vehicle', 'lane', ...]

        Returns
        -------
        data

        """
        data = {}
        for domain in domains:
            data[domain] = self.buffers[domain].buffer.values()
        return data

    def dump_to_file(self, domain=None, dumpfile=None):
        """
        Option to dump buffers to file

        Parameters
        ----------
        domain: can specify the domain to dump e.g. 'vehicle'
        dumpfile: the file handle to write the data to

        Returns
        -------
        Nothing

        """
        if not self.dumpfile:
            self.dumpfile.open('rolodex_dump', 'w')
        if domain:
            self.buffers[domain].dump(dumpfile=dumpfile)
        else:
            for buffer in self.buffers:
                buffer.dump(dumpfile=dumpfile)

    def remove_subscription(self, domain, ids=[]):
        """
        removes a subscription from TraCi

        Parameters
        ----------
        domain: the label of the domain e.g. 'vehicle'
        ids: the list of ids to remove subscriptions for e.g. ['car100', 'car101']

        Returns
        -------

        """
        for id in ids:
            self.context_domains[domain].unsubscribe(id)


if __name__ == '__main__':
    buffers = Rolodex(attributes=attribute_frequency_list)
    # Or initialize without assigning attributes to set up collection of all available attributes. Can set global_sampling_frequency for all attributes/ids, or use default of updating every simulation tick
    buffers = Rolodex(global_sampling_frequency=60)