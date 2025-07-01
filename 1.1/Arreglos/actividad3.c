/*

Escribe un programa en lenguaje C que calcule el producto escalar
(producto punto) de dos vectores de R^N (N dimensiones, o tamaño N)

Completa el código con las siguientes opciones:

1. scanf("%lf",&a[i]);
2. 0
3. resultado+=a[i]*b[i];
4. N
5. scanf("%lf",&b[i]);

*/

#include <stdio.h>

int main(){
    int N;
    printf("Ingresa la dimensión o tamaño de los vectores: ");
    scanf("%d",&N);
    double a[N];  // 4
    double b[N]; // 4

    printf("Ingresa el vector A: \n");
    for(int i=0; i<N; i++){
        scanf("%lf",&a[i]); // 1
    }

    printf("Ingresa el vector B: \n");
    for(int i=0; i<N; i++){
        scanf("%lf",&b[i]); //5
    }

    double resultado = 0; // 2
    for(int i=0; i<N; i++){
        resultado+=a[i]*b[i]; // 3
    }

    printf("El resultado del producto escalar es: %.4lf\n",resultado);
}

