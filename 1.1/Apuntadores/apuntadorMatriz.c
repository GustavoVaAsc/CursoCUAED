#include<stdio.h>

int main(){
   int *ap, indice; // Declaramos un apuntador y un contador
   int nums[3][3] = {{99,88,77},
             {66,55,44},
             {33,22,11}}; // Arreglo multidimensional de 3x3
   ap = *nums; // ap apunta a la referencia de nums (nums[0][0])
   for (indice = 0; indice < 9 ; indice++){ // Se itera hasta 9, porque tenemos 9 posiciones
       if ((indice%3)==0) // Si acabamos de recorrer una fila, damos un salto de linea
           printf("\n");
       printf("%x\t",(ap+indice)); // Imprimimos la direccion de memoria de cada elemento
   }
   return 0;
}
