

void encolar(Cola *cola, char *nombre, char *contenido, char extension[5]){
    Nodo *nuevo_nodo = (Nodo *) malloc(sizeof(Nodo));
    if(nuevo_nodo == NULL){
        printf("Error al asignar memoria :( \n");
        return;
    }

    nuevo_nodo->nombre = strdup(nombre);
    nuevo_nodo->contenido = strdup(contenido);
    strncpy(nuevo_nodo->extension, extension, sizeof(nuevo_nodo->extension));
    nuevo_nodo->extension[4] = '\0'; // Aseguramos terminación nula

    if(estaVacia(cola)){
        cola->frente = nuevo_nodo;
        cola->final = nuevo_nodo;
        nuevo_nodo->siguiente = NULL;
    }else{
        cola->final->siguiente = nuevo_nodo;
        cola->final = nuevo_nodo;
        nuevo_nodo->siguiente = NULL;
    }
    
    cola->tam++;
}