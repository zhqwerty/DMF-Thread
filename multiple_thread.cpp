#include <iostream>
#include <vector>
#include <math.h>
#include <random>
#include "simple_random.h"
#include "timer.h"
#include "fvector.h"
#include "examples.h"
#include "tools.h"
#include "global_macros.h"

using namespace std;

void permute(simple_random &rand, int *d, int n) {
  for(int i = n - 1; i > 0; i--) {
    int rand_index = rand.rand_int(i); // pick something [0,i]
    int temp       = d[i];
    d[i]           = d[rand_index];
    d[rand_index]  = temp;    
  }
  VERBOSE_ONLY(for(int i = 0; i < n; i++){cout << i << " -> " << d[i] << endl;})
}

int* init_permutation(int nSize) {
  int *ret = new int[nSize];
  for(int i = nSize - 1; i >= 0; i--) { ret[i] = i; }
  return ret;
}

struct permute_thread_info {
  simple_random &rand; 
  int *r, n;
  permute_thread_info(simple_random &_rand, int* _r, int _n) : rand(_rand), r(_r), n(_n) { } 
};

void* permute_thread( void* p ) {
  struct permute_thread_info *pti = (struct permute_thread_info*) p;
  permute(pti->rand, pti->r, pti->n);
  return NULL;
}

struct gradient_thread_info {
    int id, nWorkers, nTrain;
    FVector *X, *Y;
    Example* ex;
    int* perm;
    int* sample;
    double cur_learning_rate, lambda;
    gradient_thread_info(int _id, int _nWorkers, int _nTrain, 
            FVector* _X, FVector* _Y, Example* _ex, int* _perm, int* _sample,
            double _cur_learning_rate, double _lambda){
        id = _id; nWorkers = _nWorkers; nTrain = _nTrain;
        X = _X; Y = _Y; ex = _ex; perm = _perm; sample = _sample;
        cur_learning_rate = _cur_learning_rate; lambda = _lambda;
    }
};

void* gradient_thread(void* params) {
    struct gradient_thread_info* gti = (struct gradient_thread_info*)(params);
    int id = gti->id;
    int nWorkers = gti->nWorkers;
    int* perm = gti->perm;
    int* sample = gti->sample;
    FVector *X = gti->X;
    FVector *Y = gti->Y;
    struct Example* examples = gti->ex;
    int nTrain = gti->nTrain;
    double cur_learning_rate = gti->cur_learning_rate;
    double lambda = gti->lambda;

    // Calculate offset for examples
    int start_offset = id * (nTrain / nWorkers);
    int end_offset   = min(nTrain, (id + 1) * (nTrain / nWorkers));
    DEBUG_ONLY(cout << "start=" << start_offset << " -- " << end_offset << " " << nExamples << " nWorkers=" << nWorkers << " id=" << id << endl;)

    for (int i = start_offset; i < end_offset; i++){
        // Read example
        int pi = sample[perm[i]];
        int row_index = examples[pi].row;
        int col_index = examples[pi].col;
        double rating = examples[pi].rating;

        // Calculate gradient
        double predict = FVector::dot(X[row_index], Y[col_index]);
        double den = pow(1 + exp(predict * rating), 2); 
        
        FVector gradXi = Y[col_index]; // need to multiply Yj
        gradXi.scale(-exp(rating * predict) * rating / den);
        gradXi.scale_and_add(X[row_index], lambda); 

        X[row_index].scale_and_add(gradXi, -cur_learning_rate);

        FVector gradYj = X[row_index]; // need to multiply by Xi
        gradYj.scale(-exp(rating * predict) * rating / den);
        gradYj.scale_and_add(Y[col_index], lambda);

        Y[col_index].scale_and_add(gradYj, -cur_learning_rate);
    }
    return NULL;
}

int main(int argv, char *argc[]){
    const char* inputFile = "/Users/ZMY/data/Slashdot/slashdot.txt";
    int nRows, nCols, nExamples;
    Example* examples = load_examples(inputFile, nRows, nCols, nExamples);
    
    std::cout << "nRows: " << nRows  << " nCols: " << nCols << " nExamples: " << nExamples << std::endl;
    //for (int i = 0; i < nExamples; i++) std::cout << examples[i].row << " " << examples[i].col << " " << examples[i].rating << std::endl;
    
    int rank = 30;
    int nWorkers = 1;
    double sample_rate = 0.9;
    double lambda = 0.1;
    int nTrain = int(nExamples * sample_rate);
    int nTest = nExamples - nTrain;
    std::cout << "nWorkers: " << nWorkers << std::endl;

    FVector* X = new FVector[nRows];
    FVector* Y = new FVector[nCols];

    int* sample = init_permutation(nExamples);
    simple_random rd;
    permute(rd, sample, nExamples);

    // Variables Update
    int maxEpoch = 50;
    double learning_rate = 0.01;
    double cur_learning_rate = learning_rate;
    std::vector<double> acc;
    std::vector<double> rmse;
     
    std::cout << "Start Training ... " << std::endl;
    timer train_time(true);
    int* shared_perm = init_permutation(nTrain);
    //printVec(shared_perm, nTrain); 
    simple_random rd1;
    struct permute_thread_info* pti = new permute_thread_info(rd1, shared_perm, nTrain);

    gradient_thread_info* wtis[nWorkers];
    for (int i = 0; i < nWorkers; i++){
        wtis[i] = new gradient_thread_info(i, nWorkers, nTrain, X, Y, examples, 
                                            shared_perm, sample, cur_learning_rate, lambda);
    }

    for (int epoch = 0; epoch < maxEpoch; epoch++){
        pthread_t shuffler_t;
        cur_learning_rate = learning_rate * pow(1 + epoch, 0.1);
        int ret = pthread_create( &shuffler_t, NULL, permute_thread, (void*)pti);
        if(ret != 0) { 
            cout << "Error in pthread_create: " << ret << endl;
            exit(-1); 
        }

        pthread_t workers[nWorkers];
        for(int i = 0; i < nWorkers; i++) {
            wtis[i]->perm = pti->r;
            wtis[i]->cur_learning_rate = cur_learning_rate;
            int ret = pthread_create( &workers[i], NULL, gradient_thread, (void*) wtis[i]);
            if(ret != 0) { 
                cout << "Error in pthread_create: " << ret << endl;
                exit(-1); 
            }
        }
        // Thread Join
        for(int i = 0; i < nWorkers; i++) {
            pthread_join(workers[i], NULL);
        }
        pthread_join(shuffler_t, NULL);
        
        // Test Error and Accuracy 
        int trueNum = 0;
        long double error = 0;
        for (int i = nTrain + 1; i < nExamples; i++){
            int pi = sample[i]; 
            int row_index = examples[pi].row;
            int col_index = examples[pi].col;
            double rating = examples[pi].rating;

            double predict = FVector::dot(X[row_index], Y[col_index]);
            if ( sign(predict) == sign(rating) ) trueNum++;
            error += pow(predict - rating, 2);
        }
        acc.push_back(double(trueNum) / nTest);
        rmse.push_back(sqrt(error / nTest));
        train_time.stop();
        printf("Epoch: %d   Accuracy: %.4f  RMSE: %.4f  Spend Time: %.2f s \n", epoch + 1, acc.back(), rmse.back(), train_time.elapsed() ); 
    }

    for (int i = 0; i < nWorkers; i++) delete wtis[i];
    delete shared_perm;
    delete pti;
    delete[] X;
    delete[] Y;
    return 0;
}
