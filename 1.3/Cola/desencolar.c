

void desencolar(Cola *cola){
    if(estaVacia(cola)){
        printf("La cola esta vacia! \n");
        return;
    }

    Nodo *por_desencolar = cola->frente;
    cola->frente = por_desencolar->siguiente;

    // Si después de desencolar no queda ningún nodo
    if (cola->frente == NULL) cola->final = NULL;
    

    free(por_desencolar->nombre);
    free(por_desencolar->contenido);
    free(por_desencolar);

}