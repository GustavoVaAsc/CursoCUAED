void limpiarTransmision(char *mensaje, float costoPorByte) {
    char *lectura = mensaje;
    char *escritura = mensaje;
    int eliminados = 0;

    while (*lectura != '\0') {
        if (*lectura != '#') {
            *escritura = *lectura;
            escritura++;
        } else {
            eliminados++;
        }
        lectura++;
    }

    *escritura = '\0';

    printf("%d\n", eliminados);
    printf("%.2f\n", eliminados * costoPorByte);
    printf("%s\n", mensaje);
}
