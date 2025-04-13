#include <stdio.h>

char *nombre_mes(int); // Prototipo de funcion, retorna un apuntador a caracter

int main(void){
   char *mes = NULL; // Declaramos un apuntador a caracter inicializado en NULO
   int n; puts("Introduzca el número del mes deseado");
   if (scanf("%d", &n) != 1){ // Si Scanf no recibe con exito el valor, mostramos caracter invalido
       printf("Carácter inválido\n");
       return 0; // Fin del programa
   }
   mes = nombre_mes(n); // Igualamos el apuntador a la funcion que retorna el nombre del mes
   printf("El mes seleccionado es:\n%s\n", mes); // Mostramos el mes en pantalla
   return 0;
}


/* Funcion que genera un arreglo de caracteres (apuntador de apuntadores) */
char *nombre_mes(int numero){
   static char *mes[] = { // Apuntador a arreglo de caracteres (arreglo de arreglos de caracteres)
       "Mes inválido",
       "Enero", "Febrero", "Marzo",
       "Abril", "Mayo", "Junio",
       "Julio", "Agosto", "Septiembre",
       "Octubre", "Noviembre", "Diciembre" }; // Asignacion de valores


    // Evaluamos con condicional ternario, si es correcto, retornamos el indice correspondiente
    // De otra manera retornamos la posicion 0, que contiene el texto "Mes invalido"
   return (numero < 1 || numero > 12) ? mes[0] : mes[numero];
}
