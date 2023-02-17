#include <iostream>
using namespace std;

int main(){
    
    int edad = 41;
    
    if(edad < 30){
        if(edad < 20){
            cout << "Eres una persona muy joven";
        }else{
            cout << "Eres una persona joven";
        }
    }else{
        if(edad < 40){
            cout << "No eres una persona tan joven";
        }else{
            cout << "No eres una persona joven";
        }
    }

    return 0;    
}
