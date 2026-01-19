/*

Escribe un programa en lenguaje C que simule una cola para
un parque de diversiones.

Hay dos tipos de personas que pueden entrar a la cola:
1. Prioritarias (P)
2. Generales (G)

Las personas entran al juego en bloques de 6. 
Siempre se debe priorizar a las personas de tipo  P, pero si no hay suficientes
personas de tipo P, se debe completar el bloque con personas de tipo G.

Imprime el orden en que las personas entran al juego.

1. desencolar(colaNormal, &cliente)
2. !esta_vacia(colaNormal) || !esta_vacia(colaPrioritaria)
3. encolar(colaPrioritaria, cliente)
4. desencolar(colaPrioritaria, &cliente)
5. !esta_vacia(colaNormal)
6. !esta_vacia(colaPrioritaria)
7. colaNormal, cliente
8. inicializar_cola(100)

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define ERROR __INT32_MAX__ // Definición del valor de error

typedef enum boolean { False, True } boolean;

typedef struct Cliente{
    int id_cliente;
    char tipo; 
}Cliente;

// Definición de la estructura de la cola estática
typedef struct ColaEstatica{
    Cliente *datos; // Arreglo para almacenar los elementos de la cola
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
    cola->datos = (Cliente *)malloc(capacidad * sizeof(Cliente));
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
    return cola->final == cola->capacidad-1; 
}

// Función para encolar un elemento
boolean encolar(ColaEstatica *cola, Cliente cliente){
    // Verificar si la cola está llena
    if(esta_llena(cola)){ 
        return False; 
    }

    cola->final = cola->final + 1;
    cola->datos[cola->final] = cliente; // Insertar el nuevo elemento al final
    cola->numElementos++; // Incrementar el número de elementos
    return True; // Éxito
}

// Función para desencolar un elemento
boolean desencolar(ColaEstatica *cola, Cliente *cliente){
    // Verificar si la cola está vacía
    if(esta_vacia(cola)){
        return False; // No se puede desencolar
    }
    // Obtener el valor del frente
    *cliente = cola->datos[cola->frente];
    cola->frente = cola->frente + 1; 
    cola->numElementos--; // Decrementar el número de elementos
    return True; // Éxito
}

// Función para obtener el elemento del frente sin desencolarlo
// Retorna __INT32_MAX__ si la cola está vacía, debido a que es un valor inválido en este contexto
// __INT32_MAX__ = 2147483647
Cliente obtener_frente(ColaEstatica *cola){
    if(esta_vacia(cola)){
        Cliente cliente;
        cliente.id_cliente = ERROR;
        cliente.tipo = '\0';
        return cliente; // Cola vacía
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
    ColaEstatica *colaNormal = inicializar_cola(100); // 8
    ColaEstatica *colaPrioritaria = inicializar_cola(100);

    int idsClientes[] = {4, 2, 13, 25, 7, 34, 8, 19, 27, 3, 11, 5, 17, 9, 1};
    char tiposClientes[] = {'G','P','G','G','P','G','P','G','G','P','G','G','P','G','G'};

    for (int i = 0; i < 15; i++){
        Cliente cliente;
        cliente.id_cliente = idsClientes[i];
        cliente.tipo = tiposClientes[i];
        if(cliente.tipo == 'P'){
            encolar(colaPrioritaria, cliente); // 3
        }else{
            encolar(colaNormal, cliente); // 7
        }
    }

    printf("Orden de entrada al juego:\n");
    int contador = 0;
    while(!esta_vacia(colaNormal) || !esta_vacia(colaPrioritaria)){ // 2
        printf("\nBloque %d:\n", ++contador);
        for(int i=0; i<6; i++){
            Cliente cliente;
            if(!esta_vacia(colaPrioritaria)){ // 6
                desencolar(colaPrioritaria, &cliente); // 4
                printf("Cliente %d (Prioritaria)\n", cliente.id_cliente);
            }else if(!esta_vacia(colaNormal)){ // 5
                desencolar(colaNormal, &cliente); // 1
                printf("Cliente %d (General)\n", cliente.id_cliente);
            }
        }
    }

    liberar_cola(colaNormal); 
    liberar_cola(colaPrioritaria);

    return 0;
}