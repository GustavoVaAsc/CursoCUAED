#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "Cola.c"
#include "inicializar.c"
#include "estaVacia.c"
#include "obtenerFrente.c"
#include "encolar.c"
#include "desencolar.c"

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