function subnivel(){
    $("#dimesubnivel").html("Posiciona");
    contador_subnivel++;
    // Asigna nuevas posiciones a los dados
    for(var i=0; i<arraydados.length; i++){
        arraydados[i].dx = tablerox1 + (Math.floor(Math.random() * 9)) * 45 + correccion_dx;
        arraydados[i].dy = tableroy2 + (Math.floor(Math.random() * 9)) * 45 + correccion_dy;
    }
    // Manda al robot a su posición inicial
    px = px_inicial,
    py = py_inicial;
}