# -*- coding: utf-8 -*-

"""
    Load Balancer Project

    file: loadbalancer.py

"""

from node import Node
from threading import Thread
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-id', '--id')
    parser.add_argument('-ip', '--ip', default='127.0.0.1')
    parser.add_argument('-ip_api', '--ip_api', default='127.0.0.1')
    parser.add_argument('-port_api', '--port_api', default=8888)
    parser.add_argument('-ip_broker', '--ip_broker', default='localhost')
    parser.add_argument('-mqtt_topic', '--mqtt_topic', default='LB/reading')
    parser.add_argument('-time', '--time', default=2)
    parser.add_argument('-n_values', '--n_values',default='3')
    parser.add_argument('-threshold', '--threshold', default='0')
    args = vars(parser.parse_args())
    print(args)
    id_node = args['id']
    ip = args['ip']
    ip_api = args['ip_api']
    port_api= args['port_api']
    mqtt_topic = args['mqtt_topic']
    ip_broker = args['ip_broker']
    topic = args['mqtt_topic']
    time = float(args['time'])
    n_values = int(args['n_values'])
    threshold = float(args['threshold'])

    node = Node(id_node, ip, ip_api, port_api, ip_broker, mqtt_topic, time, n_values, threshold) #inizializzazione del nodo
    print("Node: ", node.get_id())
    thread_sub = Thread(target=node.get_mqtt_client().client.loop_forever) # thread per l'ascolto sul canale MQTT
    thread_sub.start()
    thread_pub = Thread(target=node.get_mqtt_client().publish_on_topic) # thread per la pubblicazione sul canale MQTT
    thread_pub.start()

    node.get_api().starts()
