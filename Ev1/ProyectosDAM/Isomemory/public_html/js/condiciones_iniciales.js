// Declaración de las dimensiones de 'contenedor' (navegador)
var anchura_contenedor = window.innerWidth,
    altura_contenedor = window.innerHeight;
document.getElementById("contenedor").width = anchura_contenedor;
document.getElementById("contenedor").height = altura_contenedor;

// Declaración de las dimensiones de 'tablero' (ventana)
var tablero = document.getElementById("tablero"),
    anchura_tablero = tablero.offsetWidth,   
    altura_tablero = tablero.offsetHeight;
document.getElementById("tablero").width = anchura_contenedor;
document.getElementById("tablero").height = altura_contenedor;

// Declaración de las dimensiones de 'objetos' (ventana)
var objetos = document.getElementById("objetos").getContext("2d"),
    //anchura_objetos = document.getElementById("objetos").width,
    //altura_objetos = document.getElementById("objetos").height;
    anchura_objetos = 1232,
    altura_objetos = 924;
document.getElementById("objetos").width = anchura_objetos; 
document.getElementById("objetos").height = altura_objetos;
objetos.imageSmoothingEnabled = true;

var tablerox1 = 425,
    tableroy1 = 210,
    tablerox2 = 785,
    tableroy2 = -150;

var habilitado = true;  // para las teclas W, A, S, D

var contador_subnivel = 1,
    contador_nivel = 1;
 
/////////////// ▽ PERSONAJE ▽ ///////////////
var personaje = new Image();
    personaje.src = "img/robot.png";
var px = 605,
    py = 255,
    px_inicial = 605,
    py_inicial = 255;
    distancia = 45;
var direccion_desplazamiento = 0;
///////////////// △ PERSONAJE △ ///////////////

/////////////// ▽ DADOS ▽ ///////////////
var dados = new Image();
dados.src = "img/dados_spritesheet.png"; 

var arraydados = new Array();
for(var i=0; i<contador_nivel; i++){
    arraydados[i] = new Dado;
}

var correccion_dx = 18,
    correccion_dy = 12;

var contador_correctos = 0;
/////////////// △ DADOS △ ///////////////