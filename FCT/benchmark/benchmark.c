#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
#define MAX 100

int main(){
    
    int iteraciones = 10000000;
    
    printf("Cargando...");

    // CÁLCULOS
    
    clock_t tiempo1 = clock();

    double numero = 1.00000000054;

    for(int i=0; i<iteraciones; i++){
        numero *= 1.000000000001;
    }

    tiempo1 = clock() - tiempo1;
    double tiempo_ejecucion1 = ((double)tiempo1)/CLOCKS_PER_SEC;
    printf("\nTiempo de ejecucion: %f s\n", tiempo_ejecucion1);
    printf("\nCargando...");

    // ESCRITURA Y LECTURA

    clock_t tiempo2 = clock();

    FILE *puntero1;
    FILE *puntero2;

    puntero1 = fopen("archivo1.txt", "w+");

    for(int i=0; i<iteraciones; i++){
        fputs("hola\n", puntero1);
    }
    
    puntero2 = fopen("archivo2.txt", "w");

    char line[100];
    
    while(fgets(line, sizeof(puntero1), puntero1)) {
        fputs(line, puntero2); 
    }

    fclose(puntero1);
    fclose(puntero2);

    remove("archivo1.txt");
    remove("archivo2.txt");

    tiempo2 = clock() - tiempo2;
    double tiempo_ejecucion2 = ((double)tiempo2)/CLOCKS_PER_SEC;
    printf("\nTiempo de ejecucion: %f s\n", tiempo_ejecucion2);

    system("pause");

    return 0;
}