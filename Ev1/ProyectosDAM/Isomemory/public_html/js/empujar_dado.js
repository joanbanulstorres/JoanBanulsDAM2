// El personaje empuja los dados dependiendo de su posición respecto a los mismos, y éstos no se pueden salir del tablero 
function empujar_dado(){
    for(var i =0 ; i<arraydados.length; i++){
        //console.log("Posición actual del dado " + arraydados[i] + " : " + arraydados[i].dx + ", " + arraydados[i].dy);
        
        if(px +45 + correccion_dx == arraydados[i].dx && py + correccion_dy == arraydados[i].dy){       // Si el personaje está a la izquierda del dado
            //console.log("Dado empujado desde la izquierda");
            arraydados[i].dx += 45;
            var direccion_empuje = 'izquierda';
        }
        if(px -45 + correccion_dx == arraydados[i].dx && py + correccion_dy == arraydados[i].dy){       // Si el personaje está a la derecha del dado
            //console.log("Dado empujado desde la derecha");
            arraydados[i].dx -= 45;
            var direccion_empuje = 'derecha';
        }
        if(px + correccion_dx == arraydados[i].dx && py -45 + correccion_dy == arraydados[i].dy){       // Si el personaje está abajo del dado
            //console.log("Dado empujado desde abajo");
            arraydados[i].dy -= 45;
            var direccion_empuje = 'abajo';
        }
        if(px + correccion_dx == arraydados[i].dx && py +45 + correccion_dy == arraydados[i].dy){       // Si el personaje está arriba del dado
            //console.log("Dado empujado desde ariba");
            arraydados[i].dy += 45;
            var direccion_empuje = 'arriba';
        }
        // Para que los dados no lleguen a tener la misma posición
        if(i > 0){
            for(var j =0 ; j<arraydados.length; j++){
                if(i != j){
                    if(arraydados[i].dx == arraydados[j].dx && arraydados[i].dy == arraydados[j].dy){
                        switch(direccion_empuje){
                            case 'izquierda':
                                arraydados[i].dx -= 45;
                            break;
                            case 'derecha':
                                arraydados[i].dx += 45;
                            break;
                            case 'abajo':
                                arraydados[i].dy += 45;
                            break;
                            case 'arriba':
                                arraydados[i].dy -= 45;
                            break;
                            default:return;
                        }
                    }
                }
            }
        }
        // Para controlar que los dados no se salgan del tablero
        if(arraydados[i].dx < tablerox1 - 18){
            arraydados[i].dx += 45;
        }
        if(arraydados[i].dx > tablerox2 + 18){
            arraydados[i].dx -= 45;
        }
        if(arraydados[i].dy > tableroy1 + 12){
            arraydados[i].dy -= 45;
        }
        if(arraydados[i].dy < tableroy2 - 12){
            arraydados[i].dy += 45;
        } 
    }
}