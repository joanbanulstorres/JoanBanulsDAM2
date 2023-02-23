function dibujar_dados(){               
    var sx = 0, // Punto a seleccionar del spritesheet
        sy = 0;
    for(var i=0; i<arraydados.length; i++){
        // Para dibujar un solo dado
        if(i == 0){
            objetos.drawImage(
                dados,
                sx, 
                sy,
                400,
                400,
                isox(arraydados[i].dx, arraydados[i].dy),
                isoy(arraydados[i].dx, arraydados[i].dy),
                80,
                80);
            if(sx < 800){
                sx += 400;
            }else{
                sx = 0;
                if(sy < 400){
                    sy += 400;
                }
            }
        // Para dibujar de 2 a 6 dados
        }else{
            // Se compara la posición del dado nuevo con las de los dados anteriores
            for(var j=0; j<arraydados.length; j++){    // Para no comparar un dado con sí mismo
                if(i != j){ 
                    // Mientras las posiciones de dos dados sean iguales...
                    while(arraydados[i].dx == arraydados[j].dx && arraydados[i].dy == arraydados[j].dy){
                        console.log("Misma posición");
                        // Da al nuevo dado una posición aleatoria
                        arraydados[i].dx = 473 + correccion_dx + (Math.floor(Math.random() * 5)) * distancia;
                        arraydados[i].dy = -95 + correccion_dy + (Math.floor(Math.random() * 5)) * distancia;
                    }
                }    
            }
            // Una vez la posición del nuevo dado no coincida con las posiciones de los dados anteriores, se dibuja el nuevo dado
            objetos.drawImage(
                dados,
                sx,
                sy,
                400,
                400,
                isox(arraydados[i].dx, arraydados[i].dy),
                isoy(arraydados[i].dx, arraydados[i].dy),
                80,
                80);
            if(sx < 800){
                sx += 400;
            }else{
                sx =0;
                if(sy < 400){
                    sy += 400;
                }
            }
        }
    }
}