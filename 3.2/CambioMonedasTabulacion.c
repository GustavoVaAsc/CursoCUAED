#include <stdio.h>
#include <stdlib.h>
#include <limits.h> // Para INT_MAX

/*
-----------------------------------------------------------------------------------------
Problema del cambio de monedas utilizando un enfoque de programación dinámica con tabulación.

Dado un monto y un conjunto de denominaciones de monedas, el objetivo es encontrar la
combinación óptima de monedas que sume el monto dado, utilizando la menor cantidad de
monedas posible.
----------------------------------------------------------------------------------------
*/

#define INFINITO INT_MAX // Definición de un valor alto para representar infinito
#define MAX_MONTO 10000 // Definición del monto máximo permitido

int cantidadMinimaDeMonedas(int monto, int denominaciones[], int numDenominaciones){


    /*

    Podemos ver el acceso a nuestra tabla como una función, nuestra función recibe
    el monto y devuelve la cantidad mínima de monedas necesarias para ese monto.

    f(monto) = monedasMinimas[monto]

    La tabla se irá construyendo de manera ascendente, desde el monto 0 hasta el monto objetivo.

    */
    int monedasMinimas[MAX_MONTO + 1];

    // Inicializamos la tabla
    for(int i = 0; i <= monto; i++){
        monedasMinimas[i] = INFINITO; // Inicialmente, todos los montos son inalcanzables
    }
    // Caso base: 0 monedas son necesarias para el monto 0
    monedasMinimas[0] = 0;

    // Proceso de llenado de la tabla
    for(int i = 1; i <= monto; i++){ // Para cada monto desde 1 hasta el monto objetivo
        for(int j = 0; j < numDenominaciones; j++){ // Para cada denominación de moneda
            // Si la denominación es menor o igual al monto actual
            if(denominaciones[j] <= i){ 
                // Verificamos si usar esta moneda mejora la solución
                // Es decir, si la solución para (monto - denominación) es alcanzable
                int subProblema = monedasMinimas[i - denominaciones[j]];
                // Si el subproblema es alcanzable y mejora la solución actual, actualizamos el valor
                if(subProblema != INFINITO && subProblema + 1 < monedasMinimas[i]){
                    monedasMinimas[i] = subProblema + 1; // Actualizamos la tabla con la mejor solución encontrada
                }
            }
        }
    }
    if(monedasMinimas[monto] == INFINITO){
        return -1; // No es posible hacer el cambio exacto
    }
    return monedasMinimas[monto];
}

int main(){
    int denominaciones[] = {1,3,4}; // Denominaciones de monedas disponibles
    int numDenominaciones = sizeof(denominaciones) / sizeof(denominaciones[0]);
    int monto = 6; // Monto a cambiar

    // Calculamos la cantidad mínima de monedas necesarias
    int resultado = cantidadMinimaDeMonedas(monto, denominaciones, numDenominaciones);
    if(resultado != -1){
        printf("Cantidad mínima de monedas necesarias: %d\n", resultado);
    }else{
        printf("No es posible hacer el cambio exacto con las denominaciones dadas.\n");
    }

    return 0;
}