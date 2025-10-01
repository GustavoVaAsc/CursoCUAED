/*

Sea el siguiente struct de C que representa una pelicula:

struct Pelicula{
    char titulo[50];
    int anioEstreno;
    char clasificacion[6];
    struct Pelicula *siguiente;
};

Realizar un programa en lenguaje C que encadene todas las peliculas de rapidos y furiosos
en orden cronológico mediante su apuntador "siguiente" y las imprima en pantalla.

Lista de peliculas:

1. The Fast and the Furious (2001) - R
2. 2 Fast 2 Furious (2003) - PG-13
3. The Fast and the Furious: Tokyo Drift (2006) - PG-13
4. Fast & Furious (2009) - PG-13
5. Fast Five (2011) - PG-13
6. Fast & Furious 6 (2013) - PG-13
7. Furious 7 (2015) - PG-13
8. The Fate of the Furious (2017) - PG-13
9. F9 (2021) - PG-13
10. Fast X (2023) - PG-13

Relaciona el código con los siguientes puntos:

1. Pelicula **inicio, char titulos[10][50], int anios[10], char clasificaciones[10][6]
2. (Pelicula*) malloc(sizeof(Pelicula))
3. actual->siguiente = nuevaPelicula
4. *inicio = nuevaPelicula
5. Pelicula *actual = NULL
6. while(actual != NULL)
7. actual = nuevaPelicula
8. strcpy(nuevaPelicula->clasificacion, clasificaciones[i])
9. actual = actual->siguiente;
10. actual = nuevaPelicula

*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct Pelicula{
    char titulo[50];
    int anioEstreno;
    char clasificacion[6];
    struct Pelicula *siguiente;
} Pelicula;

void crearLista(Pelicula **inicio, char titulos[10][50], int anios[10], char clasificaciones[10][6]){ // 1
    Pelicula *actual = NULL; // 5
    for(int i=0; i<10; i++){
        Pelicula *nuevaPelicula = (Pelicula*) malloc(sizeof(Pelicula)); // 2
        strcpy(nuevaPelicula->titulo, titulos[i]);
        nuevaPelicula->anioEstreno = anios[i];
        strcpy(nuevaPelicula->clasificacion, clasificaciones[i]); // 8
        nuevaPelicula->siguiente = NULL;
        if(*inicio == NULL){
            *inicio = nuevaPelicula; // 4
            actual = nuevaPelicula; // 7
        }else{
            actual->siguiente = nuevaPelicula; // 3
            actual = nuevaPelicula; // 10
        }
    }
}

void mostrarLista(Pelicula *inicio){
    Pelicula *actual = inicio;
    while(actual != NULL){ // 6
        printf("%s (%d) - %s\n", actual->titulo, actual->anioEstreno, actual->clasificacion);
        actual = actual->siguiente; // 9
    }
}

int main(){
    char titulos[10][50] = {
        "The Fast and the Furious",
        "2 Fast 2 Furious",
        "The Fast and the Furious: Tokyo Drift",
        "Fast & Furious",
        "Fast Five",
        "Fast & Furious 6",
        "Furious 7",
        "The Fate of the Furious",
        "F9",
        "Fast X"
    };

    int anios[10] = {2001, 2003, 2006, 2009, 2011, 2013, 2015, 2017, 2021, 2023};
    char clasificaciones[10][6] = {"R", "PG-13", "PG-13", "PG-13", "PG-13", "PG-13", "PG-13", "PG-13", "PG-13", "PG-13"};

    Pelicula *inicio = NULL;

    crearLista(&inicio, titulos, anios, clasificaciones);
    mostrarLista(inicio);

    return 0;
}