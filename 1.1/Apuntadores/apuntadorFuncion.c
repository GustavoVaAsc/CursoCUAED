#include<stdio.h>

int suma(int,int); // Prototipo de funcion suma con dos argumentos


int main(){
   int (*apSuma)(int,int)=&suma; //apSuma apunta a la direccion del prototipo suma
   printf("Dirección memoria suma: %x\n",&suma); 
   printf("Dirección memoria apSuma: %x\n",&apSuma);
   printf("apSuma apunta a: %x\n",*apSuma);
   printf("apSuma(6,4) -> %d\n",apSuma(6,4));
   printf("suma(6,4) -> %d\n",suma(6,4));
}


int suma(int a,int b) {
   return a+b;
}
