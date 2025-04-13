#include <stdio.h>

int main(){
   char c = 'x'; // Variable de tipo caracter
   char *ap; // Variable de tipo apuntador a caracter
   ap = &c; // El apuntador es igual a la direccion de memoria de c

   printf("&c = %x\n", &c); // Imprimimos la direccion de memoria de c
   printf("ap -> %x\n", ap); // Imprimimos el valor del apuntador
   printf("&ap = %x\n", &ap); // Imprimimos la direccion de memoria del apuntador
   return 0;
}
