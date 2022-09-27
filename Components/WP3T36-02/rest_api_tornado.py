import tornado.ioloop
import tornado.web
import time, json
import psutil

resource = {}
threshold = None

class id_node(tornado.web.RequestHandler):

    # curl GET http://127.0.0.1:8888/LB/id_node
    def get(self):
        global threshold
        ts = threshold
        t1 = time.process_time() #second
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory()[2]
        print("CPU : %s Mem: %s" % (cpu, memory))
        id = None
        dict_id = {}
        if cpu > ts and memory > ts:  # evaluate cpu and memory
            id= self.find_node() #, ip, port
        dict_id['id_node'] = id
        msg_json = json.dumps(dict_id)# find the id_node with less computational load
        t2 = time.process_time() - t1 #second
        print("Time: ", t2*1000, "(ms)\n") # t2*1000 ms
        return self.write(msg_json)

    # function that identifies the node within the array of resources to which
    # delegate the computational load
    def find_node(self):
        global resource
        res = resource
        weight_min = None
        node_id = None

        for elem in res:
            node = res[elem]
            # print(node, elem)
            if 'WEIGTH_Average' == res[elem].keys():
                weight = node['WEIGTH_Average']
            else:
                weight = node['WEIGTH']
            if weight_min == None or weight < weight_min:
                weight_min = weight
                node_id = elem
                #node_ip = node['IP']
                #node_port = node['Port']
                # id = elem

        print(f"The node that will perform the computation is identified with id: {node_id}")
        return node_id #, node_ip, node_port

class rest_api_tornado:

    def __init__(self, ip,  port, threshold):
        self.app = self.make_app()
        self.app.listen(port=port, address=ip)
        self.set_threshold(threshold)

    def make_app(self):
        return tornado.web.Application([(r"/LB/id_node", id_node), ]) # entripoint REST API  (r"/LB",loadbalancer)

    def get_app(self):
        return self.app

    def starts(self):
        return tornado.ioloop.IOLoop.current().start()

    # def get_resource(self):
    #     return resource
    def set_threshold(self, thres):
        global threshold
        threshold = thres
        return True

    def set_resource(self, res):
        global resource
        resource = res
        return True