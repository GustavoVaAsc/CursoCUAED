#include<stdio.h>

int main () {
   short arr[5], *apArr; // Declaramos el arreglo y un apuntador de entero
   apArr = &arr[0]; // apArr apunta a la posicion 0 del arreglo
   printf("%x\n",arr); // Imprimimos la referencia del arreglo en memoria (Se encuentra en la posicion 0)
   printf("%x\n",apArr); // apArr apunta a la referencia del arreglo en memoria
   return 0;
}
