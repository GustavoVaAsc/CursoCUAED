/*

Realizar un programa en lenguaje C que busque la cadena "Estructuras" en un
arreglo de cadenas (arreglo de arreglos de caracteres)

Completar el código con las opciones dadas

1. return -1;
2. "Estructuras",6,cadenas
3. 6
4. strcmp(a_buscar,cadenas[i]) == 0
5. return i;
6. indice != -1
7. char *a_buscar, int tam_arr, char **cadenas

*/

#include <stdio.h>
#include <string.h>

int buscarCadena(char *a_buscar, int tam_arr, char **cadenas); // 7

int main(){
    char *cadenas[6] = {"Datos", "Objetos", "Estructuras", "Algoritmos", "Orientada", "Fundamentos"}; // 3
    int indice = buscarCadena("Estructuras",6,cadenas); // 2

    if(indice != -1){ // 6
        printf("Cadena encontrada en la posicion %d\n",indice);
    }else{
        printf("La cadena no existe en el arreglo\n");
    }

    free(cadenas);
    return 0;
}

int buscarCadena(char *a_buscar, int tam_arr,char **cadenas){
    for(int i=0; i<tam_arr; i++){
        if(strcmp(a_buscar,cadenas[i]) == 0){ // 4
            printf("Cadena encontrada!\n");
            return i; // 5
        }
    }
    return -1; // 1
}