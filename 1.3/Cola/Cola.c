typedef struct Nodo Nodo;

struct Nodo{
    char *nombre;
    char *contenido;
    char extension[5];
    Nodo *siguiente;
};

typedef struct Cola Cola;

struct Cola{
    Nodo *frente;
    Nodo *final;
    int tam;
};
