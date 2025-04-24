#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "Lista.c"
#include "inicializar.c"
#include "estaVacia.c"
#include "buscar.c"
#include "insertar.c"
#include "eliminar.c"


int main(){
    Lista l; // Declaramos la lista
    inicializar(&l); // Inicializamos la lista

    if(buscar(&l,"Hola") == NULL) printf("Nodo no encontrado\n"); // Probamos a buscar en una lista vacía

    // Insertamos cinco elementos
    insertar(&l, "Nombre1");
    insertar(&l, "Nombre2");
    insertar(&l, "Nombre3");
    insertar(&l, "Nombre4");
    insertar(&l, "Nombre5");

    // Iteramos la lista
    Nodo *iterador = l.primero;
    while(iterador!=NULL){
        printf("Nombre del nodo: %s\n",iterador->nombre);
        printf("ID del nodo: %d\n",iterador->id);
        iterador = iterador->siguiente;
    }
    printf("\n");

    // Borramos Nombre3;
    eliminar(&l,"Nombre3");

    // Iteramos la lista de nuevo
    iterador = l.primero;
    while(iterador!=NULL){
        printf("Nombre del nodo: %s\n",iterador->nombre);
        printf("ID del nodo: %d\n",iterador->id);
        iterador = iterador->siguiente;
    }
    printf("\n");

    // Buscamos el Nombre2
    Nodo *a_buscar = buscar(&l, "Nombre2");

    // Si el valor retornado no es NULL, lo imprimimos
    if(a_buscar != NULL) printf("Nodo con id %d y nombre %s encontrado!\n",a_buscar->id, a_buscar->nombre);
    else printf("Nodo no encontrado\n");
    return 0;
}