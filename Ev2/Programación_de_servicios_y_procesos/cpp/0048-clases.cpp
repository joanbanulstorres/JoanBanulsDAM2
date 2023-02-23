#include <iostream>
using namespace std;

class Persona{
    // Propiedades
    public:
        string nombre;
        int edad;
};

int main(){
    
    // Se crea un objeto a partir de la clase
    Persona persona1;
    persona1.nombre = "Joan";
    persona1.edad = 22;

    Persona persona2;
    persona2.nombre = "Lucas";
    persona2.edad = 19;

    cout << persona1.nombre << "\n";
    cout << persona2.edad << "\n";
    
    return 0;
}
