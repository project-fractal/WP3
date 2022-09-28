#include <cstdio>
#include <cstdlib>
#include <iostream>

#include "eddl/apis/eddl.h"
#include "eddl/serialization/onnx/eddl_onnx.h"

using namespace eddl;

//////////////////////////////////
// mnist_mlp.cpp:
// A very basic MLP for mnist
// Using fit for training
//////////////////////////////////

int main(int argc, char **argv) {
    // Settings
    int epochs = 5;
    int batch_size = 16;
    int num_classes = 1;

    // Define network
    layer in = Input({2000});
    layer l = in;  // Aux var

    l = LeakyReLu(Dense(l, 1024));
    l = LeakyReLu(Dense(l, 1024));
    l = LeakyReLu(Dense(l, 1024));

    layer out = Sigmoid(Dense(l, num_classes));
    model net = Model({in}, {out});
    net->verbosity_level = 0;

    // Build model
    build(net,
          adam(0.01), // Optimizer
          {"binary_cross_entropy"}, // Losses
          {"binary_accuracy"}, // Metrics
          //CS_GPU({1}) // one GPU
          //CS_GPU({1,1},100) // two GPU with weight sync every 100 batches
          CS_CPU()
          //CS_FPGA({1})
    );
    //toGPU(net,{1},100,"low_mem"); // In two gpus, syncronize every 100 batches, low_mem setup

    // View model
    summary(net);

    // Load dataset
    Tensor* x_train = Tensor::load("uc15_dataset/X_train.bin");
    Tensor* y_train = Tensor::load("uc15_dataset/y_train.bin");
    Tensor* x_test = Tensor::load("uc15_dataset/X_test.bin");
    Tensor* y_test = Tensor::load("uc15_dataset/y_test.bin");

    // Preprocessing
    //float x_max = x_train->max();
    //x_train->div_(x_max);
    //x_test->div_(x_max);

    for(int i=0;i<epochs;i++){
        std:cout<<"Epoch "<< i <<std::endl;
        // Train model
        fit(net, {x_train}, {y_train}, batch_size, 1);
        evaluate(net, {x_test}, {y_test}, batch_size);
    }
    save_net_to_onnx_file(net, "uc15_eddl_net.onnx");
    save(net, "uc15_eddl_weights.bin");    
}

