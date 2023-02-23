#include <iostream>
using namespace std;

int main(){
    
    string nombre = "Joan";
    string &referencia = nombre;

    cout << &nombre << "\n";

    return 0;
}
