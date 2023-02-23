#include <iostream>
using namespace std;

int main(){
    
    int operando1 = 4;
    int operando2 = 3;
    bool comparacion;

    comparacion = operando1 == operando2;
    cout << "Es cierto que el operando1 es igual al operando2? " << comparacion;

    comparacion = operando1 != operando2;
    cout << "\nEs cierto que el operando1 no es igual al operando2? " << comparacion;

    comparacion = operando1 < operando2;
    cout << "\nEs cierto que el operando1 es menor que el operando2? " << comparacion;

    comparacion = operando1 > operando2;
    cout << "\nEs cierto que el operando1 es mayor que el operando2? " << comparacion;

    comparacion = operando1 <= operando2;
    cout << "\nEs cierto que el operando1 es menor o igual al operando2? " << comparacion;

    comparacion = operando1 >= operando2;
    cout << "\nEs cierto que el operando1 es mayor o igual al operando2? " << comparacion;

    return 0;   
}
