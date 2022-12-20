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

var tablerox1 = 416,
    tableroy1 = 190,
    tablerox2 = 758,
    tableroy2 = -152;

var habilitado = true;  // para las teclas W, A, S, D

var contador_subnivel = 1,
    contador_nivel = 1;
 
/////////////// ▽ PERSONAJE ▽ ///////////////
var personaje = new Image();
    personaje.src = "img/robot.png";
var px = 587,
    py = 190,
    px_inicial = 587,
    py_inicial = 190,
    distancia = 57;
var direccion_desplazamiento = 0;
///////////////// △ PERSONAJE △ ///////////////

/////////////// ▽ DADOS ▽ ///////////////
var dados = new Image();
dados.src = "img/dados_spritesheet.png"; 

var arraydados = new Array();
for(var i=0; i<contador_nivel; i++){
    arraydados[i] = new Dado;
}

var correccion_dx = 22,
    correccion_dy = 15;

var contador_correctos = 0;
/////////////// △ DADOS △ ///////////////