/*

Escribe un programa en lenguaje C que sume 1 a todos los
elementos impares de un arreglo usando apuntadores.

Indicación importante: NO USAR LOS ÍNDICES DEL ARREGLO.

Completa el código con las siguientes opciones:

1. p++
2. sizeof(arr)/sizeof(arr[0]);
3. (*p)++
4. (*p)%2
5. arr

*/

#include <stdio.h>

int main(){
    int arr[] = {1,2,4,5,6,18,23,25,28,30};
    int tam = sizeof(arr)/sizeof(arr[0]); // 2
    int *p = arr; // 5

    int *final = arr + tam;

    while(p < final){
        if((*p)%2 == 1){ // 4
            (*p)++; // 3
        }
        p++; // 1
    }

    for(int i=0; i<10; i++){
        printf("%d ",arr[i]);
    }
    printf("\n");

    return 0;
}