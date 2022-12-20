// En la función de bucle cargamos todo aquello que se va a ir repitiendo una y otra vez durante el juego
function bucle(){
    contexto.clearRect(0, 0, anchuranavegador, alturanavegador); //Al principio de cada bucle, borramos el lienzo anterior
    
    /* NUEVO */
    contextopunto.clearRect(0, 0, 512, 512);
    contextopunto.fillRect(posx/50, posy/50, 5, 5);     // 50 es el tamaño de 'anchurabloque'
    dibujaterreno();
    var mediopantallax = anchuranavegador/2;
    var mediopantallay = alturanavegador/2;
    /*if(isox(posx, posy) +desfasex <= mediopantallax){desfasex+=velocidaddesfase;}else{desfasex-=velocidaddesfase;}
    if(isoy(posx, posy) +desfasey < mediopantallay){desfasey+=velocidaddesfase;}else{desfasey-=velocidaddesfase;}*/
    
    /* NUEVO - El personaje se cae del terreno */
    var pixelpersonaje = contextomapa.getImageData(Math.round(posx/50)+1, Math.round(posy/50)+1, 1, 1);
    for(var i=0; i<pixelpersonaje.data.length; i+=4){
        var ca = pixelpersonaje.data[i+3];     // Opacidad
        
        if(ca == 0){
            console.log("Te has caído");
            velocidadz *= 1.3;
            posz += velocidadz;
        }
    }
    if(posz > 800){
        window.location = window.location;
    }
        
    /* NUEVO */
    desfasex = mediopantallax - isox(posx, posy);
    desfasey = mediopantallay - isoy(posx, posy);
    
    ////////////////////////////// ↓ NPCS ↓ //////////////////////////////
    // Iteramos todos los elementos del array uno a uno y realizamos las operaciones
    for(var i=0; i<numeropersonajes; i++){
        // Medimos la distancia entre el personaje y los npcs
        var a = posx - arraypersonajes[i].x;
        var b = posy - arraypersonajes[i].y;
        var distancia = Math.sqrt( a*a + b*b );
        
        // Movemos los npc
        if(distancia < 400){ 
            arraypersonajes[i].persigue();  // Si el npc está cerca del personaje le persigue
            //arraypersonajes[i].mueve();
        }else{
           arraypersonajes[i].mueve(); 
        }
        if(distancia < 10){ // Si el npc está muy cerca del personaje le quita energía
            energia -= 5;
        }
        
        var angulo_npc;
        if(arraypersonajes[i].direccionisometrica == 0){angulo_npc = 0;}
        if(arraypersonajes[i].direccionisometrica == 1){angulo_npc = 512;}
        if(arraypersonajes[i].direccionisometrica == 2){angulo_npc = 1024;}
        if(arraypersonajes[i].direccionisometrica == 3){angulo_npc = 1536;}
        
        
        if(arraypersonajes[i].color == 0){          /* NUEVO */
            // Dibujamos los npc
            if(     /* NUEVO - Los npcs que estén fuera de la pantalla no se dibujan */
                isox(arraypersonajes[i].x, arraypersonajes[i].y) + desfasex > 0
                &&
                isox(arraypersonajes[i].x, arraypersonajes[i].y) + desfasex < anchuranavegador
                &&
                isoy(arraypersonajes[i].x, arraypersonajes[i].y) + desfasey > 0
                &&
                isoy(arraypersonajes[i].x, arraypersonajes[i].y) + desfasey < alturanavegador
            ){
                contexto.drawImage(
                    imagennpc1,
                    arraypersonajes[i].estadoanimacion_npc*256, 
                    angulo_npc+256,  // +256 para que coja la fila de las imágenes isonométricas
                    256,
                    256,    
                    isox(arraypersonajes[i].x,arraypersonajes[i].y) + desfasex,     // Desfasex
                    isoy(arraypersonajes[i].x,arraypersonajes[i].y) + desfasey,     // Desfasey
                    128,
                    128
                );
            }
        // Dibujamos en el punto (0,0)px un cuadrado de (256, 256)px de los 2048x2048px de la spritesheet para obtener solo la primera imagen del npc  
        }
        else if(arraypersonajes[i].color == 1){
            if(
                isox(arraypersonajes[i].x, arraypersonajes[i].y) + desfasex > 0
                &&
                isox(arraypersonajes[i].x, arraypersonajes[i].y) + desfasex < anchuranavegador
                &&
                isoy(arraypersonajes[i].x, arraypersonajes[i].y) + desfasey > 0
                &&
                isoy(arraypersonajes[i].x, arraypersonajes[i].y) + desfasey < alturanavegador
            ){
                contexto.drawImage(
                    imagennpc2,
                    arraypersonajes[i].estadoanimacion_npc*256, 
                    angulo_npc+256,  // +256 para que coja la fila de las imágenes isonométricas
                    256,
                    256,    
                    isox(arraypersonajes[i].x,arraypersonajes[i].y) + desfasex,     // Desfasex
                    isoy(arraypersonajes[i].x,arraypersonajes[i].y) + desfasey,     // Desfasey
                    128,
                    128
                );
            }
        }
        else if(arraypersonajes[i].color == 2){
            if(
                isox(arraypersonajes[i].x, arraypersonajes[i].y) + desfasex > 0
                &&
                isox(arraypersonajes[i].x, arraypersonajes[i].y) + desfasex < anchuranavegador
                &&
                isoy(arraypersonajes[i].x, arraypersonajes[i].y) + desfasey > 0
                &&
                isoy(arraypersonajes[i].x, arraypersonajes[i].y) + desfasey < alturanavegador
            ){
                contexto.drawImage(
                    imagennpc3,
                    arraypersonajes[i].estadoanimacion_npc*256, 
                    angulo_npc+256,  // +256 para que coja la fila de las imágenes isonométricas
                    256,
                    256,    
                    isox(arraypersonajes[i].x,arraypersonajes[i].y) + desfasex,     // Desfasex
                    isoy(arraypersonajes[i].x,arraypersonajes[i].y) + desfasey,     // Desfasey
                    128,
                    128
                );
            }
        }
        else if(arraypersonajes[i].color == 3){
            if(
                isox(arraypersonajes[i].x, arraypersonajes[i].y) + desfasex > 0
                &&
                isox(arraypersonajes[i].x, arraypersonajes[i].y) + desfasex < anchuranavegador
                &&
                isoy(arraypersonajes[i].x, arraypersonajes[i].y) + desfasey > 0
                &&
                isoy(arraypersonajes[i].x, arraypersonajes[i].y) + desfasey < alturanavegador
            ){
                contexto.drawImage(
                    imagennpc4,
                    arraypersonajes[i].estadoanimacion_npc*256, 
                    angulo_npc+256,  // +256 para que coja la fila de las imágenes isonométricas
                    256,
                    256,    
                    isox(arraypersonajes[i].x,arraypersonajes[i].y) + desfasex,     // Desfasex
                    isoy(arraypersonajes[i].x,arraypersonajes[i].y) + desfasey,     // Desfasey
                    128,
                    128
                );
            }
        }
        else if(arraypersonajes[i].color == 4){
            if(
                isox(arraypersonajes[i].x, arraypersonajes[i].y) + desfasex > 0
                &&
                isox(arraypersonajes[i].x, arraypersonajes[i].y) + desfasex < anchuranavegador
                &&
                isoy(arraypersonajes[i].x, arraypersonajes[i].y) + desfasey > 0
                &&
                isoy(arraypersonajes[i].x, arraypersonajes[i].y) + desfasey < alturanavegador
            ){
                contexto.drawImage(
                    imagennpc5,
                    arraypersonajes[i].estadoanimacion_npc*256, 
                    angulo_npc+256,  // +256 para que coja la fila de las imágenes isonométricas
                    256,
                    256,    
                    isox(arraypersonajes[i].x,arraypersonajes[i].y) + desfasex,     // Desfasex
                    isoy(arraypersonajes[i].x,arraypersonajes[i].y) + desfasey,     // Desfasey
                    128,
                    128
                );
            }
        }
        else if(arraypersonajes[i].color == 5){
            if(
                isox(arraypersonajes[i].x, arraypersonajes[i].y) + desfasex > 0
                &&
                isox(arraypersonajes[i].x, arraypersonajes[i].y) + desfasex < anchuranavegador
                &&
                isoy(arraypersonajes[i].x, arraypersonajes[i].y) + desfasey > 0
                &&
                isoy(arraypersonajes[i].x, arraypersonajes[i].y) + desfasey < alturanavegador
            ){
                contexto.drawImage(
                    imagennpc6,
                    arraypersonajes[i].estadoanimacion_npc*256, 
                    angulo_npc+256,  // +256 para que coja la fila de las imágenes isonométricas
                    256,
                    256,    
                    isox(arraypersonajes[i].x,arraypersonajes[i].y) + desfasex,     // Desfasex
                    isoy(arraypersonajes[i].x,arraypersonajes[i].y) + desfasey,     // Desfasey
                    128,
                    128
                );
            }
        }
        
        
        
        if(
            isox(arraypersonajes[i].x, arraypersonajes[i].y) + desfasex > 0
            &&
            isox(arraypersonajes[i].x, arraypersonajes[i].y) + desfasex < anchuranavegador
            &&
            isoy(arraypersonajes[i].x, arraypersonajes[i].y) + desfasey > 0
            &&
            isoy(arraypersonajes[i].x, arraypersonajes[i].y) + desfasey < alturanavegador
        ){
            // Dibujamos la barra de energía
            contexto.fillStyle = "black";
            contexto.fillRect(
                isox(arraypersonajes[i].x, arraypersonajes[i].y)+32 + desfasex, // Desfasex
                isoy(arraypersonajes[i].x, arraypersonajes[i].y) + desfasey,    // Desfasey
                64,
                10
            )
            contexto.fillStyle = "green";
            contexto.fillRect(
                isox(arraypersonajes[i].x, arraypersonajes[i].y)+34 + desfasex, // Desfasex
                isoy(arraypersonajes[i].x, arraypersonajes[i].y)+2 + desfasey,  // Desfasey
                60*(arraypersonajes[i].energia/100),
                6
            )
        }
    }
    ////////////////////////////// ↑ NPCS ↑ //////////////////////////////
    
    ////////////////////////////// ↓ PERSONAJE PROTAGONISTA ↓ //////////////////////////////
    estadoanimacion_personaje++;
    if(estadoanimacion_personaje > 7){estadoanimacion_personaje = 0}
    contexto.drawImage(
        imagenpersonaje,
        estadoanimacion_personaje*256, 
        angulo+256,
        256,
        256,    
        isox(posx, posy) + desfasex,                                    // Desfasex
        isoy(posx, posy) + desfasey + posz,                             // Desfasey ---------------------------- * NUEVO - posz *
        128,
        128
    );
    if(direccion == 1){posy -= velocidad; angulo=512}   // w
    if(direccion == 2){posy += velocidad; angulo=1536}  // s
    if(direccion == 3){posx -= velocidad; angulo=0}     // a
    if(direccion == 4){posx += velocidad; angulo=1024}  // d
    
    // Dibujamos la barra de energía
    contexto.fillStyle = "black";
    contexto.fillRect(
        isox(posx, posy)+32 + desfasex,                                 // Desfasex
        isoy(posx, posy) + desfasey + posz,                             // Desfasey ---------------------------- * NUEVO - posz *
        64,
        10
    )
    contexto.fillStyle = "green";
    contexto.fillRect(
        isox(posx, posy)+34 + desfasex,                                 // Desfasex
        isoy(posx, posy)+2 + desfasey + posz,                           // Desfasey ---------------------------- * NUEVO - posz *
        60*(energia/100),
        6
    )
    ////////////////////////////// ↑ PERSONAJE PROTAGONISTA ↑ //////////////////////////////
    
    ////////////////////////////// ↓ PREMIO ↓ ////////////////////////////// 
    contexto.drawImage(imagenpremio, isox(premiox, premioy)  + desfasex, isoy(premiox, premioy) + desfasey);    
    a = posx - premiox;
    b = posy - premioy;
    distancia = Math.sqrt( a*a + b*b );     // Teorema de Pitágoras
    if(distancia < 20){
        console.log("premio");
        subirnivel();
    }
    ////////////////////////////// ↑ PREMIO ↑ ////////////////////////////// 
    
    // Muerte del personaje
    if(energia <= 0){    
        $("#pantallainicial").fadeIn("slow");
        reiniciar();
        contexto.clearRect(0, 0, anchuranavegador, alturanavegador);
        pausa = "true";
    }
    
    clearTimeout(temporizador); // Eliminamos el temporizador actual
    if(pausa == false){    
        temporizador = setTimeout("bucle()", 33); // Creamos un nuevo temporizador para volver a ejecutar
    }
}