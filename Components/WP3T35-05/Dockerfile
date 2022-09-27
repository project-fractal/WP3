#Deriving the latest base image
FROM python:latest

RUN mkdir -p /app/src

RUN python -m pip install --upgrade pip
RUN pip3 install Pillow
RUN pip3 install scikit-image
RUN pip3 install opencv-contrib-python
RUN pip3 install numpy
RUN pip3 install matplotlib
RUN pip3 install tornado
RUN pip3 install psutil
RUN apt update
RUN apt install -y libgl1-mesa-glx


#Working directory
WORKDIR /app/src

#to copy the remote file at working diectory in container
COPY . /app/src

#CMD instruction used to run the software contained by your image
CMD ["python", "./iris_rest_api.py" ]

