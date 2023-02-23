#include <iostream>
using namespace std;

int main(){
    
    struct{
        string nombre;
        int telefono;
        string email;
    }registro1, registro2;

    registro1.nombre = "Joan";
    registro1.telefono = 654128445;
    registro1.email = "joan@gmail.com";

    cout << registro1.nombre << "\n";

    return 0;  
}
