#include <iostream>
using namespace std;

int main(){
    
    int operando1;
    
    operando1 = 5;                                              // Operador de asignacion
    cout << "Ahora el operando vale " << operando1 << "\n";
   
    operando1++;                                                // Operador de incremento
    cout << "Ahora el operando vale " << operando1 << "\n";
    
    operando1--;                                                // Operador de decremento
    cout << "Ahora el operando vale " << operando1 << "\n";
    
    operando1 = operando1 + 5;
    cout << "Ahora el operando vale " << operando1 << "\n";
    
    operando1 += 5;                                             // Operador abreviado de suma
    cout << "Ahora el operando vale " << operando1 << "\n";
    
    operando1 -= 5;                                             // Operador abreviado de resta
    cout << "Ahora el operando vale " << operando1 << "\n";
    
    operando1 *= 5;                                             // Operador abreviado de multiplicación
    cout << "Ahora el operando vale " << operando1 << "\n";
    
    operando1 /= 5;                                             // Operador abreviado de división
    cout << "Ahora el operando vale " << operando1 << "\n";

    return 0;
}
