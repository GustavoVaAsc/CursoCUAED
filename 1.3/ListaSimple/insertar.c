// Función para insertar en una lista ligada simple

void insertar(Lista *lista, char *nombre){
    // Generamos un nuevo nodo con el nombre que queremos insertar
    Nodo *nuevo_nodo = (Nodo *) malloc(sizeof(Nodo)); // Reservamos la memoria necesaria para el nuevo nodo

    if(nuevo_nodo == NULL){ // Error al reservar memoria
        printf("Error al asignar memoria :( \n");
        return;
    }

    nuevo_nodo->nombre = strdup(nombre); // Asignamos nombre al nodo con strdup de string.h
    nuevo_nodo->siguiente = NULL; // Como caso base, el nodo siguiente es NULL

    // Si la lista está vacía
    if(estaVacia(lista)){ 
        nuevo_nodo->id = 1; // Le asignamos el id 1 si la lista está vacía
        lista->primero = nuevo_nodo; // El primer nodo de la lista ahora es el nuevo nodo
        lista->tam++; // Incrementamos el tamaño
    }
    // Caso general de inserción
    else{ 
        /*
        Si queremos que la inserción en una lista ligada tenga una complejidad algorítmica de O(1)
        debemos insertar el nuevo nodo al inicio, debido a que no nos vemos en la necesidad de recorrer
        toda la lista para insertar el nodo, lo que nos tomaría O(n), siendo n el tamaño de la lista.
        */
       nuevo_nodo->id = lista->primero->id+1; // Le asignamos el valor del id anterior + 1
       nuevo_nodo->siguiente = lista->primero; // El siguiente del nodo a insertar es el que era el primero de la lista

       lista->primero = nuevo_nodo; // Nuestro nuevo nodo ahora es el primero en la lista
       lista->tam++; // Aumentamos en 1 el tamaño
    }
}