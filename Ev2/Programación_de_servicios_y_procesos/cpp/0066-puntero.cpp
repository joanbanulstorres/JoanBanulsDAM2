#include <iostream>
using namespace std;

int main(){
    
    string nombre = "Joan";
    string &referencia = nombre;
    string *puntero = &nombre;                  // puntero: variable que almacena la dirección en la memoria de un valor

    cout << puntero << "\n";
    cout << *puntero << "\n";                   // Para desreferenciar

    return 0;
}
