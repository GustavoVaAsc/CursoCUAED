// Función para comprobar si la cola está vacía

int estaVacia(Cola *cola){
    return cola->frente == NULL && cola->final == NULL; // Retornamos el valor evaluado si los apuntadores
}                                                       // frente y final son NULL