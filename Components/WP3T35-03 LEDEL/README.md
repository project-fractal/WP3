# WP3T35-03 LEDEL

LEDEL is a Low-power Energy Deep Learning Library developed to be executed in RISC-V hardware. To achieve this, an alredy existing library based on Artificial Intelligence has been adapated to execute using RISC-V: the EDDL library. EDDL is an open source library for Distributed Deep Learning and Tensor Operations in C++ for CPU, GPU and FPGA. EDDL is developed inside the DeepHealth project and is publicly available from its GitHub [repository](https://github.com/deephealthproject/eddl).

In this component we present some examples of the LEDEL library installed in different emulation images of a RISC-V hardaware.

## Contents

### 1. Docker images

Three docker images with the tools needed to make use of the LEDEL library has been developed:

  #### 1.1: LEDEL using the Isar RISC-V layer developed by Siemens:
  
  In this docker image an emulation of a RISC-V hardware can be run, in which the LEDEL library has been alredy installed. This docker image allows any user to compile and execute code using the LEDEL library and includes some examples to ilustrate how to do it.
 
  Avaliable via:
  ```docker pull solverml/ledel:isar_riscv```
  
  #### 1.2: EDDL cross-compilation Image:
 
  Avaliable via:
  ```docker pull solverml/ledel:cross_compilation```
  
  #### 1.3: EDDL standard compilatio using an open source Image:
 
  Avaliable via:
  ```docker pull solverml/ledel:artifacts```
  
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
  
