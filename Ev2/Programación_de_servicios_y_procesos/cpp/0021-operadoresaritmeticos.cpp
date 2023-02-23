#include <iostream>
using namespace std;

int main(){
    
    int operando1 = 5;
    int operando2 = 2;

    int suma = operando1 + operando2;
    cout << "La suma entre los operandos es " << suma << "\n";

    int resta = operando1 - operando2;
    cout << "La resta entre los operandos es " << resta << "\n";

    int multiplicacion = operando1 * operando2;
    cout << "La multiplicacion entre los operandos es " << multiplicacion << "\n";

    int division = operando1 / operando2;
    cout << "La division entre los operandos es " << division << "\n";

    float resto = operando1 % operando2;
    cout << "El resto de la division entre los operandos es " << resto << "\n";

    return 0;
}
