#include <iostream>
#include <fstream>
#include <string.h>                                                     // Para 'strcpy'
using namespace std;

// Defino los datos con los que voy a trabajar

int cursor = 0;                                                         // Para saber en qué posición está la agenda
int longitud = 100;                                                     // Longitud de la agenda

struct registro{                                                        // Estructura para el registro
    string nombre;
    string telefono;
    string email;
};

// Definición del array agenda
registro agenda[100];

string opcion;

void menu(){
    // Menú inicial 
    cout << "Programa agenda v.001\n";
    cout << "Escoge una opcion\n";
    cout << "1.- Introducir un registro\n";
    cout << "2.- Listar registros\n";
    cout << "3.- Salir del programa\n";
    cout << "4.- Guardar la agenda\n";
    cin >> opcion;                                                          // Se solicita una entrada al usuario
    cout << "Has elegido la opcion: " << opcion << "\n";
    if(opcion == "1"){
        cout << "Vamos a insertar un nuevo registro en la agenda\n";
        
        cout << "Introduce el nombre de la persona: ";
        string nombre;
        cin >> nombre;

        cout << "Introduce el telefono de la persona: ";
        string telefono;
        cin >> telefono;
        
        cout << "Introduce el email de la persona: ";
        string email;
        cin >> email;

        cout << "Voy a introducir: " << nombre << ", " << telefono << ", " << email << "\n";
        agenda[cursor].nombre = nombre;
        agenda[cursor].telefono = telefono;
        agenda[cursor].email = email;
        cursor++;

        cout << "Registro en la agenda:\n";
        for(int i=0; i<cursor; i++){
            cout << agenda[i].nombre << ", " << agenda[i].telefono << ", " << agenda[i].email << "\n";
        }
        cout << "\n\n\n";

    }else if(opcion == "2"){
        cout << "LISTA DE REGISTROS DE LA AGENDA\n";
        for(int i=0; i<cursor; i++){
            cout << agenda[i].nombre << ", " << agenda[i].telefono << ", " << agenda[i].email << "\n";
        }
        cout << "\n\n\n";
    }else if(opcion == "3"){
        cout << "HAS SALIDO DEL PROGRAMA";
        cout << "\n\n\n";
        exit(0);                                                                // Se sale del programa
    }else if(opcion == "4"){
        ofstream archivo;
        archivo.open("agenda.txt");
        for(int i=0; i<cursor; i++){
            string cadena = agenda[i].nombre + ", " + agenda[i].telefono + ", " + agenda[i].email + "\n";
            archivo << cadena;
        }
        archivo.close();
    }

    menu();

}

int main(){

    // Se cargan los registros previamente guardados
    string linea;
    ifstream archivo;
    archivo.open("agenda.txt");
    while(getline(archivo, linea)){
        char micadena[100];
        strcpy(micadena, linea.c_str());
        char *ptr;
        ptr = strtok(micadena, ",");
        int contador = 0;
        while(ptr != NULL){
            if(contador == 0){
                agenda[cursor].nombre = ptr;
            }else if(contador == 1){
                agenda[cursor].telefono = ptr;
            }else if(contador == 2){
                agenda[cursor].email = ptr;
            }
            contador++;
            ptr = strtok(NULL, ", ");
        }
        cursor++;
    }
    archivo.close();

    system("cls");                                                              // Limpia la consola - "cls" en Windows, "clear" en UNIX/LINUX

    menu();

    return 0;    
}