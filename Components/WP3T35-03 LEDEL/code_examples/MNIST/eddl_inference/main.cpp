#include <cstdio>
#include <cstdlib>
#include <iostream>

#include "eddl/apis/eddl.h"
#include "eddl/serialization/onnx/eddl_onnx.h"

using namespace eddl;


int main(int argc, char **argv) {

    // Download mnist
    download_mnist();
    
    // Load dataset
    Tensor* x_test = Tensor::load("mnist_tsX.bin");
    Tensor* y_test = Tensor::load("mnist_tsY.bin");

    // Preprocessing
    x_test->div_(255.0f);


    // Load net
    Net* net = import_net_from_onnx_file("mnist_eddl_net.onnx");


    // Build model
    build(net,
          rmsprop(0.01), // Optimizer
          {"soft_cross_entropy"}, // Losses
          {"categorical_accuracy"}, // Metrics
          //CS_GPU({1}) // one GPU
          //CS_GPU({1,1},100) // two GPU with weight sync every 100 batches
          CS_CPU(),
          //CS_FPGA({1})
          false //Disable model initialization, since we want to use the onnx weights
    );

    // View model
    summary(net);

    // Evaluate
    evaluate(net, {x_test}, {y_test});
    
    std::remove("mnist_trX.bin");
    std::remove("mnist_trY.bin");
    std::remove("mnist_tsX.bin");
    std::remove("mnist_tsY.bin");
}
