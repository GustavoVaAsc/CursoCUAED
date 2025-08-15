/*

Encuentra el error en este programa en lenguaje C
el cual calcula la transpuesta de una matriz y
selecciona la instrucción que arregla el programa

a) int transpuesta[N][N]; -> int transpuesta[N][N] = matriz;
b) transpuesta[i][i] = matriz[j][j]; -> transpuesta[i][j] = matriz[i][j];
c) scanf("%d",&matriz[i][j]); -> scanf("%d",matriz[i][j]);
d) transpuesta[i][i] = matriz[j][j]; -> transpuesta[i][j] = matriz[j][i]; (Correcta)

Retroalimentación A: Respuesta incorrecta: No se puede inicializar de esa forma la matriz
Retroalimentación B: Respuesta incorrecta: Solo se está copiando la matriz
Retroalimentación C: Respuesta incorrecta: Debemos usar el & para escribir el dato en la dirección de memoria
Retroalimentación D: Respuesta correcta

*/



#include <stdio.h>

int main(){
    int N;
    printf("Ingresa el tamaño de la matriz: ");
    scanf("%d",&N);
    int matriz[N][N];
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            scanf("%d",&matriz[i][j]);
        }
    }

    int transpuesta[N][N];

    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            transpuesta[i][j] = matriz[j][i];
            //transpuesta[i][i] = matriz[j][j];
        }
    }

    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            printf("%d ",transpuesta[i][j]);
        }
        printf("\n");
    }

    return 0;
}