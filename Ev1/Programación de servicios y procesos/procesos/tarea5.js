 //Solo se envía un un postMessage cuando se recibe un onmessage
onmessage = function(datos){
    //Cálculo 1
    console.log(datos);
    console.log("Tu edad es: " + datos.data.edad);
    console.log("Tu nombre es: " + datos.data.nombre)
    console.log("Vamos con un cálculo");
    var numero = 0.000004423423;
    var iteraciones = 1000000000;
    for(var i =0; i<iteraciones; i++){
        numero = numero*1.00000000005435
    }
    postMessage(numero); //postMessage desde la tarea envía un mensaje al trabajador
}
