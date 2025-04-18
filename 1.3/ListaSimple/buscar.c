// Función para buscar en una lista, en este caso por nombre

Nodo *buscar(Lista *lista, char *nombre){ 
    if(lista->primero == NULL) return NULL; // Si la lista está vacía, devolvemos NULL
    
    Nodo *iterador = lista->primero; // Apuntador para iterar la lista

    // Mientras no lleguemos a NULL
    while(iterador!=NULL){
        // Comparamos las cadenas con la funcion strcmp de string.h
        if(strcmp(iterador->nombre, nombre) == 0) return iterador; // Si son iguales, devolvemos el nodo
        iterador = iterador->siguiente; // Pasamos al siguiente
    }
    return NULL; // Si no lo encontramos devolvemos NULL
}