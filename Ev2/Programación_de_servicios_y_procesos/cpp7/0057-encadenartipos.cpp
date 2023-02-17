#include <iostream>
using namespace std;

int main(){
    
    string nombre = "Joan";
    int edad = 22;

    //cout << nombre + edad;                        // No es posible ya que + se utiliza también para la operación de suma

    cout << nombre + " " + to_string(edad);

    return 0;
}
