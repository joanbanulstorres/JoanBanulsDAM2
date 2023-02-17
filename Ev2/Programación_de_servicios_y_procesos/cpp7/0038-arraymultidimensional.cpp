#include <iostream>
using namespace std;

int main(){
    
    int longitud = 20;
    string agenda[longitud][3];
    
    agenda[0][0] = "Joan";
    agenda[0][1] = "654871255";
    agenda[0][2] = "joan@gmail.com";

    agenda[1][0] = "Lucas";
    agenda[1][1] = "654125448";
    agenda[1][2] = "lucas@gmail.com";

    agenda[2][0] = "Diego";
    agenda[2][1] = "6541977544";
    agenda[2][2] = "diego@gmail.com";

    for(int i=0; i<longitud; i++){
        cout << "Nombre: " << agenda[i][0] << "\tTelefono: " << agenda[i][1] << "\tEmail: " << agenda[i][2] << "\n";
    }

    return 0;  
}
