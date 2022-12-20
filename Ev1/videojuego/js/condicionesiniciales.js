// Capturamos el lienzo y lo introducimos dentro de la variable contexto /
var contexto = document.getElementById("lienzo").getContext("2d");

var contextofondo = document.getElementById("lienzofondo").getContext("2d");                          
var contextomapa = document.getElementById("lienzomapa").getContext("2d");                            
var contextopunto = document.getElementById("lienzopunto").getContext("2d");

pixelesmapa = contextomapa.getImageData(0,0,512,512);   /* NUEVO - Para la función que impide a los npcs salirse del terreno */

contextopunto.fillStyle = "red";                                                                     

// Aquí voy a declarar las variables globales a todo el programa

var temporizador;
var anchuranavegador = window.innerWidth;   // Para obtener la anchura de la ventana
var alturanavegador = window.innerHeight;   // Para obtener la altura de la ventana

// Aplicamos la anchura y altura dinámica al lienzo, al fondo y al contenedor
document.getElementById("lienzo").width = anchuranavegador;
document.getElementById("lienzo").height = alturanavegador;
document.getElementById("lienzofondo").width = anchuranavegador;    
document.getElementById("lienzofondo").height = alturanavegador;    
document.getElementById("fondo").width = anchuranavegador; 
document.getElementById("fondo").height = alturanavegador;
document.getElementById("contenedor").width = anchuranavegador;
document.getElementById("contenedor").height = alturanavegador;

// Cargamos las imégenes de npc y personaje
var imagennpc1;
var imagennpc1 = new Image();
imagennpc1.src = "img/personajes/personajerojo.png";
/* NUEVO */
var imagennpc2 = new Image();
imagennpc2.src = "img/personajes/personajeverde.png";
var imagennpc3 = new Image();
imagennpc3.src = "img/personajes/personajeazul.png";
var imagennpc4 = new Image();
imagennpc4.src = "img/personajes/personajeamarillo.png";
var imagennpc5 = new Image();
imagennpc5.src = "img/personajes/personajecyan.png";
var imagennpc6 = new Image();
imagennpc6.src = "img/personajes/personajemagenta.png";

var imagenpersonaje = new Image();
imagenpersonaje.src = "img/personajes/personaje.png";   /* NUEVO */

var imagenpremio = new Image();
imagenpremio.src = "img/items/premio.png";


var mapa = new Image();                                                                     
mapa.src = "img/mapas/mapa1.png";
var bloque9 = new Image();                                                                     
bloque9.src = "img/terreno/terreno9.png";


// Introducimos la lista de los personajes
var numeropersonajes = 0;
var arraypersonajes = new Array();

// Propiedades protagonista
var posx = 1000;
var posy = 200;

var posz = 0;   /* ---------------------------------------------------- NUEVO */
var velocidadz = 1;

var estadoanimacion_personaje = 0;
var angulo = 0;
var velocidad = 10;
var direccion = 0;
var energia = 100;  

// Coordenadas del terreno en el que sa van a mover los npc (750x750px)
var terrenox1 = 550;
var terrenoy1 = -350;
var terrenox2 = 1300;
var terrenoy2 = 400;

var premiox = 800;
var premioy = 400;
var nivel = 1;

var pausa = false;

/* NUEVO */
var desfasex = 120;
var desfasey = 0;
var velocidaddesfase = 1;