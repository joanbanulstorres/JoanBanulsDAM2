#include <iostream>
using namespace std;

// Las funciones tienen declarse con anterioridad para porder ser llamadas
void saluda(){
    cout << "Yo te saludo";
}

int main(){
    
    saluda();

    return 0;    
}