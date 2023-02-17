#include <iostream>
using namespace std;

int main(){
    
    int dia = 9;
    
    switch(dia){
        case 1:
            cout << "Hoy es el peor dia de la semana\n";
        break;
        case 2:
            cout << "Hoy es el segundo peor dia de la semana\n";
        break;
        case 3:
            cout << "Hoy estamos a mitad de semana\n";
        break;
        case 4:
            cout << "Hoy es juernes\n";
        break;
        case 5:
            cout << "Ya se acaba la semana\n";
        break;
        case 6:
            cout << "Hoy es el mejor dia de la semana\n";
        break;
        case 7:
            cout << "Parece mentira que mañana sea lunes\n";
        break;
        default:
            cout << "Lo que has introducido no es un día de la semana\n";
    }

    return 0; 
}
