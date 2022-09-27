#Deriving the latest base image
FROM python:latest

RUN mkdir -p /app/src

RUN python -m pip install --upgrade pip
RUN pip3 install psutil
#RUN pip3 install threading
#RUN pip3 install json
#RUN pip install os
#RUN pip3 install copy
#RUN pip3 install setuptools
RUN pip3 install paho-mqtt
RUN pip3 install tornado

#Working directory
WORKDIR /app/src

#to copy the remote file at working diectory in container
COPY . /app/src

#CMD instruction used to run the software contained by your image
CMD ["python", "./loadbalancer.py" ]


