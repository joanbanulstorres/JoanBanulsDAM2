function dibujar_personaje(){
    if(direccion_desplazamiento == 1 && habilitado == true){        // W
        py -= distancia;
        habilitado = false;
        setTimeout(function(){                                      // Las teclas de dirección tienen "cooldown"
        habilitado = true;
        }, 150);
    }      
    if(direccion_desplazamiento == 2 && habilitado == true){        // A
        px -= distancia;
        habilitado = false;
        setTimeout(function(){
            habilitado = true;
        }, 150);
    }                
    if(direccion_desplazamiento == 3 && habilitado == true){        // S
        py += distancia;
        habilitado = false;
        setTimeout(function(){
            habilitado = true;
        }, 150);
    }      
    if(direccion_desplazamiento == 4 && habilitado == true){        // D
        px += distancia;
        habilitado = false;
        setTimeout(function(){
            habilitado = true;
        }, 150);
    }      
    // Para que el personaje no pueda rener la misma posición que los dados
    for(var i=0; i<arraydados.length; i++){
        if(px == arraydados[i].dx - correccion_dx && py == arraydados[i].dy - correccion_dy){
            switch(direccion_desplazamiento){
                case 1:
                    py += distancia;
                break;
                case 2:
                    px += distancia;
                break;
                case 3:
                    py -= distancia;
                break;
                case 4:
                    px -= distancia;
                break;
                default:return;
            }
        }
    }
    // Para controlar que el personaje no se salga del tablero
    if(px < tablerox1 - 45){
        px += 45;
    }
    if(px > tablerox2 + 45){  
        px -= 45;
    }
    if(py > tableroy1 + 45){
        py -= 45;
    }
    if(py < tableroy2 - 45){
        py += 45;
    }
    
    objetos.drawImage(personaje, isox(px, py), isoy(px, py), 80, 80);
}