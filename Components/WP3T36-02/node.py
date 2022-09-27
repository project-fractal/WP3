# -*- coding: utf-8 -*-

"""
    Luca Visconti Project

    file node.py

"""

from mqtt_client import Mqtt_client
from rest_api_tornado import rest_api_tornado


class Node:
    def __init__(self, id_node, ip, ip_api, port_api, ip_broker, mqtt_topic, time, n_values, threshold):
        self.id = id_node # to identify node
        self.ip = ip
        self.api = rest_api_tornado(ip_api, port_api, threshold)
        self.mqtt_client = Mqtt_client(id_node, ip, ip_broker, mqtt_topic, time, n_values, self.api) #self.rest_api
        self.resource = None  # class that contains the evaluation matrix

    def get_id(self):
        return self.id

    def get_mqtt_client(self):
        return self.mqtt_client
    
    def get_api(self):
        return self.api

    def set_resource(self):
        self.resource = self.get_mqtt_client().get_resource().getResource()
        return True

    def get_resource(self):
        return self.resource

