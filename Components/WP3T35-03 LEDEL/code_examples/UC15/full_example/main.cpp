#include <png.h>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <random>
#include "eddl/apis/eddl.h"

png_infop info_ptr;
std::vector<std::vector<std::string> > parsedCsv;

png_bytepp read_png(const char *file_name)
{
    png_bytepp row_pointers;
    FILE *fp = fopen(file_name, "rb");
    png_structp png_ptr = png_create_read_struct(PNG_LIBPNG_VER_STRING, NULL, NULL, NULL);
    info_ptr = png_create_info_struct(png_ptr);  
    png_init_io(png_ptr, fp);
    png_read_png(png_ptr, info_ptr, PNG_TRANSFORM_IDENTITY, NULL);
    row_pointers = png_get_rows(png_ptr, info_ptr);
    png_destroy_read_struct(&png_ptr, NULL, NULL); 
    fclose(fp);
    return row_pointers;
}

void png_rows_to_float_vector(png_bytepp row_pointers, std::vector<float> & vfloat)
{
    vfloat.clear();
    vfloat.reserve(256 * 256);

    for (int i = 0; i < 256; i++) {
        for (int j = 0; j < 256; j++) {
           vfloat.push_back(row_pointers[i][j] / 1.0f);
        }
	free(row_pointers[i]);
    }
    free(row_pointers);
}

Tensor * load_png(const char * file_name)
{
    png_bytepp row_pointers_read = read_png(file_name);
    std::vector<float> vfloat;
    png_rows_to_float_vector(row_pointers_read, vfloat);
    return new Tensor(vfloat, {256, 256});
}

void parseCSV(){
    std::ifstream  data("../data/train.csv");
    std::string line;
    while(std::getline(data,line))
    {
        std::stringstream lineStream(line);
        std::string cell;
        std::vector<std::string> parsedRow;
        while(std::getline(lineStream,cell,','))
        {
            parsedRow.push_back(cell);
        }

        parsedCsv.push_back(parsedRow);
    }
};


// Write png to file function
//void write_png(char *file_name)
//{
//    FILE *fp = fopen(file_name, "wb");
//    png_structp png_ptr = png_create_write_struct(PNG_LIBPNG_VER_STRING, NULL, NULL, NULL);
//    png_init_io(png_ptr, fp);
//    png_set_rows(png_ptr, info_ptr, row_pointers);
//    png_write_png(png_ptr, info_ptr, PNG_TRANSFORM_IDENTITY, NULL);
//    png_destroy_write_struct(&png_ptr, &info_ptr);
//    fclose(fp);
//}

int main(int argc, char *argv[])
{
    //Load dataset CSV
    parseCSV();
    
    std::vector<int> indexes(parsedCsv.size()-1);
    for (int j = 1; j < parsedCsv.size(); j++)
    {
        indexes[j-1] = j;
    }
    
    auto rng = std::default_random_engine {};
    


    // Settings
    int epochs = 1;
    int batch_size = 32;

    // network
    eddl::layer in=eddl::Input({1,256,256});
    eddl::layer l=in;

    // l=Select(l, {"1", "1:31", "1:31"});
    l=eddl::MaxPool2D(eddl::ReLu(eddl::Conv2D(l,32,{3,3},{1,1})),{2,2});
    l=eddl::MaxPool2D(eddl::ReLu(eddl::Conv2D(l,64,{3,3},{1,1})),{2,2});
    l=eddl::MaxPool2D(eddl::ReLu(eddl::Conv2D(l,128,{3,3},{1,1})),{2,2});
    l=eddl::MaxPool2D(eddl::ReLu(eddl::Conv2D(l,256,{3,3},{1,1})),{2,2});

    l=eddl::Reshape(l,{-1});

    l=eddl::Activation(eddl::Dense(l,128),"relu");

    eddl::layer out=eddl::Activation(eddl::Dense(l,1),"sigmoid");

    // net define input and output layers list
    eddl::model net=eddl::Model({in},{out});

        // Build model
    eddl::build(net,
          eddl::sgd(0.01, 0.9), // Optimizer
          {"binary_cross_entropy"}, // Losses
          {"binary_accuracy"}, // Metrics
          //CS_GPU({1}) // one GPU
          //CS_GPU({1,1},100) // two GPU with weight sync every 100 batches
          eddl::CS_CPU()
    );

    for (int e = 1; e <= epochs; e++){

        std::shuffle(std::begin(indexes), std::end(indexes), rng);
        
        eddl::reset_loss(net);

        for (int k = 0; k < indexes.size() / batch_size; k++){

            //Load batches of Tensors
            //Train tensor
            std::vector<Tensor*> tensor_vector_x = {};
            std::vector<float> tensor_vector_y = {};
            
            for (int i = 0; i < batch_size; i++) {
                int index = indexes[(batch_size*k) + i];
                std::string filepath_1 = "../images/"+parsedCsv[index][2];
                Tensor* t1 = load_png(filepath_1.c_str());
                tensor_vector_x.push_back(t1);
                
                //Test tensor
                float label_1 = std::stof(parsedCsv[index][7]);
                tensor_vector_y.push_back(label_1);
            }
            Tensor* x_train = Tensor::stack(tensor_vector_x, 0);
            
            for (int i = 0; i < batch_size; i++) {
                delete tensor_vector_x[i];
            }
            
            Tensor* y_train = new Tensor(tensor_vector_y, {batch_size,1});
            
            //x_train->info();
            //y_train->info();
            
            //x_train->save("tensor.png");
            
            // training, list of input and output tensors, batch, epochs
            eddl::train_batch(net,{x_train},{y_train});
            
            delete x_train;
            delete y_train;
            
            // Get the current losses and metrics
            float curr_loss = eddl::get_losses(net)[0];
            float curr_acc = eddl::get_metrics(net)[0];
            
            std::cout << "\rEpochs: " << e << " Batch: " << k << " Metrics[ loss=" << curr_loss << ", acc=" << curr_acc << " ]  " << std::flush;

        }
    }
    
    
    //write_png(argv[2]);
    return 0;
}

