#include <iostream>
#include <fstream>          // librería fstream -> para la lectura y escritura de archivos
using namespace std;

int main(){
    
    string linea;
    
    ifstream archivo;
    archivo.open("miarchivo2.txt");
    if(archivo.is_open()){
        while(getline(archivo, linea)){
            cout << linea << "\n";
        }
    }else{
        cout << "El archivo no existe o no se ha podido abrir";
    }
    archivo.close();
    
    return 0;
}
