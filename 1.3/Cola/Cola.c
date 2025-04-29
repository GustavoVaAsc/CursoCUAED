// Definición de Nodo y Cola con typedef struct

// Definimos el nodo de la cola usando un typedef struct
typedef struct Nodo Nodo;

// Este nodo simula ser un archivo para una cola de impresión
struct Nodo{
    char *nombre; // Nombre del archivo
    char *contenido; // Contenido del archivo
    char extension[5]; // Extensión del archivo
    Nodo *siguiente; // Apuntador al siguiente nodo en la cola
};

// Definición de la Cola con typedef struct
typedef struct Cola Cola;

struct Cola{
    Nodo *frente; // Apuntador al nodo que va al frente 
    Nodo *final; // Apuntador al final de la cola 
    int tam; // Tamaño de la cola, ya que es dinámica
};
