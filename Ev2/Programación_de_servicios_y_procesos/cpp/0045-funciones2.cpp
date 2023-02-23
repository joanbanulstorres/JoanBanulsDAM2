#include <iostream>
using namespace std;

// Las funciones tienen declarse con anterioridad para porder ser llamadas
// Forma más limpia
string saluda(){
    return "Yo te saludo";  // Lo que se devuelve realmente es una cadena
}

int main(){
    
    cout << saluda();

    return 0;
}