import json
from preprocessing import Preprocessing
from PIL import Image
import time
import glob
import cv2
import numpy as np
import argparse

class iris_preprocessing():

    def __init__(self, img): #path, ip_api, port_api
        self.img = img
        self.preprocessing = None

    def get_img(self):
        return self.img

    def set_img(self, img):
        self.img = img
        return True

    def init_preprocessing(self, img, img_i):
        self.preprocessing = Preprocessing(img, img_i)
        return True

    def run_preproc(self):
        print("####---- START PREPROCESSING for the image----####")
        t_init = time.time()
        ### Start preprocessing
        self.init_preprocessing(self.img, None)
        img_prep = self.preprocessing.run()
        ret, buffer = cv2.imencode('.jpg', img_prep)
        dict = {}
        dict['img_byte'] = buffer  # buffer, img_prep
        json_msg = json.dumps(dict, cls=NumpyEncoder)

        t_tot = time.time() - t_init
        minute = t_tot / 60  # minuti
        resto = t_tot % 60  # secondi
        print("TOTAL TIME :", t_tot, "s", "(", int(minute), "m", int(resto), "s)")
        return json_msg

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)