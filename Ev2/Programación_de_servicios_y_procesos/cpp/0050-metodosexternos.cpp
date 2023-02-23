#include <iostream>
using namespace std;

class Persona{
    // Propiedades
    public:
        string nombre;
        int edad;
    // Métodos
    string saluda(){
        string cadena = "Yo me llamo " + nombre + " y te digo hola\n";
        return cadena;
    }
    string buenosDias();
};

// Definición de un método fuera de la clase
string Persona::buenosDias(){
    return "Yo te digo buenos dias";
}

int main(){
    
    Persona persona1;
    persona1.nombre = "Joan";
    persona1.edad = 22;

    Persona persona2;
    persona2.nombre = "Lucas";
    persona2.edad = 19;

    cout << persona1.nombre << "\n";
    cout << persona2.edad << "\n";
    
    cout << persona1.saluda();
    cout << persona2.saluda();
    cout << persona1.buenosDias();

    return 0;
}
