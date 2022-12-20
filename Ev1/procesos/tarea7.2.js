//Solo se envía un un postMessage cuando se recibe un onmessage
onmessage = function(datos){
    //console.log(datos)
    if(datos.data.px != null){
        var destino = 0;
        for(var i=0; i<datos.data.px.data.length-8; i++){  //Recorremos los píxeles uno a uno  
            var borde = false;  // En principio asumimos que no hay borde en el píxel registrado
            // Para cada uno de los píxeles comprobamos si hay mucha diferencia de color o no la hay
            if(Math.abs(datos.data.px.data[i] - datos.data.px.data[i-(datos.data.mianchurabucket*4)-4]) > datos.data.miumbral){borde = true}   // pixel de arriba a la izquierda
            if(Math.abs(datos.data.px.data[i] - datos.data.px.data[i-(datos.data.mianchurabucket*4)]) > datos.data.miumbral){borde = true}   // pixel de arriba
            if(Math.abs(datos.data.px.data[i] - datos.data.px.data[i-(datos.data.mianchurabucket*4)+4]) > datos.data.miumbral){borde = true}   // pixel de arriba a la derecha
            if(Math.abs(datos.data.px.data[i] - datos.data.px.data[i-4]) > datos.data.umbral){borde = true}   // pixel de la izquierda
            if(Math.abs(datos.data.px.data[i] - datos.data.px.data[i+4]) > datos.data.umbral){borde = true}   // pixel de la derecha
            if(Math.abs(datos.data.px.data[i] - datos.data.px.data[i+(datos.data.mianchurabucket*4)-4]) > datos.data.miumbral){borde = true}   // pixel de abajo a la izquierda
            if(Math.abs(datos.data.px.data[i] - datos.data.px.data[i+(datos.data.mianchurabucket*4)]) > datos.data.miumbral){borde = true}   // pixel de abajo
            if(Math.abs(datos.data.px.data[i] - datos.data.px.data[i+(datos.data.mianchurabucket*4)+4]) > datos.data.miumbral){borde = true}   // pixel de abajo a la derecha
            if (borde == true){     // En el caso de que SÍ haya un borde pinta de negro
                datos.data.pxdst.data[i] = 0;   // R
                datos.data.pxdst.data[i+1] = 0;   // G
                datos.data.pxdst.data[i+2] = 0;   // B
                datos.data.pxdst.data[i+3] = 255; // Transparencia
            }else{      // En el caso de que NO haya un borde pinta de blanco
                datos.data.pxdst.data[i] = 0;
                datos.data.pxdst.data[i+1] = 255;
                datos.data.pxdst.data[i+2] = 255;
                datos.data.pxdst.data[i+3] = 255;
            }
        }
        json = {mix:datos.data.mix, miy:datos.data.miy, resultado:datos.data.pxdst, miidworker:datos.data.idworker}
        postMessage(json) 
    }else{
        postMessage("No se ha recibido la información correctamente");
    }
}