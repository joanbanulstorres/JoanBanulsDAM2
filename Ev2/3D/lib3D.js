var Vertice3D = function(x, y, z){
    this.x = parseFloat(x);                                                 // 'parseFolat' analiza un argumento y devuelve el primer número
    this.y = parseFloat(y);
    this.z = parseFloat(z);
}

var Vertice2D = function(x, y){
    this.x = parseFloat(x);                                                 
    this.y = parseFloat(y);
}

var Cubo = function(centro, lado, color){
    var anchura = lado/2;
    this.color = color;
    this.vertices = [
        new Vertice3D(centro.x - anchura, centro.y - anchura, centro.z + anchura),
        new Vertice3D(centro.x - anchura, centro.y - anchura, centro.z - anchura),
        new Vertice3D(centro.x + anchura, centro.y - anchura, centro.z - anchura),
        new Vertice3D(centro.x + anchura, centro.y - anchura, centro.z + anchura),
        new Vertice3D(centro.x + anchura, centro.y + anchura, centro.z + anchura),
        new Vertice3D(centro.x + anchura, centro.y + anchura, centro.z - anchura),
        new Vertice3D(centro.x - anchura, centro.y + anchura, centro.z - anchura),
        new Vertice3D(centro.x - anchura, centro.y + anchura, centro.z + anchura)
    ];
    this.caras = [
        [this.vertices[0], this.vertices[1], this.vertices[2], this.vertices[3]],    // Una cara entre 4 vertices
        [this.vertices[4], this.vertices[5], this.vertices[6], this.vertices[7]],
        [this.vertices[3], this.vertices[2], this.vertices[5], this.vertices[4]],
        [this.vertices[7], this.vertices[6], this.vertices[1], this.vertices[0]],
        [this.vertices[7], this.vertices[0], this.vertices[3], this.vertices[4]],
        [this.vertices[1], this.vertices[6], this.vertices[5], this.vertices[2]]
    ];
}

// Proyección o punto de vista
function proyeccion(O){             // Le pasamos lo que sea
    var persp = 200;                // persp : perspectiva
    var calculo = persp/O.y;
    return new Vertice2D(calculo*O.x, calculo*O.z);
}

function representacion(objetos, contexto, dx, dy){           // Render
    contexto.clearRect(0, 0, 512, 512);                      // Se borra el canvas anterior
    for(var i=0; i<objetos.length; i++){
        contexto.fillStyle = objetos[i].color;
        for(var j=0, ncaras=objetos[i].caras.length; j<ncaras; ++j){    // ++j -> preincremento
            var cara = objetos[i].caras[j];
            var P = proyeccion(cara[0]);
            contexto.beginPath();
            contexto.moveTo(P.x + dx, -P.y + dy)
            for(var k=0, nvertices=cara.length; k<nvertices; ++k){
                P = proyeccion(cara[k]);
                contexto.lineTo(P.x + dx, -P.y + dy);
            }
            contexto.closePath();
            contexto.stroke();
            contexto.fill();
        }
    }
}



function rotar(O, centro, theta, phi){      // O -> lo que se está rotando
    var ct = Math.cos(theta);
    var st = Math.sin(theta);
    var cp = Math.cos(phi);
    var sp = Math.sin(phi);

    var x = O.x - centro.x;
    var y = O.y - centro.y;
    var z = O.z - centro.z;

    O.x = ct*x - st*cp*y + st*sp*z + centro.x;
    O.y = st*x + ct*cp*y - ct*sp*z + centro.y;
    O.z = sp*y + cp*z +centro.z;

}
function empezarMovimiento(){
    ratonPulsado = true;
    mx = event.clientX;
    my = event.clientY;
}
function mover(){
    if(ratonPulsado){   
        var theta = (event.clientX - mx) * Math.PI/360;     // theta -> movimiento orbital horizontal
        var phi = (event.clientY - my) * Math.PI/180;       // phi -> movimiento orbital vertical

        for(var j=0; j<cubos.length; j++){
            for(var i=0; i<8; ++i){     // 8 vértices
                rotar(cubos[j].vertices[i], centrocubo, theta, phi);
                mx = event.clientX;
                my = event.clientY;
                representacion(objetos, contexto, centrox, centroy);
            }
        }
    }
}
function pararMovimiento(){
    ratonPulsado = false;
}