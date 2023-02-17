#include <iostream>
#include <fstream>          // librería 'fstream' -> para la lectura y escritura de archivos
using namespace std;

int main(){
    
    string linea;
    
    ifstream archivo;
    
    archivo.open("miarchivo.txt");
    while(getline(archivo, linea)){
        cout << linea << "\n";
    }
    archivo.close();
    
    return 0;
}
