// Función para encolar en una cola simple

void encolar(Cola *cola, char *nombre, char *contenido, char extension[5]){
    Nodo *nuevo_nodo = (Nodo *) malloc(sizeof(Nodo)); // Reservamos la memoria para un nuevo nodo
    if(nuevo_nodo == NULL){ // En caso de no poder reservar, salimos de la función
        printf("Error al asignar memoria :( \n");
        return;
    }

    nuevo_nodo->nombre = strdup(nombre); // Copiamos el contenido de la cadena nombre con strdup() de string.h
    nuevo_nodo->contenido = strdup(contenido); // Copiamos el contenido de la cadena contenido con strdup() de string.h
    strncpy(nuevo_nodo->extension, extension, sizeof(nuevo_nodo->extension)); // Al tener un arreglo estático, para la extensión usamos strcpy() de string.h
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