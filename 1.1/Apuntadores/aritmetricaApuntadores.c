#include<stdio.h>

int main () {
   short arr[5] = {91,28,73,46,55}; // Arreglo
   short *apArr; // Se declara un apuntador
   apArr = arr; // Apunta a la referencia en memoria del arreglo
   printf("%i\n",*apArr); // Imprime el valor al que apunta (primer elemento)
   printf("%i\n",*(apArr+1)); // Imprime el valor al que apunta la siguiente direccion de memoria
   printf("%i\n",*(apArr+2)); // Imprime el valor al que apunta con dos direcciones de memoria por delante
   return 0;
}
