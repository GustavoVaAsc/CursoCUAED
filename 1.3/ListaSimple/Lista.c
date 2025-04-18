// Nodo de una lista ligada simple usando typedef struct
typedef struct Nodo Nodo;

struct Nodo{
    int id; // Identificador
    char *nombre; // Nombre como dato
    Nodo *siguiente; // Apuntador al siguiente nodo
};

// Definimos la lista
typedef struct Lista Lista;
struct Lista{
    Nodo *primero; // Primer nodo, también llamado cabeza
    int tam; // Tamaño actual de la lista
};