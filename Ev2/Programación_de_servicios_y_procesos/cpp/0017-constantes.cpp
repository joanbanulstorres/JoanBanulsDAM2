#include <iostream>
using namespace std;

int main(){
    
    int edad = 22;
    cout << "Mi edad es " << edad << " años\n";
    edad = 23;
    cout << "Mi edad es " << edad << " años\n";

    const float PI = 3.1416;
    cout << "El valor del número PI es " << PI << "\n";
    PI = 4;                                                           // Da error

    return 0;
}
