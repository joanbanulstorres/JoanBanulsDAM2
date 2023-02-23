#include <iostream>
using namespace std;

int main(){
    
    string edad = "22";
    string anyos = "10";
    int suma = stoi(edad) + stoi(anyos);

    cout << to_string(suma);

    return 0;
}
