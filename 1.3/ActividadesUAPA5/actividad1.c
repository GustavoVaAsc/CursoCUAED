/*

Escribe un programa en lenguaje C que utilice una pila estática para
convertir una palabra a un palindromo, agregando caracteres
al final de la palabra original.

Ejemplos:
Entrada: "hola"
Salida: "holaloh"

Entrada: "radar"
Salida: "radaradar"

1. apilar(pila, palabra[i]);
2. char palabra[MAX_LONGITUD];
3. strlen(palabra);
4. palindromo[len] = caracter;
5. PilaEstatica *pila = crear_pila(longitud);
6. strlen(palindromo);
7. strcpy(palindromo, palabra);
8. palindromo[len] = '\0';
9. desapilar(pila, &caracter)
10. liberar_pila(pila);

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LONGITUD 100 // Definición de la longitud máxima de la palabra

typedef enum boolean { False, True } boolean;

typedef struct PilaEstatica{
    char *datos; // Arreglo para almacenar los elementos de la pila
    int cima; // Índice de la cima de la pila
    int capacidad; // Capacidad máxima de la pila
} PilaEstatica;

PilaEstatica* crear_pila(int capacidad){
    PilaEstatica *pila = (PilaEstatica *)malloc(sizeof(PilaEstatica));
    if(!pila) return NULL; // Error al crear la pila
    pila->datos = (char *)malloc(capacidad * sizeof(char));
    if(!pila->datos){
        free(pila);
        return NULL; // Error al crear el arreglo
    }
    pila->cima = -1; // Inicializar la cima
    pila->capacidad = capacidad; // Establecer la capacidad
    return pila;
}

void liberar_pila(PilaEstatica *pila){
    if(pila){
        free(pila->datos); // Liberar el arreglo de datos
        free(pila); // Liberar la estructura de la pila
    }
}

boolean apilar(PilaEstatica *pila, char elemento){
    if(pila->cima == pila->capacidad - 1) return False; // Pila llena
    pila->datos[++pila->cima] = elemento; // Apilar el elemento
    return True;
}

boolean desapilar(PilaEstatica *pila, char *elemento){
    if(pila->cima == -1) return False; // Pila vacía
    *elemento = pila->datos[pila->cima--]; // Desapilar el elemento
    return True;
}


int main(){
    char palabra[MAX_LONGITUD]; // 2
    printf("Ingrese una palabra: "); 
    scanf("%s", palabra);

    int longitud = strlen(palabra); // 3
    PilaEstatica *pila = crear_pila(longitud); // 5
    if(!pila){
        printf("Error al crear la pila.\n");
        return 1;
    }

    // Apilar los caracteres de la palabra
    for(int i = 0; i < longitud; i++){
        apilar(pila, palabra[i]); // 1
    }

    // Construir el palíndromo
    char palindromo[2 * MAX_LONGITUD]; 
    strcpy(palindromo, palabra); // 7

    char caracter;
    while(desapilar(pila, &caracter)){ // 9
        int len = strlen(palindromo); // 6
        palindromo[len] = caracter; // 4
        palindromo[len + 1] = '\0'; // 8
    }

    printf("Palíndromo resultante: %s\n", palindromo);

    liberar_pila(pila); // 10
    return 0;
}
