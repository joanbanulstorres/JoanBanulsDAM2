function reiniciar(){
    contador_subnivel = 1;
    contador_nivel = 1;
    $("#dimenivel").html(contador_nivel);
    px = px_inicial,
    py = py_inicial,
    arraydados.length = 0;  // Vacía el array
    for(var i=0; i<contador_nivel; i++){
        arraydados[i] = new Dado;
    }
}