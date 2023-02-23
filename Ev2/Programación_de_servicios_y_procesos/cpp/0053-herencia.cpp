#include <iostream>
using namespace std;

class Animal{
    public:
        string seMueve(){
            return "Este animal se mueve\n";
        }
};

class Mamifero: public Animal{
    public:
        string mama(){
            return "Este animal mama cuando es pequeno\n";
        }
};

class Gato: public Mamifero{
    // Propiedades
    public:
        string nombre;
        int edad;
        string maulla(){
            return "El gato esta maullando\n";
        }
};

int main(){
    
    Gato gato1;
    cout << gato1.maulla();
    cout << gato1.mama();
    cout << gato1.seMueve();

    return 0;
}
