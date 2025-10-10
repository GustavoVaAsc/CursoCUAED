#include <stdio.h>  
#include <stdlib.h>

typedef struct ColaEstatica {
    int *datos;
    int frente;
    int final;
    int numElementos;
    int capacidad;
} ColaEstatica;

ColaEstatica* inicializar_cola(int capacidad){
    ColaEstatica *cola = (ColaEstatica *)malloc(sizeof(ColaEstatica));
    cola->datos = (int *)malloc(capacidad * sizeof(int));
    cola->frente = 0;
    cola->final = -1;
    cola->numElementos = 0;
    cola->capacidad = capacidad;
    return cola;
}

void liberar_cola(ColaEstatica *cola){
    if (cola) {
        free(cola->datos);
        free(cola);
    }
}

int esta_vacia(ColaEstatica *cola){
    return cola->numElementos == 0;
}

int esta_llena(ColaEstatica *cola){
    return cola->numElementos == cola->capacidad;
}

int encolar(ColaEstatica *cola, int valor){
    if (esta_llena(cola)) {
        return 0; 
    }
    cola->final = (cola->final + 1) % cola->capacidad;
    cola->datos[cola->final] = valor;
    cola->numElementos++;
    return 1; // Éxito
}

int desencolar(ColaEstatica *cola, int *valor){
    if (esta_vacia(cola)) {
        return 0; 
    }
    *valor = cola->datos[cola->frente];
    cola->frente = (cola->frente + 1) % cola->capacidad;
    cola->numElementos--;
    return 1; // Éxito
}

int obtener_frente(ColaEstatica *cola, int *valor){
    if (esta_vacia(cola)) {
        return 0; 
    }
    *valor = cola->datos[cola->frente];
    return 1; // Éxito
}

int main(){
    return 0;
}