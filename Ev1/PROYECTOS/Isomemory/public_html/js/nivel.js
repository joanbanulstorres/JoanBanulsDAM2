function nivel(){
    // Se comparan las posiciones nuevas de los dados con las anteriores
    for(var i=0; i<arraydados.length; i++){
        if(arraydados[i].dx == arraydados[i].dx_anterior && arraydados[i].dy == arraydados[i].dy_anterior){ 
            contador_correctos += 1;
        }
    }
    //console.log("Dados posicionados correctamente: " + contador_correctos + " de " + arraydados.length);
    if(contador_correctos == arraydados.length){    // Si todas las nuevas posiciones de los dados son iguales a las posiciones anteriores sube de nivel
        if(contador_nivel < 6){    // Hay un máximo de 6 niveles (de 0 a 5)
            contador_nivel++;
            contador_subnivel--;
            $("#dimesubnivel").html("Memoriza");
            $("#dimenivel").html(contador_nivel);
            //console.log(contador_nivel);
            px = px_inicial;
            py = py_inicial;

            // Crea un nuevo dado
            arraydados[contador_nivel-1] = new Dado;

            for(i=0; i<arraydados.length; i++){
                // Asigna nuevas posiciones a los dados
                arraydados[i].dx = tablerox1 + (Math.floor(Math.random() * 9)) * 45 + correccion_dx;
                arraydados[i].dy = tableroy2 + (Math.floor(Math.random() * 9)) * 45 + correccion_dy;
                // Guarda esas posiciones para poder compararlas en la fase de posicionar
                arraydados[i].dx_anterior = arraydados[i].dx;
                arraydados[i].dy_anterior = arraydados[i].dy;
            }
        }else{
            $("#contenedor").addClass("difuminado");
            $("#pantallanivel").fadeOut("slow");
            $("#pantallavictoria").fadeIn("slow");
        }
        contador_correctos = 0;
    }else{  // Si no lo son, vuelve a la pantalla inicial
        var objetos = document.getElementById("objetos").getContext("2d");
        objetos.clearRect(0, 0, anchura_objetos, altura_objetos);
        //$("#dimenivel").html(nivel);
        $("#contenedor").addClass("difuminado");
        $("#pantallanivel").fadeOut("slow");
        $("#pantallafinal").fadeIn("slow");
        contador_correctos = 0;
    }
}