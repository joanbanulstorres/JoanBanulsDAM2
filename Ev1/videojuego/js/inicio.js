// En la función de inicio cargamos todas las condiciones iniciales del juego
function inicio(){

    // Creo una instancia del objeto o personaje dentro de cada uno de los elemento de la colección
    /*
    for(var i=0; i<numeropersonajes; i++){
        arraypersonajes[i] = new Npc;
    }
    */
    
    // Movimiento del personaje a través del teclado
    // Al pulsar las teclas
    $(document).keydown(function(e){    
        if(e.key == "w"){direccion = 1;}
        if(e.key == "s"){direccion = 2;}                  
        if(e.key == "a"){direccion = 3;}                  
        if(e.key == "d"){direccion = 4;}                  
    })
    // Al dejar de pulsar las teclas
    $(document).keyup(function(e){
        if(e.key == "w"){direccion = 0;}
        if(e.key == "s"){direccion = 0;}                  
        if(e.key == "a"){direccion = 0;}                  
        if(e.key == "d"){direccion = 0;}                    
    })
    
    // Para pausar el juego
    $(document).keydown(function(e){
        if(e.keyCode == 27){
            pausa = true;
            $("#pantallainicialmedio").fadeIn("slow");
            $("#contenedor").addClass("difuminado");
        }
    })
    
    // Cuando la ventana se reescala, calculamos de nuevo el contenido de los contenedores en base a la ventana
    $(window).resize(function(){
        var anchuranavegador = window.innerWidth;   // Para obtener la anchura de la ventana
        var alturanavegador = window.innerHeight;   // Para obtener la altura de la ventana
        // Aplicamos la anchura y altura dinámica al lienzo, al fondo y al contenedor
        document.getElementById("lienzo").width = anchuranavegador;
        document.getElementById("lienzo").height = alturanavegador;
        document.getElementById("fondo").width = anchuranavegador;
        document.getElementById("fondo").height = alturanavegador;
        document.getElementById("contenedor").width = anchuranavegador;
        document.getElementById("contenedor").height = alturanavegador;
    })
    
    posinicialjugador();    /* NUEVO */
    creaenemigos();         /* NUEVO */
    creaobjetivo();         /* NUEVO */
    
    temporizador = setTimeout("bucle()", 1000);  // Lanzo la ejecución del bucle tras 1000ms = 1s
}