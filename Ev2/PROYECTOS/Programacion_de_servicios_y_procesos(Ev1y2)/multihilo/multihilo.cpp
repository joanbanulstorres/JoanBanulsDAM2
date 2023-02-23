#include <iostream>
//#include <filesystem>
#include <fstream>                                                                          // Librería para la lectura y escritura de archivos
#include <thread>                                                                            // Librería para la programación multihilo
#include <string>
using namespace std;
namespace fs = std::filesystem;

// Esta función abre unos archivos especificados y busca si la cadena que se le ha pasado coincide con el texto de alguno de los archivos en algún punto
string buscarTexto(int inicializador, string nombres_archivos[], string linea, string busqueda){
    //cout << "El hilo " << inicializador << " ha encontrado una(s) coincidencia(s):" << endl;
    string resultado = "";
    for(int i=inicializador; i<9; i+=3){
        ifstream archivo;
        archivo.open("archivos/" + nombres_archivos[i]);
        if(archivo.is_open()){
            int contador_linea = 1;
            while(getline(archivo, linea)){
                //cout << linea << endl;
                if(linea.find(busqueda) != string::npos){
                    resultado += "Se ha encontrado una coincidencia en la linea " + to_string(contador_linea) + " del archivo \"" + nombres_archivos[i] + "\"" + "\n";
                }else{
                    //cout << "No se ha encontrado una coincidencia en la linea " << contador_linea << endl;
                }
                contador_linea++; 
            }
        }else{
            cout << "El archivo no existe o no se ha podido abrir";
        }
        archivo.close(); 
    }

    return resultado;

}

int main(){                                                                                 // Hilo principal

    /* // Se sacan los nombres de los archivos contenidos en la carpeta 'archivos' ------- NO ------
    string path = "archivos/";
    for(const auto & entry : fs::directory_iterator(path)){
        cout << entry.path() << std::endl;
    } */

    //////////////////// ▼ VARIABLES GLOBALES ▼ ////////////////////
    string nombres_archivos[] = {
        "Cinco minutos.txt",
        "Final para un cuento fantastico.txt",
        "La elefanta.txt",
        "La intrusa.txt",
        "La obra y el poeta.txt",
        "La pluma.txt",
        "Sobre el abismo del mar.txt",
        "Sueno de la mariposa.txt",
        "Tranvia.txt"
    };
    string linea;
    string busqueda;
    //////////////////// ▲ VARIABLES GLOBALES ▲ ////////////////////

    cout << "Introduce la palabra o frase que deseas buscar: ";
    getline(cin, busqueda);                                                             // Para guardar la cadena con espacios
    
    // Declaración de los hilos "hijos"
    thread hilo0(buscarTexto, 0, nombres_archivos, linea, busqueda);                   
    thread hilo1(buscarTexto, 1, nombres_archivos, linea, busqueda);
    thread hilo2(buscarTexto, 2, nombres_archivos, linea, busqueda);

    // 'join()' -> el hilo principal espera al hilo hijo antes de devolver algo
    //hilo1.join();                                                              
    
    /* 'detach()' -> el hilo principal se desvincula del hilo hijo (no le espera), el cual pasa a ejecutarse en segundo plano (daemon)
    / si el hilo principal es más rápido que le hilo hijo, este último no llega a devolver algo  */ 
    
    // if(hilo0.joinable()){hilo0.join();}
    // if(hilo1.joinable()){hilo1.join();}
    // if(hilo2.joinable()){hilo2.join();} 
    
    cout << buscarTexto(0, nombres_archivos, linea, busqueda);

    return 0;
}