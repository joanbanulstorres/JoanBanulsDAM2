$("#dimenivel").html(contador_nivel);
$("#dimesubnivel").html("Memoriza"); 
$("#botonjugar").click(function(){
    $("#contenedor").removeClass("difuminado");
    $("#pantallainicial").fadeOut("slow");
    $("#pantallanivel").fadeIn("slow");
    px = 605;
    py = 255;
    inicio();
});
$("#botoninstrucciones").click(function(){
    $("#pantallainicial").fadeOut("slow");
    $("#pantallainstrucciones").fadeIn("slow");
});
$("#botoninstrucciones2").click(function(){
    $("#pantallafinal").fadeOut("slow");
    $("#pantallainstrucciones").fadeIn("slow");
});
$("#botonvolver").click(function(){
    $("#pantallainstrucciones").fadeOut("slow");
    $("#pantallainicial").fadeIn("slow");
});
$("#botoncontinuar").click(function(){
    $("#contenedor").removeClass("difuminado");
    $("#pantallamedio").fadeOut("slow");
    $("#pantallanivel").fadeIn("slow");
});
$("#botonvolveraempezar").click(function(){
    $("#contenedor").removeClass("difuminado");
    $("#pantallamedio").fadeOut("slow");
    $("#dimesubnivel").html("Memoriza");
    $("#pantallanivel").fadeIn("slow");
    reiniciar();
});
$("#botonvolverajugar").click(function(){
    $("#contenedor").removeClass("difuminado");
    $("#pantallafinal").fadeOut("slow");
    $("#pantallanivel").fadeIn("slow");
    $("#dimesubnivel").html("Memoriza");
    reiniciar();
});
$("#botonvolverajugar2").click(function(){
    $("#contenedor").removeClass("difuminado");
    $("#pantallavictoria").fadeOut("slow");
    $("#pantallanivel").fadeIn("slow");
    $("#dimesubnivel").html("Memoriza");
    reiniciar();
});