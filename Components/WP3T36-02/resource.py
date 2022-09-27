# -*- coding: utf-8 -*-

"""
    Luca Visconti project

    file: resource.py
"""

from copy import copy
from config import *

class Resource:

    def __init__(self, n_values):
        self.n_values = n_values
        self.resource = {}  # dictionary that contains the evaluation matrics
        self.element_resource = {}  # dictionary that contains the past n evaluation metrics to performe Average

    def get_n_values(self):
        return self.n_values

    def getResource(self):
        return self.resource
    
    def getElementResource(self):
        return self.element_resource

    # to update/add the evaluation metric on dictionary
    def add_resource(self, msg_dict):
        n_values = self.get_n_values()
        id = msg_dict['Id_Node']
        #print(id)
        if self.resource.get(id) == None:
            #id = msg_dict['Id_Node']
            self.resource[id] = {}
            self.element_resource[id] = {}
            self.element_resource[id]['Index'] = -1
            self.element_resource[id]['Time_Element'] = []
            self.element_resource[id]['CPU_Element'] = []
            self.element_resource[id]['MEMORY_Element'] = []
            self.element_resource[id]['PROCESSES_Element'] = []

        self.resource[id]['Time'] = msg_dict['Time'] # message time
        self.resource[id]['IP'] = msg_dict['IP'] # ip
        #self.resource[id]['Port'] = msg_dict['Port'] # port
        self.resource[id]['CPU'] = msg_dict['CPU_Usage'] # CPU Usage
        self.resource[id]['MEMORY'] = msg_dict['Memory_Usage'] # Memory RAM usage
        self.resource[id]['PROCESSES'] = msg_dict['Active_Processes'] # number of active process
        self.resource[id]['WEIGTH'] = round((CPU_WEIGTH * msg_dict['CPU_Usage'] + MEMORY_WEIGTH * msg_dict['Memory_Usage'] \
             + PROCESSES_WEIGHT * msg_dict['Active_Processes']) / (len(msg_dict) - 1), 2) #weighted average

        # upgrade of the resource matrix, array circolare
        toadd_index = (self.element_resource[id]['Index'] + 1) % n_values
        if len(self.element_resource[id]['CPU_Element']) == n_values and \
                len(self.element_resource[id]['MEMORY_Element']) == n_values and \
                len(self.element_resource[id]['PROCESSES_Element']) == n_values:
            self.element_resource[id]['Time_Element'].pop(toadd_index)
            self.element_resource[id]['CPU_Element'].pop(toadd_index)
            self.element_resource[id]['MEMORY_Element'].pop(toadd_index)
            self.element_resource[id]['PROCESSES_Element'].pop(toadd_index)

        self.element_resource[id]['Index'] = toadd_index
        self.element_resource[id]['Time_Element'].insert(toadd_index, msg_dict['Time'])
        self.element_resource[id]['CPU_Element'].insert(toadd_index, msg_dict['CPU_Usage'])
        self.element_resource[id]['MEMORY_Element'].insert(toadd_index, msg_dict['Memory_Usage'])
        self.element_resource[id]['PROCESSES_Element'].insert(toadd_index, msg_dict['Active_Processes'])

        # perform the average value (respect to delta time defined)
        if len(self.element_resource[id]['CPU_Element']) == n_values and \
                len(self.element_resource[id]['MEMORY_Element']) == n_values and \
                len(self.element_resource[id]['PROCESSES_Element']) == n_values:
            verify_time = copy(self.element_resource[id]['Time_Element'])
            delta_time = False
            for i in range(0, n_values - 1):
                if (abs(verify_time[i]-verify_time[i+1]) < 200): # the gap between time is less than 200 seconds
                    delta_time = True
                else:
                    delta_time = False
                    i = n_values
            #print(verify_time)
            if delta_time == True:
                cpu_average = round(sum(self.element_resource[id]['CPU_Element']) / n_values, 2)
                memory_average = round(sum(self.element_resource[id]['MEMORY_Element']) / n_values, 2)
                processes_average = round(sum(self.element_resource[id]['PROCESSES_Element']) / n_values, 2)

                self.resource[id]['CPU_Average'] = cpu_average
                self.resource[id]['MEMORY_Average'] = memory_average
                self.resource[id]['PROCESSES_Average'] = processes_average
                self.resource[id]['WEIGTH_Average'] = round(CPU_WEIGTH * cpu_average + MEMORY_WEIGTH * memory_average \
                    + PROCESSES_WEIGHT * processes_average / (len(msg_dict) - 1), 2)

        return True
