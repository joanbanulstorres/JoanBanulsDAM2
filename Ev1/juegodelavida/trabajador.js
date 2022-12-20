onmessage = function(json){
    datos = json.data.datos;
    centro = datos.data[16];    // célula del centro
    var viva;
    var celulasvivas = 0;

    if(datos.data[0] == 0){celulasvivas++;}     // célula de arriba a la izquierda
    if(datos.data[4] == 0){celulasvivas++;}     // célula de arriba en el centro
    if(datos.data[8] == 0){celulasvivas++;}     // célula de arriba a la derecha
    if(datos.data[12] == 0){celulasvivas++;}    // célula de la izquierda
    if(datos.data[20] == 0){celulasvivas++;}    // célula de la derecha
    if(datos.data[24] == 0){celulasvivas++;}    // célula de abajao a la izquierda
    if(datos.data[28] == 0){celulasvivas++;}    // célula de abajo en el centro
    if(datos.data[32] == 0){celulasvivas++;}    // célula de abajo a la derecha
        
    if(centro == 255){                                  // Si una célula muerta...
        if(celulasvivas == 3){                          // ...tiene tres vecinas vivas...
            viva = true;                                // ...nace en la siguiente iteración...
        }else{
            viva = false;                               // ...en caso contrario sigue muerta
        }
    }
    if(centro == 0){                                    // Si una célula viva...
        if(celulasvivas == 3 || celulasvivas == 2){     // ...tiene 3 o 2 vecinas vivas... 
            viva = true;                               // ...sigue viva en la siguiente iteración
        }else{
            viva = false;                                // ...en caso contrario muere
        }
    }
    
    var jsondevuelta = {"datos":viva,"x":json.data.x ,"y":json.data.y}
    postMessage(jsondevuelta);
}
