#include <iostream>
using namespace std;

string saluda(string nombre){
    return "Hola " + nombre + ", yo te saludo\n";
}

// Sobrecarga de funciones
string saluda(){
    return "Hola, yo te saludo\n";
}
string saluda(string nombre, int edad){
    return "Hola " + nombre + ", tienes " + to_string(edad) + " anyos y yo te saludo\n";
}

int main(){
    
    cout << saluda("Joan");
    cout << saluda("Diego");
    cout << saluda();
    cout << saluda("Lucas", 19);

    return 0;    
}