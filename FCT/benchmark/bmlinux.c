#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
#define MAX 100

int main(){
    
    printf("Cargando...");

    clock_t tiempo = clock();
    
    int iteraciones = 5000000;
    double numero = 1.000054;

    FILE *puntero1;
    FILE *puntero2;

    puntero1 = fopen("archivo1.txt", "w+");

    for(int i=0; i<iteraciones; i++){
        numero *= 1.000000000001;
        char num[MAX];
        sprintf(num, "%f", numero);
        strcat(num, "\n");
        fputs(num, puntero1);
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

    tiempo = clock() - tiempo;
    double tiempo_ejecucion = ((double)tiempo)/CLOCKS_PER_SEC;

    printf("\nTiempo de ejecucion: %f s\n", tiempo_ejecucion);

    system("pause");

    return 0;
}