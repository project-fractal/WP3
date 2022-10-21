from io import BytesIO

import tornado.ioloop
import tornado.web
import argparse
from threading import Thread
import random
import time, json
from PIL import Image
import cv2
import numpy as np
from iris_preprocessing import iris_preprocessing
import psutil

class image(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json')

    def post(self):
        img = json.loads(self.request.body)
        print("Image_byte recived")
        # Image in Bytearray
        image_byte = bytearray(img['img_byte'])
        #print(image_byte)
        stream = BytesIO(image_byte)
        image_new = Image.open(stream) #open image
        #stream.close()
        #print(image_new)
        P = iris_preprocessing(image_new)
        img_preproc = P.run_preproc()
        return self.write(img_preproc)

class rest_api_tornado:

    def __init__(self, ip,  port):
        self.app = self.make_app()
        self.app.listen(port=port, address=ip)

    def make_app(self):
        return tornado.web.Application([(r"/IR/image", image), ]) # entripoint REST API

    def get_app(self):
        return self.app

    def starts(self):
        return tornado.ioloop.IOLoop.current().start()

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

def convert_from_image_to_cv2(img: Image) -> np.ndarray:
# return cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    return np.asarray(img)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-ip_server', '--ip_server', default='127.0.0.1')
    parser.add_argument('-port_server', '--port_server', default=8888)
    args = vars(parser.parse_args())
    #print(args)
    ip_server = args['ip_server']
    port_server = args['port_server']
    print("Connection with ip %s and port %s"%(ip_server, port_server))
    api_rest = rest_api_tornado(ip_server, port_server)
    api_rest.starts()

    time.sleep(3)

