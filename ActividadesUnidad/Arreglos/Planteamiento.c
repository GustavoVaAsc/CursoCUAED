/*

La empresa de pan dulce Terranela tiene controles de calidad para el peso de 
sus productos. El software de las máquinas que hornean los panes registra el
peso de cada producto en un arreglo. 

Eres el encargado de crear su sistema de filtrado de productos. El sistema
debe tomar el arreglo con los pesos de los productos y determinar cuáles
cumplen con el control de calidad de la empresa. Para esto, te dan dos valores
que representan un umbral (pesoMinimo, pesoMaximo), si un producto tiene un peso
menor al peso mínimo o mayor al peso máximo, este no cumple los estándares.

De igual forma, la empresa te provee el costo de producir cada pan. Calcula el 
total perdido de la empresa (cuánto perdieron por cada pan defectuoso).

Entrada:

En la función panesDefectuosos(), se envían los siguientes parámetros.

int numPanes -> El tamaño los dos arreglos
float pesoPanes[] -> El arreglo con el peso correspondiente a cada pan
float costo -> El costo de producir cada pan

Salida:

En la entrada estándar de C, debes imprimir:

En la primera línea, la cantidad de panes defectuosos (int).
En la segunda línea, el total perdido (float).
En la tercera línea, un arreglo de caracteres con las siguientes condiciones:
    - Debe ser de tamaño numPanes.
    - Solo puede tener dos caracteres.
        - D -> Para panes defectuosos
        - C -> Para panes que cumplen el control de calidad
    - Los caracteres deben estar separados por espacios.

*/