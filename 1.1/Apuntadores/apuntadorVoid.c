#include <stdio.h>

void ver(void *, int); // Prototipo de funcion que recibe apuntador void

int main() {
   char a='b'; //Variable de tipo caracter
   int x=3; // Variable de tipo entero
   double y=4.5; // Variable de tipo real double
   char *cad="hola"; // Apuntador de caracteres (cadena)
   ver(&a, 0); // Enviamos la direccion de memoria de a como parametro a la funcion.
   ver(&x, 2); // Enviamos la direccion de memoria de x como parametro a la funcion.
   ver(&y, 1); // Enviamos la direccion de memoria de y como parametro a la funcion.
   ver(cad, 3); // Enviamos la referencia en memoria de cad como parametro a la funcion
   getchar(); // Esperamos un caracter
   return 0;
}


void ver( void *p, int d) {
   switch(d) { // Condicional
       case 0:
            // Casteamos el apuntador de void a caracter y mostramos el valor
            // de la direccion a la que apunta
           printf("%c\n",*(char *)p); 
           break;
       case 1:
            // Casteamos el apuntador de void a double y mostramos el valor
            // de la direccion a la que apunta
           printf("%d\n",*(double *)p);
           break;
       case 2:
            // Casteamos el apuntador de void a entero y mostramos el valor
            // de la direccion a la que apunta
           printf("%ld\n",*(int *)p);
           break;
       case 3:
            // Casteamos el apuntador de void a apuntador a caracter y mostramos el valor
            // de la direccion a la que apunta
           printf("%s\n",(char *)p);
           break;
       default:
           printf("Error "); // En caso de recibir un dato erroneo
   }
}
