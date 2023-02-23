#include <iostream>
using namespace std;

int main(){
    
    string minombre = "Mi nombre es Joan";

    for(int i=0; i<minombre.length(); i++){
        if(i%2 == 0){
            minombre[i] = '*';
        }
    }
    cout << minombre << "\n";
    
    return 0;
}
