#!/usr/bin/env python

import time
from ts_core.execution.Rolodex import Rolodex
    
class OptimizerExample():
    def __init__(self):
        #(context, attribute label, [id list], sampling frequency)
        # attributes = [
            # ('edge','',[],1),
            # ('gui','',[],1),
            # ('induction loop','',[],1),
            # ('junction','',[],1),
            # ('lane','',[],1),
            # ('lane area','',[],1),
            # ('multi-entry-exit detector','',[],1),
            # ('person','',[],1),
            # ('poi','',[],1),
            # ('polygon','',[],1),
            # ('route','',[],1),
            # ('simulation','',[],1),
            # ('traffic light','',[],1),
            # ('vehicle','',[],1),
            # ('vehicle type','',[],1) ]
        self.attributes = [
            ('vehicle','road id',[],1),
            ('vehicle','lane position',[],1),
        ]
        self.rolodex = Rolodex(attributes=self.attributes, buffer_length=10)

    def train(self, tick_num):
        if tick_num > 260:
            time.sleep(0.5)
        self.rolodex.update_subscription_buffers(tick_num)
        print('\n\nVehicle domain buffer data:')#\n{}'.format(self.rolodex.buffers['vehicle'].buffer))
        for vehicle in self.rolodex.buffers['vehicle'].buffer:
            print('Vehicle ID {}:'.format(vehicle))
            for tick in self.rolodex.buffers['vehicle'].buffer[vehicle]:
                print('Simulation tick #{}: {}'.format(tick, self.rolodex.buffers['vehicle'].buffer[vehicle][tick]))
