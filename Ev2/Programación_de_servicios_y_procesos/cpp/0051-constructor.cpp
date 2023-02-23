#include <iostream>
using namespace std;

class Persona{
    // Propiedades
    public:
        string nombre;
        int edad;
        Persona(string minombre, int miedad){                  // Constructor - En C++ debe tener el mismo nombre que la clase
            nombre = minombre;
            edad = miedad;
        }
};


int main(){
    
    Persona persona1("Joan", 22);
    cout << persona1.nombre << "\n";

    return 0;
}
