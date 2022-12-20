// Este código centra la ventana del juego en la ventana del navegador

// Cálculo del margen vertical (top) y el margen horizontal (left) entre 'contenedor' y 'tablero'
var margen_vertical = (altura_contenedor - altura_tablero)/2,
    margen_horizontal = (anchura_contenedor - anchura_tablero)/2;

// Aplicación de los márgenes optenidos a cada uno de los elementos de la ventana ('tablero', 'objetos', 'pantallaincial' ...)
var ventana = document.getElementsByClassName("ventana");
for(var i=0; i<ventana.length; i++){
    ventana[i].style.setProperty("top", margen_vertical + "px");
    ventana[i].style.setProperty("left", margen_horizontal + "px");
}

// Cada vez que se reescale la ventana, se vuelven a capturar sus dimensiones para centrar el canvas vertical y horizontalmente 
$(window).resize(function(){
    anchura_contenedor = window.innerWidth,
    altura_contenedor = window.innerHeight;
    document.getElementById("contenedor").width = anchura_contenedor;
    document.getElementById("contenedor").height = altura_contenedor;
    
    margen_vertical = (altura_contenedor - altura_tablero)/2,
    margen_horizontal = (anchura_contenedor - anchura_tablero)/2;
    ventana = document.getElementsByClassName("ventana");
    for(i=0; i<ventana.length; i++){
        ventana[i].style.setProperty("top", margen_vertical + "px");
        ventana[i].style.setProperty("left", margen_horizontal + "px");
    }
});