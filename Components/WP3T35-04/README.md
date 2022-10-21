# WP3T35-04 Iris Recognition - MODIS Consulting


### Pre-processing
To bring all the images at the same resolution and at a resolution that can could be handled without hardware problema during the training phase, we resized all the image at 500*330 resolution 
For the Pre-processing phase there are 3 operation: 
1. Cropping operation, It is needed to bring the images to a squared shape;
2. Resizing operation, once we have squared images, we can resize them all to the same resolution, that is 456*456;
3. CLAHE (Contrast Limited Adaptive Histrogram Equalization) operation, to enhance the contrast of the raw images. To better highlight some characteristic symptons of DR like, hemorrhages, exudates, cotton wool sposts and microaneurysmsm, we used a hisrogram equalization (HE) technique called CLAHE, that is a HE methodology that resolves the problems of traditional ones. 

### Interfaces 

The Iris Recognition component interfaces with other appications using the following interfaces:

- "IR/image" for REST API: used as entry point to send via POST the bytearray images that you want Pre-processing and to recived the bytearray image pre-processed.

### Requirement 
To use this component, the following requirements are required: 

#### Hardware
- Zynq UltraScale+ ZCU102 or devices with Linux OS;
#### Software
- Libraries: Pillow, scikit-image, opencv-python, numpy, matplotlib, tornado, psutil
- Python3.8+

### Execution 
To execute of the Iris Recognition pre-processing it is necessary to execute "iris_rest_api.py" with the following command 

- python3 iris_rest_api.py -ip_server "<your_IP_server>" -port_server "<your_PORT_server>"

To execute the Load Balancer without necessarily having to install dependencies, it is possibile to build the component in a docker image with dockerfile.
After that it is possible to execute with the following command and parameters can be modified according to needs: 

- sudo docker run --rm -it --network host wp3t35-05-modis-irisrecognition:latest python3 /app/src/iris_rest_api.py -ip_server "<your_IP_server>" -port_server "<your_PORT_server>"
