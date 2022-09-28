#include <cstdio>
#include <cstdlib>
#include <iostream>

#include "eddl/apis/eddl.h"
#include "eddl/serialization/onnx/eddl_onnx.h"

using namespace eddl;


int main(int argc, char **argv) {

    // download CIFAR data
    download_cifar10();

    // Load and preprocess test data
    Tensor* x_test = Tensor::load("cifar_tsX.bin");
    Tensor* y_test = Tensor::load("cifar_tsY.bin");
    x_test->div_(255.0f);

    // Load net
    Net* net = import_net_from_onnx_file("cifar10_eddl_net.onnx");


    // Build model
    build(net,
          sgd(0.01, 0.9), // Optimizer
          {"soft_cross_entropy"}, // Losses
          {"categorical_accuracy"}, // Metrics
          //CS_GPU({1}) // one GPU
          //CS_GPU({1,1},100) // two GPU with weight sync every 100 batches
          CS_CPU(),
          false
    );

    // View model
    summary(net);

    // Evaluate
    evaluate(net, {x_test}, {y_test});
    
    std::remove("cifar_trX.bin");
    std::remove("cifar_trY.bin");
    std::remove("cifar_tsX.bin");
    std::remove("cifar_tsY.bin");
    
}
