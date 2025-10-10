#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Definición de Nodo y Cola con typedef struct

// Definimos el nodo de la cola usando un typedef struct
typedef struct Nodo Nodo;

// Este nodo simula ser un archivo para una cola de impresión
struct Nodo{
    char *nombre; // Nombre del archivo
    char *contenido; // Contenido del archivo
    char extension[5]; // Extensión del archivo
    Nodo *siguiente; // Apuntador al siguiente nodo en la cola
};

// Definición de la Cola con typedef struct
typedef struct Cola Cola;

struct Cola{
    Nodo *frente; // Apuntador al nodo que va al frente 
    Nodo *final; // Apuntador al final de la cola 
    int tam; // Tamaño de la cola, ya que es dinámica
};

// Función para inicializar la cola
void inicializar(Cola *cola){
    cola->frente = NULL; // El frente de la cola es NULL
    cola->final = NULL; // El final de la cola es NULL 
    cola->tam = 0; // Su tamaño es 0
}

// Función para comprobar si la cola está vacía
int estaVacia(Cola *cola){
    return cola->frente == NULL && cola->final == NULL; // Retornamos el valor evaluado si los apuntadores
}                                                       // frente y final son NULL

// Función para encolar en una cola simple
void encolar(Cola *cola, char *nombre, char *contenido, char extension[5]){
    Nodo *nuevo_nodo = (Nodo *) malloc(sizeof(Nodo)); // Reservamos la memoria para un nuevo nodo
    if(nuevo_nodo == NULL){ // En caso de no poder reservar, salimos de la función
        printf("Error al asignar memoria :( \n");
        return;
    }

    nuevo_nodo->nombre = strdup(nombre); // Copiamos el contenido de la cadena nombre con strdup() de string.h
    nuevo_nodo->contenido = strdup(contenido); // Copiamos el contenido de la cadena contenido con strdup() de string.h
    strncpy(nuevo_nodo->extension, extension, 4); // Copiamos máximo 4 caracteres para la extensión
    nuevo_nodo->extension[4] = '\0'; // Aseguramos terminación nula
    nuevo_nodo->siguiente = NULL; // Al ser una cola, el nodo que insertemos, no tendrá siguiente, ya que este es el último

    // Si la cola está vacía 
    if(estaVacia(cola)){
        cola->frente = nuevo_nodo; // El frente de la cola es el nuevo nodo que generamos
        cola->final = nuevo_nodo; // Al tener solo un elemento, también es el final de la cola
    }else{ // En caso contrario
        cola->final->siguiente = nuevo_nodo;  // El nodo siguiente de nuestro nodo final actual, ahora debe apuntar al nodo a insertar
        cola->final = nuevo_nodo; // El final de la cola ahora es nuestro nodo a insertar
    }
    
    cola->tam++; // Aumentamos en 1 el tamaño
}

// Función para desencolar
void desencolar(Cola *cola){
    // Si está vacía, salimos de la función
    if(estaVacia(cola)){
        printf("La cola esta vacia! \n");
        return;
    }

    // Creamos un apuntador a Nodo que será el que desencolaremos
    Nodo *por_desencolar = cola->frente;  // El nodo a desencolar es igual al frente de la cola
    cola->frente = por_desencolar->siguiente; // El frente de la cola ahora es el siguiente del nodo a desencolar
    // Si después de desencolar no queda ningún nodo
    if (cola->frente == NULL) cola->final = NULL; // Si desencolamos el último nodo, los dos apuntadores de la cola ahora son nulos
    
    // Liberamos la memoria de todo lo que reservamos de forma dinámica
    free(por_desencolar->nombre);
    free(por_desencolar->contenido);
    free(por_desencolar);

    // Reducimos el tamaño de la cola
    cola->tam--;
}

// Función para obtener el frente de la cola
Nodo *obtenerFrente(Cola *cola){ // Retorna un puntero a nodo
    return cola->frente; // Retornamos el nodo que está al frente de la cola
}

// Función principal con ejemplo de uso
int main(){
    Cola q;
    inicializar(&q); // Inicializamos la cola

    // Intentamos desencolar
    desencolar(&q);

    // Encolamos 5 elementos
    encolar(&q,"Tarea_1","El sistema solar es bla bla bla ...","docx");
    encolar(&q,"Factura_PC","Detalles de su compra ...\nRyzen 7 5700G ------ $3,200\nbla bla bla ...","pdf");
    encolar(&q,"gatito","Una imagen de un gatito muy bonito... MIAU","png");
    encolar(&q,"codigoEDA","#include<stdio.h>\n\nint main(){\n\tprintf(\"Hola mundo\");\n\treturn 0;\n}","txt");
    encolar(&q,"maxresdefault","Una foto chistosa de internet","jpg");

    // Imprimimos la cola 

    printf("Mostrando la cola de impresión\n");
    printf("Mostrando la cola de impresión\n");
    printf("Tamaño de la cola %d\n", q.tam);
    Nodo *iterador = q.frente;
    int contador = 0;
    while(iterador != NULL){
        printf("-------------------------------------------------------------------------------\n");
        printf("Nodo %d\n",contador);
        printf("\n");
        printf("%s.%s\n",iterador->nombre,iterador->extension);
        printf("%s\n",iterador->contenido);
        printf("\n");
        printf("-------------------------------------------------------------------------------\n");
        iterador = iterador->siguiente; // Pasamos al siguiente nodo
        contador++;
    }

    printf("\nDesencolamos dos veces\n");

    desencolar(&q);
    desencolar(&q);

    // Obtenemos el frente de la cola
    printf("\n");
    printf("Nuevo frente de cola\n");
    printf("\n");
    iterador = obtenerFrente(&q);

    if(iterador == NULL){
        printf("La cola esta vacia\n");
        return 0;
    }

    printf("-------------------------------------------------------------------------------\n");
    printf("\n");
    printf("%s.%s\n",iterador->nombre,iterador->extension);
    printf("\n");
    printf("%s\n",iterador->contenido);
    printf("\n");
    printf("-------------------------------------------------------------------------------\n");
    printf("\n");

    // Imprimimos de nuevo la cola

    iterador = q.frente;
    contador = 0;
    printf("Mostrando la cola de impresión\n");
    printf("Tamaño de la cola %d\n", q.tam);
    while(iterador != NULL){
        printf("-------------------------------------------------------------------------------\n");
        printf("Nodo %d\n",contador);
        printf("\n");
        printf("%s.%s\n",iterador->nombre,iterador->extension);
        printf("\n");
        printf("%s\n",iterador->contenido);
        printf("\n");
        printf("-------------------------------------------------------------------------------\n");
        iterador = iterador->siguiente;
        contador++;
    }

    return 0;
}
