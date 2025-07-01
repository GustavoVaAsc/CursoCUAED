/*

Encuentra el error en este programa en lenguaje C
el cual calcula la suma de los elementos de un arreglo hasta el
índice i e indica qué tipo de error es.

a) for(int i=1; i<=10; i++){  -  Error de lógica al incrementar el índice "i" (i++)
b) suma[i] = arr[i]+suma[i-1];  -  Error de lógica al calcular la suma 
c) for(int i=1; i<=10; i++){  -  Error en el límite de acceso al arreglo (i<=10) (Correcta)
d) int arr[10] = {2,3,5,7,11,13,17,19,23,29};  -  Error de sintáxis en la declaración del arreglo

Retroalimentación A: Respuesta incorrecta: El índice del arreglo sí debe incrementarse en 1
Retroalimentación B: Respuesta incorrecta: La suma sí se calcula correctamente
Retroalimentación C: Respuesta correcta: Al intentar acceder al índice i=10, accedemos a una posición que no pertenece al arreglo
Retroalimentación D: Respuesta incorrecta: El arreglo se declara de manera correcta en su forma explícita

*/

#include <stdio.h>

int main(){
    int arr[10] = {2,3,5,7,11,13,17,19,23,29};
    int suma[10];

    suma[0] = arr[0];
    for(int i=1; i<=10; i++){
        suma[i] = arr[i]+suma[i-1];
        printf("Iteracion: %d - Total: %d\n",i, suma[i]);
    }

    return 0;
}