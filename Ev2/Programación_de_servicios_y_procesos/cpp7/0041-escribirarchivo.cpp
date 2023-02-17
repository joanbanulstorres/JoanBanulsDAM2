#include <iostream>
#include <fstream>          // librería 'fstream' -> para la lectura y escritura de archivos
using namespace std;

int main(){
    
    ofstream archivo;                                                                   // Abre un archivo para escribir en el mismo
    
    archivo.open("miarchivo.txt");
    archivo << "Hola archivo\nEsta es mi primera linea\nEsta es mi segunda linea";
    archivo.close();
    
    return 0;   
}
