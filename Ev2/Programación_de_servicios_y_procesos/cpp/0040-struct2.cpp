#include <iostream>
using namespace std;

int main(){
    
    struct registro{
        string nombre;
        int telefono;
        string email;
    };

    registro agenda[20];
    agenda[0].nombre = "Joan";
    agenda[0].telefono = 651245521;
    agenda[0].email = "joan@gmail.com";

    cout << agenda[0].nombre << "\n";

    return 0;  
}
