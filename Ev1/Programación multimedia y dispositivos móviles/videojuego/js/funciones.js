// Funciones de conversión a gráficos isonométricos
function isox(x, y){
    return(x-y);
}
function isoy(x, y){
    return((x+y)/2);
}

function reiniciar(){   
    // Introducimos la lista de los personajes
    numeropersonajes = 5;
    arraypersonajes = new Array();

    // Propiedades protagonista
    posx = 1000;
    posy = 200;
    estadoanimacion_personaje = 0;
    angulo = 0;
    velocidad = 10;
    direccion = 0;
    energia = 100;  

    // Coordenadas del terreno en el que sa van a mover los npc (750x750px)
    terrenox1 = 550;
    terrenoy1 = -350;
    terrenox2 = 1300;
    terrenoy2 = 400;

    pausa = false;  
    
    for(var i=0; i<numeropersonajes; i++){
        arraypersonajes[i] = new Npc;
    }
}

function subirnivel(){  
    pausa = true;
    nivel++;
    $("#dimenivel").html(nivel);
    $("#pantallanivel").fadeIn("slow");
    contexto.clearRect(0, 0, anchuranavegador, alturanavegador);
    setTimeout(function(){
        $("#pantallanivel").fadeOut("slow");
        pausa = false;
        bucle();
    }, 3000)
    
    // Introducimos la lista de los personajes
    numeropersonajes *= 2;
    arraypersonajes = new Array();

    // Propiedades protagonista
    posx = 1000;
    posy = 200;
    estadoanimacion_personaje = 0;
    angulo = 0;
    velocidad = 10;
    direccion = 0;
    energia = 100;  

    // Coordenadas del terreno en el que sa van a mover los npc (750x750px)
    terrenox1 = 550;
    terrenoy1 = -350;
    terrenox2 = 1300;
    terrenoy2 = 400;
    
    for(var i=0; i<numeropersonajes; i++){
        arraypersonajes[i] = new Npc;
    }
    
    // Para que el premio aparezca en lugares diferentes al subir de nivel
    premiox = terrenox1 + Math.random()*(terrenox2 - terrenox1);
    premioy = terrenoy1 + Math.random()*(terrenoy2 - terrenoy1);
}

function dibujaterreno(){
    contextofondo.clearRect(0, 0, anchuranavegador, alturanavegador);
    var anchurabloque = 50;     // Separación entre los bloques de terreno
    var anchuradibujo = 120;    // Tamaño de los bloques de terreno
    contextomapa.drawImage(mapa, 0, 0);
    var pixeles = contextomapa.getImageData(0, 0, 512, 512);
    for(var i=0; i<pixeles.data.length; i+=4){
        var cr = pixeles.data[i];       // Canal rojo
        var cg = pixeles.data[i+1];     // Canal verde
        var cb = pixeles.data[i+2];     // Canal azul
        var ca = pixeles.data[i+3];     // Opacidad
        
        // Coordenadas de los píxeles
        var x = ((i) % 512 / 4);
        var y = Math.floor((i/512)/4);
        
        if(ca == 255){  // Si se encuentra con un píxel opaco en la imagen...
            /* NUEVO - El terreno que está fuera de la pantalla no se dibuja */
            if(
                isox(x*anchurabloque, y*anchurabloque) + desfasex > 0
                &&
                isox(x*anchurabloque, y*anchurabloque) + desfasex < anchuranavegador
                &&
                isoy(x*anchurabloque, y*anchurabloque) + desfasey > 0
                &&
                isoy(x*anchurabloque, y*anchurabloque) + desfasey < alturanavegador
            ){
                //console.log("Te has encontrado con un trozo de terreno");
                //console.log(x + "," + y);
                contextofondo.drawImage(bloque9, isox(x*anchurabloque, y*anchurabloque) + desfasex, isoy(x*anchurabloque, y*anchurabloque) + desfasey, anchuradibujo, anchuradibujo); 
            }
        }
    }
}

/* NUEVO */

function posinicialjugador(){
    var pixeles = contextomapa.getImageData(0, 0, 512, 512);
    for(var i=0; i<pixeles.data.length; i+=4){
        var cr = pixeles.data[i];       // Canal rojo
        var cg = pixeles.data[i+1];     // Canal verde
        var cb = pixeles.data[i+2];     // Canal azul
        var ca = pixeles.data[i+3];     // Opacidad
        
        // Coordenadas de los píxeles
        var x = ((i) % 512 / 4);
        var y = Math.floor((i/512)/4);
        
        if(ca == 255){
            if(cr == 0 && cg == 255 && cb == 0){    // Si el píxel es verde
                posx = x*50;
                posy = y*50;
                console.log("He encontrado al jugador en las coordenadas " + posx + ", " + posy);
            }
        }
    }
}

function creaenemigos(){
    var pixeles = contextomapa.getImageData(0, 0, 512, 512);
    for(var i=0; i<pixeles.data.length; i+=4){
        var cr = pixeles.data[i];       // Canal rojo
        var cg = pixeles.data[i+1];     // Canal verde
        var cb = pixeles.data[i+2];     // Canal azul
        var ca = pixeles.data[i+3];     // Opacidad
        
        // Coordenadas de los píxeles
        var x = ((i) % 512 / 4);
        var y = Math.floor((i/512)/4);
        
        if(ca == 255){
            if(cr == 255 && cg == 0 && cb == 0){    // Si el píxel es rojo
                arraypersonajes[numeropersonajes] = new Npc;
                arraypersonajes[numeropersonajes].x = x*50;
                arraypersonajes[numeropersonajes].y = y*50;
                numeropersonajes++;
            }
        }
    }
}

function creaobjetivo(){
    var pixeles = contextomapa.getImageData(0, 0, 512, 512);
    for(var i=0; i<pixeles.data.length; i+=4){
        var cr = pixeles.data[i];       // Canal rojo
        var cg = pixeles.data[i+1];     // Canal verde
        var cb = pixeles.data[i+2];     // Canal azul
        var ca = pixeles.data[i+3];     // Opacidad
        
        // Coordenadas de los píxeles
        var x = ((i) % 512 / 4);
        var y = Math.floor((i/512)/4);
        
        if(ca == 255){
            if(cr == 0 && cg == 0 && cb == 255){    // Si el píxel es azul
                premiox = x*50;
                premioy = y*50;
            }
        }
    }
}