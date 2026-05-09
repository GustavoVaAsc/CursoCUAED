void procesarConsultas(int numRegistros, Perfil usuarios[], int numConsultas, Consulta consultas[]) {
    int indiceActual = -1;

    for (int i = 0; i < numConsultas; i++) {
        if (strcmp(consultas[i].tipo, "SELECT") == 0) {
            indiceActual = atoi(consultas[i].valor);
        }
        else if (strcmp(consultas[i].tipo, "MODIFY") == 0 && indiceActual >= 0 && indiceActual < numRegistros) {
            if (strcmp(consultas[i].campo, "username") == 0) {
                strcpy(usuarios[indiceActual].nombreUsuario, consultas[i].valor);
            }
            else if (strcmp(consultas[i].campo, "email") == 0) {
                strcpy(usuarios[indiceActual].correo, consultas[i].valor);
            }
            else if (strcmp(consultas[i].campo, "new_post") == 0) {
                usuarios[indiceActual].publicaciones++;
            }
            else if (strcmp(consultas[i].campo, "password") == 0) {
                if (strcmp(usuarios[indiceActual].contrasena, consultas[i].valor) == 0) {
                    printf("Error: Usuario %s, esa ya es tu contraseña\n", usuarios[indiceActual].nombreUsuario);
                } else {
                    strcpy(usuarios[indiceActual].contrasena, consultas[i].valor);
                }
            }
        }
    }

    for (int i = 0; i < numRegistros; i++) {
        printf("[%d] %s - %s - %s - %d posts\n", 
            i, usuarios[i].nombreUsuario, usuarios[i].correo, usuarios[i].contrasena, usuarios[i].publicaciones);
    }
}
