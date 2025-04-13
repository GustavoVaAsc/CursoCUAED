Nodo buscarEnLista(Lista *lista, char *nombre){
    if(lista->primero == NULL) return NULL;
    
    Nodo *iterador = lista->primero;
    while(iterador!=NULL){
        if(strcmp(iterador->nombre, nombre) == 0) return iterador;
        iterador = iterador->siguiente;
    }
    return NULL;
}