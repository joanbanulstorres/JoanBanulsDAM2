#include <iostream>
using namespace std;

int main(){
    
    int longitud = 20;
    string agenda[longitud];

    agenda[0] = "Carlos";
    agenda[1] = "Camilo";
    agenda[2] = "Calixto";
    agenda[3] = "Cecilia";

    for(string i : agenda){
        cout << "Elemento de la agenda:" << i << "\n";
    }

    return 0;    
}
