# WP3T36-02 Load Balancer Module - MODIS Consulting

The LB is a software service packed in a docker container able to identify the less busy node in the network able to perform a specific task. For this implementation it is specifically used for the a&g recognition task. This ability falls into the cognitive-awareness capabilities in order to gain quick access to the a&g results when a specific node is over-loaded, and for collaborative purposes.

### Control Flow 
The control flow can be summarized as follows:
1. Configuration of the node (ID, IP, PORT)
2. Configuration of the API REST Tornado Client (IP, PORT)
3. Configuration of the MQTT Client (publish/subscribe on Topic)
4. Evaluate the CPU and Memory parameters
5. Send the useful information, through REST API, to perform the load balancing 

The MQTT Client (use Mosquitto Server) is used for sharing node information, such us: id, ip, cpu, ram memory, and active process. The protocol is lightweight and implements a publish/subscribe communication pattern.

In the Load Balancer procedure the node with the lowers computationa load wll be chosen, threfore with the lowest "average load" parameter.

### Interfaces 

The Load Balancer component interfaces with other appications using the following interfaces:

- "LB/id_node" for REST API: used as entry point to find the node that will perform the computation 
- "LB/reading" for MQTT topic: used to publish the node resources and receive the reaosurces of the other nodes.

### Requirement 
To use this component, the following requirements are required: 

#### Hardware
- Zynq UltraScale+ ZCU102 or devices with Linux OS;
- Device with Linux OS for installing the MQTT Broker (Eclipse Mosquitto Recommended) and connect the target board to it
#### Software
- Libraries: time, threading, json, os, copy, psutil, setuptools, paho-mqtt, tornado
- Python3.8+

### Execution 
At the time of initilization, the following parameters must be specified.

- id, string that indicates the indentification; 
- ip, string that indicates the ip of the node;
- port, int that indicate the REST API server port; 
- ip_broker, string that indicates the IP address of the MQTT broker; 
- topic, string that indicates the topic in which the MQTT client will publish and receive the computational load resouces;
- time, int/float that indicates the time interval between resources published on the topic (every <time> second)
- threshold, int that indicate the maximum threshold in which it is possible to perform the computational load on the node, a hagher value than the threshold will start the load balancing phase. 

To execute the Load Balancer it is necessary to execute "loadbalancer.py" with the following command 

- python3 loadbalancer.py -id "1" -ip "127.0.0.1" -port 8888 -ip_broker "127.0.0.1" -topic "parameters" -time 2 -n_values 3 -threshold 75

To execute the Load Balancer without necessarily having to install dependencies, it is possibile to build the component in a docker image with dockerfile.
After that it is possible to execute with the following command and parameters can be modified 
according to needs: 

- sudo docker run --rm -it --network host wp3t36-02-modis-loadbalancer:latest python3 /app/src/loadbalancer.py -id "1" -ip "127.0.0.1" -ip_api "192.168.0.9" -port_api 8888 -ip_broker "192.168.0.2" -time 2 -n_values 3 -threshold 75
