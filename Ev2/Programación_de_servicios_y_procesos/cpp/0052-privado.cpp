#include <iostream>
using namespace std;

class Persona{
    // Propiedades
    public:
        string nombre;
        int edad;
    private:
        double altura;
    public:
        // Setters - Ponedores
        void ponAltura(double alt){
            altura = alt;
        }
        // Getters - Tomadores
        double dameAltura(){
            return altura;
        }
};


int main(){
    
    Persona persona1;
    persona1.nombre = "Joan";
    //persona1.altura = 1.75;
    persona1.ponAltura(1.80);
    cout << persona1.dameAltura();

    return 0;
}
