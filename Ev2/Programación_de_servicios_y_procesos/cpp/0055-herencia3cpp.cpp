#include <iostream>
using namespace std;

class Mamifero{
    public:
        string mama(){
            return "Este animal mama cuando es pequeno\n";
        }
        string grita(){
            return "Este animal esta gritando\n";
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
        string grita(){                                 // Sobreescribe el método de la clase madre
            return "Este gato esta gritando\n";
        }
};

int main(){
    
    Gato gato1;
    cout << gato1.maulla();
    cout << gato1.grita();

    return 0;
}
