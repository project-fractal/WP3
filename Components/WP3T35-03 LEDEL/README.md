# WP3T35-03 LEDEL

LEDEL is a Low-power Energy Deep Learning Library developed to be executed in RISC-V hardware. To achieve this, an already existing library based on Artificial Intelligence has been adapated to execute using RISC-V: the EDDL library. EDDL is an open source library for Distributed Deep Learning and Tensor Operations in C++ for CPU, GPU and FPGA. EDDL is developed inside the DeepHealth project and is publicly available from its GitHub [repository](https://github.com/deephealthproject/eddl).

In this component we present some examples of the LEDEL library installed in different emulation images of a RISC-V hardware.

## Contents

### 1. Docker images

Three Docker images with the tools needed to make use of the LEDEL library have been developed:

  #### 1.1: LEDEL using the Isar RISC-V layer developed by Siemens:
  
  In this first Docker image an emulation of a RISC-V hardware can be run, in which the LEDEL library has been already installed. This Docker image allows any user to compile and execute code using the LEDEL library and includes some examples to illustrate how to do it. The RISC-V emulation image used as foundation in this docker is available in the repository [https://github.com/siemens/isar-riscv](https://github.com/siemens/isar-riscv).
 
  **Specific instructions about how to install and use this Docker can be found [here](https://github.com/project-fractal/WP3/blob/main/Components/WP3T35-03%20LEDEL/docker_use/isar_riscv/README.md). And a video demonstrating how to make use of this Docker image is available in this [link](https://ikerlan.sharepoint.com/:v:/r/sites/FRACTAL_project/Documentos%20compartidos/WP9%20-%20Exploitation,%20Dissemination,%20Training%20,%20Stan/Training/Training%20videos/LEDEL_component_training_video.mp4?csf=1&web=1&e=CNHQNy).**
 
This Docker image is available to clone via the following Docker command:
  ```docker pull solverml/ledel:isar_riscv```
  
  #### 1.2: LEDEL using an open source RISC-V emulation:
  
  Same as the previous docker but using an open sourced emulation for the RISC-V hardware. RISC-V emulation image available here [https://people.debian.org/~gio/dqib/](https://people.debian.org/~gio/dqib/)

  **Specific instructions about how to install and use this Docker can be found [here](https://github.com/project-fractal/WP3/tree/main/Components/WP3T35-03%20LEDEL/docker_use/open_source_riscv/README.md).**

  This Docker image is available to clone via the following Docker command:
  ```docker pull solverml/ledel:artifacts```
  
  #### 1.3: LEDEL cross-compilation:
 
  In this Docker image a cross-compilator tool has been installed and configured to compile C++ code aimed to be executed on RISC-V hardware without the need of interacting directly with a RISC-V system.
 
**Specific instructions about how to install and use this Docker can be found [here]( https://github.com/project-fractal/WP3/tree/main/Components/WP3T35-03%20LEDEL/docker_use/cross_compilation_tool/README.md).** 
 
 This Docker image is available to clone via the following Docker command:
  ```docker pull solverml/ledel:cross_compilation```

  #### 1.4: LEDEL using ROS2 ond RISC-V:
  
  This docker image adds ROS2 on top of the Isar RISC-V layer from Siemens. The instructions followed to build this emulation can be found in the Siemens repository: [https://github.com/siemens/isar-riscv/blob/main/doc/ROS2.md](https://github.com/siemens/isar-riscv/blob/main/doc/ROS2.md).
 
  **Specific instructions about how to install and use this Docker can be found [here](docker_use/ros2/README.md)**
  
### 2. Code Examples

  Various examples of use of the EDDL functions applied to different datasets
  
  #### 2.1. MNIST
  - [Neural Network train and export to ONNX with EDDL](https://github.com/project-fractal/WP3/tree/main/Components/WP3T35-03%20LEDEL/code_examples/MNIST/eddl_training)
  - [Neural Network inference with EDDL](https://github.com/project-fractal/WP3/tree/main/Components/WP3T35-03%20LEDEL/code_examples/MNIST/eddl_inference)
  - [Neural Network train and export to ONNX with PyTorch](https://github.com/project-fractal/WP3/tree/main/Components/WP3T35-03%20LEDEL/code_examples/MNIST/pytorch_training)
  
  #### 2.2. CIFAR10
  - [Neural Network train and export to ONNX with EDDL](https://github.com/project-fractal/WP3/tree/main/Components/WP3T35-03%20LEDEL/code_examples/CIFAR10/eddl_train)
  - [Neural Network inference with EDDL](https://github.com/project-fractal/WP3/tree/main/Components/WP3T35-03%20LEDEL/code_examples/CIFAR10/eddl_inference)
  - [Neural Network train and export to ONNX with PyTorch](https://github.com/project-fractal/WP3/tree/main/Components/WP3T35-03%20LEDEL/code_examples/CIFAR10/pytorch_train)
  
  #### 2.3. UC15
  - [Full execution using simplified dataset](https://github.com/project-fractal/WP3/tree/main/Components/WP3T35-03%20LEDEL/code_examples/UC15/reduced_example)
  - [Full execution using full dataset](https://github.com/project-fractal/WP3/tree/main/Components/WP3T35-03%20LEDEL/code_examples/UC15/full_example)

  ##  Acknowledgement
This project has received funding from the Key Digital Technologies Joint Undertaking (KDT JU) under grant agreement No 877056. The JU receives support from the European Union’s Horizon 2020 research and innovation programme and Spain, Italy, Austria, Germany, Finland, Switzerland.

![FRACTAL Logo](https://cloud.hipert.unimore.it/apps/files_sharing/publicpreview/jHmgbEb2QJoe8WY?x=1912&y=617&a=true&file=fractal_logo_2.png&scalingup=0)

![EU Logo](https://cloud.hipert.unimore.it/apps/files_sharing/publicpreview/pessWNfeqBfYi3o?x=1912&y=617&a=true&file=eu_logo.png&scalingup=0)
![KDT Logo](https://cloud.hipert.unimore.it/apps/files_sharing/publicpreview/yd7FgKisNgtLPTy?x=1912&y=617&a=true&file=kdt_logo.png&scalingup=0)   
