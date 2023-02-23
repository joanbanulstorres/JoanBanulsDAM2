#include<iostream>
#include<thread>                                                                        // Librería para la programación multihilo
using namespace std;

void miFuncion(){
    cout << "Hola mundo";
}

int main(){                                                                             // Hilo principal

    thread hilo1(miFuncion);                                                            // Hilo "hijo"

    // 'join()' -> el hilo principal espera al hilo hijo antes de devolver algo
    //hilo1.join();                                                              
    
    /* 'detach()' -> el hilo principal se desvincula del hilo hijo (no le espera), el cual pasa a ejecutarse en segundo plano (daemon)
    / si el hilo principal es más rápido que le hilo hijo, este último no llega a devolver algo  */                                                

    return 0;
}