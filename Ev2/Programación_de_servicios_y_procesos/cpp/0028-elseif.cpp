#include <iostream>
using namespace std;

int main(){
    
    string dia = "mayo";
    
    if(dia == "lunes"){
        cout << "Hoy es el peor dia de la semana\n";
    }else if(dia == "martes"){
        cout << "Hoy es el segundo peor dia de la semana\n";
    }else if(dia == "miercoles"){
        cout << "Hoy estamos a mitad de semana\n";
    }else if(dia == "jueves"){
        cout << "Hoy es juernes\n";
    }else if(dia == "viernes"){
        cout << "Ya se acaba la semana\n";
    }else if(dia == "sabado"){
        cout << "Hoy es el mejor dia de la semana\n";
    }else if(dia == "domingo"){
        cout << "Parece mentira que mañana sea lunes\n";
    }else{
        cout << "Lo que has introducido no es un día de la semana\n";
    }

    return 0; 
}
