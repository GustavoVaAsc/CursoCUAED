/*

Realizar un programa en lenguaje C que cuente la cantidad de productos que tienen
una A en cualquier posición de su atributo "código".

La entrada del programa será un arreglo de struct Producto, definido de la siguiente
manera:

struct Producto{
    int cantidad;
    char codigo[5];
    float precio;
};

Completar el código con las opciones dadas

1. if(strchr(productos[i].codigo, 'A') != NULL)
2. cantidadA++;
3. 0
4. 7

Pregunta adicional:

¿Cómo podrías contar las A sin usar la función strchr()?

a. Revisar la posición 0 de cada código de producto.
b. Usar otro bucle for para iterar sobre el codigo de cada producto y revisar si tiene una A
c. Revisar la posición 5 de cada código de producto.
d. Hacer un condicional por cada posición de la cadena


*/

#include <stdio.h>
#include <string.h>

typedef struct Producto Producto;

struct Producto{
    int cantidad;
    char codigo[5];
    float precio;
};


int main(){
    Producto productos[7] = {
        {10, "A123", 15.5},
        {5, "B4U6", 25.99},
        {8, "C7U9", 30.15},
        {12, "CA12", 20.19},
        {7, "A345", 10.99},
        {3, "D678", 5.49},
        {9, "E9A0", 12.75}
    };

    int cantidadA = 0; // 3

    for(int i=0; i<7; i++){ // 4
        if(strchr(productos[i].codigo, 'A') != NULL){ // 1
            cantidadA++; // 2
        }
    }

    printf("La cantidad de productos los cuales su código contiene una A es: %d\n", cantidadA);
    return 0;
}
