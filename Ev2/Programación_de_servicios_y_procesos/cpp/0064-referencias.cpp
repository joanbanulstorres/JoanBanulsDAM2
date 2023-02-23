#include <iostream>
using namespace std;

int main(){
    
    string nombre = "Joan";
    string &referencia = nombre;

    cout << referencia << "\n";

    return 0;
}
