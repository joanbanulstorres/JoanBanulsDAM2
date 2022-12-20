// El personaje empuja los dados dependiendo de su posición respecto a los mismos, y éstos no se pueden salir del tablero 
function empujar_dado(){
    
    var direccion_empuje;
    
    for(var i=0; i<arraydados.length; i++){
        
        if(px +distancia + correccion_dx == arraydados[i].dx && py + correccion_dy == arraydados[i].dy){       // Si el personaje está a la izquierda del dado
            //console.log("Dado empujado desde la izquierda");
            arraydados[i].dx += distancia;
            direccion_empuje = 'derecha';
        }
        if(px -distancia + correccion_dx == arraydados[i].dx && py + correccion_dy == arraydados[i].dy){       // Si el personaje está a la derecha del dado
            //console.log("Dado empujado desde la derecha");
            arraydados[i].dx -= distancia;
            direccion_empuje = 'izquierda';
        }
        if(px + correccion_dx == arraydados[i].dx && py -distancia + correccion_dy == arraydados[i].dy){       // Si el personaje está abajo del dado
            //console.log("Dado empujado desde abajo");
            arraydados[i].dy -= distancia;
            direccion_empuje = 'arriba';
        }
        if(px + correccion_dx == arraydados[i].dx && py +distancia + correccion_dy == arraydados[i].dy){       // Si el personaje está arriba del dado
            //console.log("Dado empujado desde ariba");
            arraydados[i].dy += distancia;
            direccion_empuje = 'abajo';
        }
        
        // Para controlar que los dados no se salgan del tablero
        if(arraydados[i].dx < tablerox1 + distancia + correccion_dx){
            arraydados[i].dx += distancia;
        }
        if(arraydados[i].dx > tablerox2 - distancia + correccion_dx){
            arraydados[i].dx -= distancia;
        }
        if(arraydados[i].dy > tableroy1 - distancia + correccion_dy){
            arraydados[i].dy -= distancia;
        }
        if(arraydados[i].dy < tableroy2 + distancia + correccion_dy){
            arraydados[i].dy += distancia;
        }
        
        // Para que los dados se empujen unos a otros
        for(var j=0; j<arraydados.length; j++){
            if(i != j){     // Para no comparar un dado consigo mismo
                if(arraydados[i].dx == arraydados[j].dx && arraydados[i].dy == arraydados[j].dy){
                    switch(direccion_empuje){   // Empujado hacia
                        case 'izquierda':
                            arraydados[j].dx -= distancia;
                            if(arraydados[j].dx < tablerox1 + distancia + correccion_dx){
                                arraydados[j].dx += distancia;
                                arraydados[i].dx += distancia;
                            }
                        break;
                        case 'derecha':
                            arraydados[j].dx += distancia;
                            if(arraydados[j].dx > tablerox2 - distancia + correccion_dx){   // Para que los dados empujados no se salgan del tablero
                                arraydados[j].dx -= distancia;
                                arraydados[i].dx -= distancia;
                            }
                        break;
                        case 'arriba':
                            arraydados[j].dy -= distancia;
                            if(arraydados[j].dy < tableroy2 + distancia + correccion_dy){
                                arraydados[j].dy += distancia;
                                arraydados[i].dy += distancia;
                            }
                        break;
                        case 'abajo':
                            arraydados[j].dy += distancia;
                            if(arraydados[j].dy > tableroy1 - distancia + correccion_dy){
                                arraydados[j].dy -= distancia;
                                arraydados[i].dy -= distancia;
                            }
                        break;
                        default:return;
                    }
                }
            }
        }
    }
}