"""
    Luca Visconti Project

    On Terminal:
        > sudo systemctl start mosquitto
        > sudo systemctl status mosquitto

        > mosquitto_pub -h localhost -t parameters -m "Id Node: 1, CPU Usage: 35%, Memory Usage: 1.7, Active processes: 60"
        > mosquitto_pub -h localhost -t parameters -m "Id Node: 2, CPU Usage: 65%, Memory Usage: 2.3, Active processes: 100"

"""

import json
import os
import psutil
import time
from paho.mqtt.client import Client
from resource import Resource

PUBLISH = True

class Mqtt_client:

    def __init__(self, id, ip, ip_broker, topic, time, n_values, api):
        self.id = id #to identify the node client
        self.ip = ip #to identify the node ip
        #self.port = port
        self.ip_broker = ip_broker
        self.topic = topic
        self.time = time
        self.client = Client(client_id=id) # to manage the connection with broker
        self.connect = self.init_connect()
        self.subscribe = self.init_subscribe()
        self.resource = Resource(n_values) # class that contains the evaluation matrics
        self.api = api
        #print(self.api)

    def get_resource(self):
        return self.resource

    def get_api(self):
        return self.api

    def get_ip_broker(self):
        return self.ip_broker

    def get_topic(self):
        return self.topic

    def get_time(self):
        return self.time

    # to initialize the MQTT connection
    def init_connect(self):
        def on_connect(client, userdata, flag, rc): # callback on_connect
            if rc == 0:
                print("Connect to MQTT Broker")
            else:
                print ("Failed to connect, return code %d\n", rc)
        # Set Connecting Client ID
        client = self.client
        client.on_connect = on_connect # evento di callback
        client.connect(self.get_ip_broker()) # to connect to the Broker

    #to initialize the subscription on topic
    def init_subscribe(self):
        def on_message(client, userdata, msg): #callback on_message
            message = msg.payload.decode()
            dict_resource = json.loads(message)
            if dict_resource['Id_Node'] != self.id:
                print("Message Received: ", dict_resource)
                self.add_resource(dict_resource)
        client = self.client
        client.subscribe(self.get_topic())
        client.on_message = on_message # evento di callback

    # to publish a string message on topic
    def publish_on_topic(self):
        while PUBLISH == True:
            pids = 0
            for subdir in os.listdir('/proc'):
                if subdir.isdigit():
                    pids += 1
            dict_payload = {}
            dict_payload['Id_Node'] = self.id
            dict_payload['IP'] = self.ip
            #dict_payload['Port'] = self.port
            dict_payload['Time'] = time.time()
            dict_payload['CPU_Usage'] = psutil.cpu_percent()
            dict_payload['Memory_Usage'] = psutil.virtual_memory()[2]
            dict_payload['Active_Processes'] = pids
            msg_json = json.dumps(dict_payload)
            #print("Message Sent: ", msg_json)
            self.client.publish(topic=self.get_topic(), payload=msg_json)
            time.sleep(self.get_time())
        return True

    # to update/add the evaluation metric on dictionary
    def add_resource(self, msg_filtered):
        self.resource.add_resource(msg_filtered)
        self.get_api().set_resource(self.get_resource().getResource())
        #print("Resource Matrix: ", self.resource.getResource())
        return True
