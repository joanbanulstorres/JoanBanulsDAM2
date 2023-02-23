#include <iostream>
using namespace std;

int main(){
    
    int operando1 = 4;
    int operando2 = 3;
    int operando3 = 5;
    int operando4 = 5;
    bool comparacion;

    comparacion = operando1 == operando2 && operando3 == operando4;
    cout << "Es cierto que el op1 es igual al op2 y el op3 es igual al op4? " << comparacion;

    comparacion = operando1 == operando2 || operando3 == operando4;
    cout << "\nEs cierto que el op1 es igual al op2 o el op3 es igual al op4? " << comparacion;

    return 0;   
}
