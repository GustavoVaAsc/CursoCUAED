#include<stdio.h>

int main () {

   /*
   Sea el apuntador 
   int *p;

   &p - Accede la direccion de memoria del apuntador
   p - Accede la direccion de memoria de la variable a la que apunta
   *p - Accede al valor de la variable a la que apunta
   
   */
   short a = 5, b = 10; // Variables de tipo entero
   short *apEnt; // Apuntador a entero
   apEnt = &a; // El apuntador guarda la direccion de memoria
   printf("&a = %x\n", &a); // Imprimimos la direccion de memoria de A
   printf("apEnt -> %x\n", apEnt); // Direccion a la que apunta apEnt
   b = *apEnt; // b = 5 (Igualamos al valor de la variable a la que apunta apEnt, usando un "*")
   printf("b = %d\n", b); // Imprimimos el valor de b
   b = *apEnt+1; // b = 6 (Igualamos b al valor de la variable a la que apunta apEnt +1)
   printf("b = %d\n", b); // B ahora vale 6
   *apEnt = 0; // a = 0 (La variable a la que apunta apEnt (a), es modificada mediante el apuntador)
   printf("a = %d\n", a); // Imprimimos el nuevo valor de A

   return 0;
}
