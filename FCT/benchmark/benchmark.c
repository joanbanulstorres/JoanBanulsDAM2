#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define MAX 100

int main(){
    
    int iteraciones = 10000000;

    // CÁLCULOS - PROCESADOR

    printf("Cargando...\n");
    
    clock_t tiempo1 = clock();

    double numero = 1.00000000054;
    for(int i=0; i<iteraciones; i++){
        numero *= 1.000000000001;
    }

    tiempo1 = clock() - tiempo1;
    double tiempo_ejecucion1 = ((double)tiempo1)/CLOCKS_PER_SEC;
    printf("\nTiempo de ejecucion (procesador): %f s\n", tiempo_ejecucion1);

    // ESCRITURA Y LECTURA - DISCO DURO

    printf("\nCargando...\n");

    clock_t tiempo2 = clock();

    FILE *puntero1;
    FILE *puntero2;

    // Escritura en el archivo 1
    puntero1 = fopen("archivo1.txt", "w+");
    for(int i=0; i<iteraciones; i++){
        fputs("hola\n", puntero1);
    }
    
    // Lectura del archivo 1 y escritura de su contenido en el archivo 2
    puntero2 = fopen("archivo2.txt", "w");
    char linea[100];
    while(fgets(linea, sizeof(puntero1), puntero1)) {
        fputs(linea, puntero2); 
    }
    fclose(puntero1);
    fclose(puntero2);

    // Se borran los archivos
    remove("archivo1.txt");
    remove("archivo2.txt");

    tiempo2 = clock() - tiempo2;
    double tiempo_ejecucion2 = ((double)tiempo2)/CLOCKS_PER_SEC;
    printf("\nTiempo de ejecucion (disco duro): %f s\n\n", tiempo_ejecucion2);

    system("pause");

    return 0;
}