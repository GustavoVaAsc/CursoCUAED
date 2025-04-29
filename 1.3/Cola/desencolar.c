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