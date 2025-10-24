#include <stdio.h>  
#include <stdlib.h>
#include <limits.h> // Para INT32_MAX

#define ERROR __INT32_MAX__ // Definición del valor de error

typedef enum boolean { False, True } boolean;

// Definición de la estructura de la cola estática
typedef struct ColaEstatica{
    int *datos; // Arreglo para almacenar los elementos de la cola
    int frente; // Índice del frente de la cola
    int final; // Índice del final de la cola
    int numElementos; // Número de elementos en la cola
    int capacidad; // Capacidad máxima de la cola
}ColaEstatica;

// Función para inicializar la cola, devuelve un apuntador a la cola
ColaEstatica* inicializar_cola(int capacidad){
    // Validar capacidad
    if(capacidad <= 0){
        return NULL; // Capacidad inválida
    }
    // Reservar memoria para la cola
    ColaEstatica *cola = (ColaEstatica *)malloc(sizeof(ColaEstatica));
    // Reservar memoria para el arreglo de datos
    cola->datos = (int *)malloc(capacidad * sizeof(int));
    cola->frente = 0; // Inicializar frente
    cola->final = -1; // Inicializar final
    cola->numElementos = 0; // Inicializar número de elementos
    cola->capacidad = capacidad; // Inicializar capacidad
    return cola;
}

// Función para liberar la memoria de la cola
void liberar_cola(ColaEstatica *cola){
    if(cola){ // Verificar que la cola no sea NULL
        free(cola->datos); // Liberar el arreglo de datos
        free(cola); // Liberar la estructura de la cola
    }
}

// Función para comprobar si la cola está vacía
boolean esta_vacia(ColaEstatica *cola){
    // Si el número de elementos es 0, la cola está vacía
    return cola->numElementos == 0;
}

// Función para comprobar si la cola está llena
boolean esta_llena(ColaEstatica *cola){
    // Si el número de elementos es igual a la capacidad, la cola está llena
    return cola->numElementos == cola->capacidad; 
}

// Función para encolar un elemento
boolean encolar(ColaEstatica *cola, int valor){
    // Verificar si la cola está llena
    if(esta_llena(cola)){ 
        return False; 
    }

    // El índice del final se mueve circularmente
    cola->final = (cola->final + 1) % cola->capacidad;
    cola->datos[cola->final] = valor; // Insertar el nuevo elemento al final
    cola->numElementos++; // Incrementar el número de elementos
    return True; // Éxito
}

// Función para desencolar un elemento
boolean desencolar(ColaEstatica *cola){
    // Verificar si la cola está vacía
    if(esta_vacia(cola)){
        return False; // No se puede desencolar
    }
    // Obtener el valor del frente
    int valor = cola->datos[cola->frente];
    cola->frente = (cola->frente + 1) % cola->capacidad; // Mover el frente circularmente
    cola->numElementos--; // Decrementar el número de elementos
    return True; // Éxito
}

// Función para obtener el elemento del frente sin desencolarlo
// Retorna __INT32_MAX__ si la cola está vacía, debido a que es un valor inválido en este contexto
// __INT32_MAX__ = 2147483647
int obtener_frente(ColaEstatica *cola){
    if(esta_vacia(cola)){
        return ERROR; // Cola vacía
    }
    return cola->datos[cola->frente]; // Retornar el elemento del frente
}

// Función para imprimir los elementos de la cola (para propósitos de prueba)
void imprimir_cola(ColaEstatica *cola){
    if(esta_vacia(cola)){ // Verificar si la cola está vacía
        printf("La cola está vacía.\n");
        return;
    }
    // Imprimir los elementos de la cola
    printf("Elementos en la cola: ");
    for (int i = 0; i < cola->numElementos; i++) {
        int indice = (cola->frente + i) % cola->capacidad;
        printf("%d ", cola->datos[indice]);
    }
    printf("\n");
}

int main(){
    ColaEstatica *cola = inicializar_cola(5);
    encolar(cola, 10);
    encolar(cola, 20);
    encolar(cola, 30);
    imprimir_cola(cola);
    int valor = obtener_frente(cola);
    if(desencolar(cola)){
        printf("Desencolado: %d\n", valor);
    }
    imprimir_cola(cola);
    printf("Elemento \"frente\": %d\n", obtener_frente(cola));
    encolar(cola, 40);
    encolar(cola, 50);
    encolar(cola, 60);
    encolar(cola, 70); // Esto debería fallar ya que la cola está llena
    if(!encolar(cola, 80)){
        printf("No se pudo encolar 80, la cola está llena.\n");
    }
    imprimir_cola(cola);
    liberar_cola(cola);
    return 0;
}