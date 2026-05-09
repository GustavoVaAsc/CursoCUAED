void panesDefectuosos(int numPanes, float costo, float pesoPanes[], float pesoMin, float pesoMax) {
    char respuesta[numPanes];
    int cantPanes = 0;
    float costoTotal = 0.0f;
    
    for(int i=0; i<numPanes; i++){
        if(pesoPanes[i] < pesoMin || pesoPanes[i] > pesoMax){
            costoTotal+=costo;
            respuesta[i] = 'D';
            cantPanes++;
        }else{
            respuesta[i] = 'C';
        }
    }
    
    printf("%d\n",cantPanes);
    printf("%.2f\n", costoTotal);
    for(int i=0; i<numPanes; i++){
        printf("%c ",respuesta[i]);
    }
}
