document.onkeydown = function(e){
    switch(e.which){
        case 87:    // W
            direccion_desplazamiento = 1;
            direccion_sprite = 1;
        break;
        case 65:    // A
            direccion_desplazamiento = 2;
            direccion_sprite = 2;
        break;
        case 83:    // S
            direccion_desplazamiento = 3;
            direccion_sprite = 3;
        break;
        case 68:    // D
            direccion_desplazamiento = 4;
            direccion_sprite = 4;
        break;
        case 32:    // Espacio
            empujar_dado();
        break;
        case 82:    // R
            if(contador_subnivel == 1){
               subnivel();
            }else{
                nivel();
            }
        break;
        case 27:     // Esc
            $("#contenedor").addClass("difuminado");
            $("#pantallamedio").fadeIn("slow");
            $("#pantallanivel").fadeOut("slow");
       break;
        // Controles que no son para el usuario
        case 67:    // C  
            console.log("Posición actual del personaje: " + px + ", " + py);
            for(var i=0; i<arraydados.length; i++){
                console.log("Posición anterior del dado " + arraydados[i] + " : " + arraydados[i].dx_anterior + ", " + arraydados[i].dy_anterior);
                console.log("Posición actual del dado " + arraydados[i] + " : " + arraydados[i].dx + ", " + arraydados[i].dy);
            }
       break;
       case 80:     // P
           for(var i=0; i<arraydados.length; i++){
                arraydados[i].dx = arraydados[i].dx_anterior;
                arraydados[i].dy = arraydados[i].dy_anterior;
            }
       break;
       default:return;
    }
}
document.onkeyup = function(e){
    switch(e.which){
        case 87:    // W
            direccion_desplazamiento = 0;
        break;
        case 65:    // A
            direccion_desplazamiento = 0;
        break;
        case 83:    // S
            direccion_desplazamiento = 0;
        break;
        case 68:    // D
            direccion_desplazamiento = 0;
        break;
        default:return;
    }
}