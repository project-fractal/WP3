# INSTRUCTIONS OF USE

Here are detailed the steps necessary to use the tools included in the Docker image to execute and compile LEDEL code.

## 1. Docker installation

The Docker image can be cloned into any device with the command:
```docker pull solverml/ledel:ros2_with_eddl```

Once cloned, we can run the image as a container by executing the command:
```docker run -t -d solverml/ledel:ros2_with_eddl /bin/bash```

To access the Docker container from a terminal run the following command:
```docker exec -i -t container_id /bin/bash``` where 'container_id' needs to be replaced by the ID assign to the Docker container we have just created. To check this ID simply run the command ```docker ps```. This will keep open a terminal allowing to execute commands as a root user inside the docker container.

## 2. Running ROS2 on the RISC-V emulation

Starting from the terminal to the container and then moving to the directory ```/isar-riscv``` will show the files necessary to run the RISC-V emulation, as well as a shellscript file which will initiate the emulation.

To start the emulation run the following command: ```sh run_qemu.sh```. Once the startup of the emulation is complete it will prompt us to introduce a user and password. Type 'riscv' in both to access the RISC-V system.

The terminal then will change its focus from the container to the RISC-V emulation, where its possible to run and compile code using the LEDEL library since it's already been installed.

## 3. Compiling and running LEDEL code

In the RISC-V emulation provided here is possible to compile C++ code using the LEDEL library by writing a ```CMakeList.txt``` file along with the main code of a program and using the ```cmake``` command.

## 4. Useful emulation commands

### 4.1 File transfer

To test custom code it may be necessary to transfer files in and out of the RISC-V emulation. It's possible to do this using ssh commands. The IP corresponding  the host machine running the Docker container is visible to the RISC-V emulation as 127.17.0.1, so by executing a command similar to ```scp {host_user}@172.17.0.1 {path_in_host} {path_in_emulation}``` is possible to transfer a file from the host machine to the emulation. Inverting the paths is possible to transfer a file from the emulation to the host. 

### 4.2 Emulation state commands

Since QEMU has been used to create the emulation its possible to type special commands that will affect the state of the emulation by typing ```Ctrl + A, C```. For example:
- By default, when closing the emulation all changes made to it will be lost. To commit those changes before exiting the emulation use the special QEMU command ```commit all```.
- To stop the emulation use the command ```quit```
- The full list of QEMU commands can be found here [https://en.wikibooks.org/wiki/QEMU/Monitor](https://en.wikibooks.org/wiki/QEMU/Monitor).


