void inicializar(GestorProcesos *g, int cap_inicial) {
    g->cantidad = 0;
    g->capacidad = cap_inicial;
    g->lista = (Proceso *)malloc(cap_inicial * sizeof(Proceso));
}

void agregar_proceso(GestorProcesos *g, int pid, const char *nombre) {
    if (g->cantidad == g->capacidad) {
        int nueva_capacidad = (g->capacidad == 0) ? 1 : g->capacidad * 2;
        
        Proceso *temp = (Proceso *)realloc(g->lista, nueva_capacidad * sizeof(Proceso));
        
        if (temp != NULL) {
            g->lista = temp;
            g->capacidad = nueva_capacidad;
        } else {
            printf("Error: No se pudo asignar memoria.\n");
            return;
        }
    }

    g->lista[g->cantidad].pid = pid;
    strcpy(g->lista[g->cantidad].nombre, nombre);
    g->cantidad++;
}

void matar_proceso(GestorProcesos *g, int pid) {
    int indice = -1;
    
    for (int i = 0; i < g->cantidad; i++) {
        if (g->lista[i].pid == pid) {
            indice = i;
            break;
        }
    }

    if (indice != -1) {
        for (int i = indice; i < g->cantidad - 1; i++) {
            g->lista[i] = g->lista[i + 1];
        }
        g->cantidad--; 
    }
}

void destruir(GestorProcesos *g) {
    if (g->lista != NULL) {
        free(g->lista);
        g->lista = NULL;
    }
    g->cantidad = 0;
    g->capacidad = 0;
}

void imprimirEstado(GestorProcesos *g) {
    for (int i = 0; i < g->cantidad; i++) {
        printf("[%d] PID: %d - %s\n", i, g->lista[i].pid, g->lista[i].nombre);
    }
}

void gestionarProcesos(int n, Operacion ops[]) {
    GestorProcesos gestor;
    gestor.lista = NULL;
    gestor.cantidad = 0;
    gestor.capacidad = 0;

    for (int i = 0; i < n; i++) {
        if (strcmp(ops[i].accion, "INIT") == 0) {
            inicializar(&gestor, ops[i].param_int);
        }
        else if (strcmp(ops[i].accion, "ADD") == 0) {
            agregar_proceso(&gestor, ops[i].param_int, ops[i].param_str);
        }
        else if (strcmp(ops[i].accion, "KILL") == 0) {
            matar_proceso(&gestor, ops[i].param_int);
        }
        else if (strcmp(ops[i].accion, "STATUS") == 0) {
            imprimirEstado(&gestor);
        }
    }

    destruir(&gestor);
}
