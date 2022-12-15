# WP3T35-03 LEDEL

LEDEL is a Low-power Energy Deep Learning Library developed to be executed in RISC-V hardware. To achieve this, an alredy existing library based on Artificial Intelligence has been adapated to execute using RISC-V: the EDDL library. EDDL is an open source library for Distributed Deep Learning and Tensor Operations in C++ for CPU, GPU and FPGA. EDDL is developed inside the DeepHealth project and is publicly available from its GitHub [repository](https://github.com/deephealthproject/eddl).

In this component we present some examples of the LEDEL library installed in different emulation images of a RISC-V hardaware.

## Contents

### 1. Docker images

Three Docker images with the tools needed to make use of the LEDEL library have been developed:

  #### 1.1: LEDEL using the Isar RISC-V layer developed by Siemens:
  
  In this first Docker image an emulation of a RISC-V hardware can be run, in which the LEDEL library has been alredy installed. This Docker image allows any user to compile and execute code using the LEDEL library and includes some examples to ilustrate how to do it. The RISC-V emulation image used as foundation in this docker is available in the repository [https://github.com/siemens/isar-riscv](https://github.com/siemens/isar-riscv).
 
This Docker image is available to clone via the following Docker command:
  ```docker pull solverml/ledel:isar_riscv```
  
  #### 1.2: LEDEL using an open source RISC-V emulation:
  
  Same as the previous docker but using an open sourced emulation for the RISC-V hardware. RISC-V emulation image available here [https://people.debian.org/~gio/dqib/](https://people.debian.org/~gio/dqib/)
 
  This Docker image is available to clone via the following Docker command:
  ```docker pull solverml/ledel:artifacts```
  
  #### 1.3: LEDEL cross-compilation:
 
  In this last Docker image a cross-compilator tool has been instaled and configured to compile C++ code aimed to be executed on RISC-V hardware without the need of interacting directly with a RISC-V system.
 
 This Docker image is available to clone via the following Docker command:
  ```docker pull solverml/ledel:cross_compilation```
  
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
  
