# INSTRUCTIONS OF USE

Here are detailed the steps necessary to use the tools included in the Docker image to execute and compile LEDEL code.

## 1. Docker installation

The Docker image can be cloned into any device with the command:
```docker pull solverml/ledel:cross_compilation```

Once cloned, we can run the image as a container by executing the command:
```docker run -t -d solverml/ledel:cross_compilation /bin/bash```

To access the Docker container from a terminal run the following command:
```docker exec -i -t container_id /bin/bash``` where 'container_id' needs to be replaced by the ID assign to the Docker container we have just created. To check this ID simply run the command ```docker ps```. This will keep open a terminal allowing to execute commands as a root user inside the docker container.

## 2. Cross-compiling LEDEL code

In this docker container is possible to cross-compile programs since the cross-compiling tools are already installed. 

To show how to do this, included with the Docker container there is a code example using the MNIST dataset in the folder ```/home/eddl_examples/cifar10_eddl_cross_train```. Along with the code there is also a CMakeLists.txt file we can use to cross-compile this code. Instead of using CMake to compile the code using the default compiler of the system we need to specify the C++ compiler in the CMake command. For example, to cross-compile the code available in ```/home/eddl_examples/cifar10_eddl_cross_train``` move to the folder and execute this commands on the terminal:
1. ```mkdir build```
2. ```cd build```
3. ```cmake .. -DCMAKE_CXX_COMPILER="/home/isar-riscv/sdk/sdk-debian-sid-ports-riscv64/usr/bin/riscv64-linux-gnu-g++"```
4. ```make```

This will generate and executable file compiled for a RISC-V system. Transferring the file to a RISC-V emulation like the ones available in the other dockers on this repository should be enough to execute it without any more modifications.
