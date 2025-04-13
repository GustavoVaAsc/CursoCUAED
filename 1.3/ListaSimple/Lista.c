// Nodo de una lista ligada simple usando typedef struct
typedef struct{
    int id; // Identificador
    char *nombre; // Nombre como dato
    Nodo *siguiente; // Apuntador al siguiente nodo
}Nodo;

// Definimos la lista
typedef struct{
    Nodo *primero; // Primer nodo, también llamado cabeza
    int tam // Tamaño actual de la lista
}Lista;