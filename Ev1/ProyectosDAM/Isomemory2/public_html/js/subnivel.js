function subnivel(){
    $("#dimesubnivel").html("Posiciona");
    contador_subnivel++;
    // Asigna nuevas posiciones a los dados
    for(var i=0; i<arraydados.length; i++){
        arraydados[i].dx = tablerox1 + distancia + correccion_dx + (Math.floor(Math.random() * 5)) * distancia;
        arraydados[i].dy = tableroy2 + distancia + correccion_dy + (Math.floor(Math.random() * 5)) * distancia;
    }
    // Manda al robot a su posición inicial
    px = px_inicial,
    py = py_inicial;
}