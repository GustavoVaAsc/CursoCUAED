// Función para eliminar el nodo con el nombre deseado en la lista.

void eliminar(Lista *lista, char *nombre){
    if(lista->primero == NULL){
        printf("La lista está vacía! \n");
        return;
    }

    Nodo *iterador = lista->primero;
    Nodo *anterior = NULL;

    // Buscamos el nodo con el nombre en cuestión
    while(iterador != NULL && strcmp(iterador->nombre,nombre) != 0){
        anterior = iterador;
        iterador = iterador->siguiente;
    }

    // Si no se encontró

    if(iterador == NULL){
        printf("Nodo a eliminar no encontrado! \n");
        return;
    }

    // Si encontramos el nodo

    if(anterior == NULL) lista->primero = iterador->siguiente; // Si es el primer nodo, ahora el primer nodo de la lista es el sucesor del nodo a eliminar
    else anterior->siguiente = iterador->siguiente; // El siguiente del nodo antecesor, ahora es el sucesor del nodo a eliminar

    // Liberamos la memoria del nodo eliminado
    free(iterador->nombre);
    free(iterador);
    lista->tam --; // Reducimos el tamaño de la lista

    printf("Nodo con nombre %s eliminado correctamente! \n",nombre);
}