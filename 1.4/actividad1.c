/*

Escriba un programa en lenguaje C que, utilizando las funciones de memoria dinámica, 
cree un arreglo dinámico de enteros el cual pueda ser de cualquier tamaño y permita agregar 
elementos al final del mismo.

1.- *arreglo == NULL
2.- *tamaño++
3.- !agregar_elemento(&arreglo, &n, nuevoElemento)
4.- (int*) malloc(tamaño * sizeof(int))
5.- *arreglo = nuevo_arreglo
6.- (int*) realloc(*arreglo, (*tamaño + 1) * sizeof(int))
7.- !inicializar_arreglo(&arreglo, n)
8.- int **arreglo, int *tamaño, int nuevo_elemento
9 .- !agregar_elemento(&arreglo, &n, -2)
10.- free(arreglo)

*/

#include <stdio.h>
#include <stdlib.h>

typedef enum boolean {False, True} boolean;

boolean inicializar_arreglo(int **arreglo, int tamaño){
    *arreglo = (int*) malloc(tamaño * sizeof(int)); // 4
    if(*arreglo == NULL){ // 1
        printf("Error en la asignación de memoria\n");
        return False;
    }
    return True;
}

boolean agregar_elemento(int **arreglo, int *tamaño, int nuevo_elemento){ // 8
    int *nuevo_arreglo = (int*) realloc(*arreglo, (*tamaño + 1) * sizeof(int)); // 6
    if(nuevo_arreglo == NULL){
        printf("Error en la reasignación de memoria\n");
        return False;
    }
    *arreglo = nuevo_arreglo; // 5
    (*arreglo)[*tamaño] = nuevo_elemento;
    (*tamaño)++; // 2
    return True;
}

int main(){
    int n;
    printf("Ingrese el tamaño del arreglo: ");
    scanf("%d", &n);

    int *arreglo;
    if(!inicializar_arreglo(&arreglo, n)){ // 7
        return 1;
    }

    for(int i=0; i<n; i++){
        printf("Ingrese el elemento %d: ", i+1);
        scanf("%d", &arreglo[i]);
    }

    printf("El arreglo ingresado es:\n");
    for(int i=0; i<n; i++){
        printf("%d ", arreglo[i]);
    }
    printf("\n");

    int nuevoElemento;
    printf("Ingrese un nuevo elemento para insertar al final del arreglo: ");
    scanf("%d", &nuevoElemento);

    int *nuevoArreglo;

    if(!agregar_elemento(&arreglo, &n, nuevoElemento)){ // 3
        free(arreglo);
        return 1;
    }

    printf("Ahora vamos a agregar otro elemento, el número -2.\n");

    if(!agregar_elemento(&arreglo, &n, -2)){ // 9
        free(arreglo);
        return 1;
    }

    printf("El arreglo actualizado es:\n");
    for(int i=0; i<n; i++){
        printf("%d ", arreglo[i]);
    }
    printf("\n");

    free(arreglo); // 10
    return 0;
}