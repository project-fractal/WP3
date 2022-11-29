# WP3T35-03 LEDEL

Component explanation

## Index

### 1. Docker images

Two docker images with the tools needed to execute and compile EDDL code are available:

  #### 1.1: EDDL standard compilation Image:
 
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
  
