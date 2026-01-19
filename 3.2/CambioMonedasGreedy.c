#include <stdio.h>
#include <stdlib.h>

/*
-----------------------------------------------------------------------------------------
Problema del cambio de monedas utilizando un enfoque voraz (greedy).

Dado un monto y un conjunto de denominaciones de monedas, el objetivo es encontrar la
combinación óptima de monedas que sume el monto dado, utilizando la menor cantidad de
monedas posible.
----------------------------------------------------------------------------------------
*/

/* 

Función para calcular la cantidad mínima de monedas. 

La elección voraz (greedy) se basa en tomar siempre 
la moneda de mayor denominación posible hasta completar el monto.

*/
int cantidadMinimaDeMonedas(int monto, int denominaciones[], int numDenominaciones){
    int contadorMonedas = 0; // Iniciamos el contador de monedas en 0

    // Iteramos sobre las denominaciones de mayor a menor
    for(int i = numDenominaciones - 1; i >= 0; i--){
        // Decrementamos esa denominación mientras el monto sea mayor o igual a la denominación actual
        while(monto >= denominaciones[i]){ 
            monto -= denominaciones[i];
            contadorMonedas++; // Contamos la moneda utilizada
        }
    }
    
    // Si el monto no es 0, significa que no se pudo completar el cambio exacto
    if (contadorMonedas == 0 && monto > 0) return -1;
    return contadorMonedas; // Retornamos la cantidad mínima de monedas
}

int main(){
    int denominaciones[] = {1, 5, 10, 25, 50, 100}; // Denominaciones de monedas disponibles

    // Un caso que falla con el enfoque voraz sería denominaciones[] = {1, 3, 4} y monto = 6

    int numDenominaciones = sizeof(denominaciones) / sizeof(denominaciones[0]);
    int monto = 221; // Monto a cambiar

    // Calculamos la cantidad mínima de monedas necesarias
    int resultado = cantidadMinimaDeMonedas(monto, denominaciones, numDenominaciones);
    if(resultado != -1){
        printf("Cantidad mínima de monedas necesarias: %d\n", resultado);
    }else{
        printf("No es posible hacer el cambio exacto con las denominaciones dadas.\n");
    }

    return 0;
}