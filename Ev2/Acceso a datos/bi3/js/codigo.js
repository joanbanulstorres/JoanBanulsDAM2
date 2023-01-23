var peticion = "SELECT ";
var columnas = " * ";
var desde = " FROM ";
var tabla = "";
var condiciones = "";                                                                                   
var limite = " LIMIT 1000000000 ";
var ordenar = "";                                                                                       // *NUEVO*                                                

$(document).ready(function(){
    $("#formulario").accordion({
        heightStyle: "content"
    });
    $("#seleccionatabla").load("php/cargatablas.php");
    resultadostabla();
    $("#seleccionatabla").change(function(){
        tabla = $(this).val();
        resultadostabla();
        $("#seleccionacampos").load("php/cargacampos.php?tabla=" + tabla);
        $("#seleccionaordenar").load("php/cargaordenar.php?tabla=" + tabla);                             // *NUEVO*
    });
    
    $("#seleccionaordenar").change(function(){                                                           // *NUEVO*
        seleccionado = [];
        $('input[name="seleccionaordenar"]').each(function(){
            if($(this).is(":checked")){
                seleccionado.push($(this).val());
            }
        });
        ordenar = " ORDER BY ";
        for(var i=0; i<seleccionado.length; i++){
            ordenar += seleccionado[i] + ",";
        }
        ordenar = ordenar.slice(0, -1);   // Para quitar la última coma
        ordenar += " ";
        console.log(ordenar);
        resultadostabla();
    });
    
    $("#seleccionacampos").change(function(){
        seleccionado = [];
        $('input[name="seleccionacampos"]').each(function(){
            if($(this).is(":checked")){
                seleccionado.push($(this).val());
            }
        });
        columnas = "";
        for(var i=0; i<seleccionado.length; i++){
            columnas += seleccionado[i] + " ";
            if($("input[alias='" + seleccionado[i] + "']").val() != "") {                              
                columnas += " AS '" + $("input[alias='" + seleccionado[i] + "']").val() + "' ";
            }
            columnas += ",";                                              
        }
        columnas = columnas.slice(0, -1);   // Para quitar la última coma
        resultadostabla();
                                                                                                    
        // Para introducir las condiciones                                                                                                
        $("#seleccionacondiciones").html("");                                                            
        for(var i=0; i<seleccionado.length; i++){                                       
            $("#seleccionacondiciones").append('<tr class="condicion"><td>' + seleccionado[i] + '=</td><td><input type="text" name="" class="nuevacondicion" campo="' + seleccionado[i] + '"></td></tr><br>')
        }
        // Para introducir los alias                                                                                                
        $("#seleccionaalias").html("");                                                            
        for(var i=0; i<seleccionado.length; i++){                                       
            $("#seleccionaalias").append('<tr class="alias"><td>' + seleccionado[i] + '=</td><td><input type="text" name="" class="nuevoalias" alias="' + seleccionado[i] + '" campo="' + seleccionado[i] + '"></td></tr><br>')
        }
    });
                                                                                                        
    //$(".nuevacondicion").change(function(){                                                           // No podemos usar '.change' porque '.nuevacondicion' es un elemento creado dinámicamente...                                                             
    $(document).on("keydown", ".nuevacondicion", function(){                                            // por tanto, tenemos que usar '.on' 
        condiciones = " WHERE ";
        $(".nuevacondicion").each(function(){
            if($(this).val() != ""){
                condiciones += $(this).attr('campo') + " LIKE '%" + $(this).val() + "%' & ";
            }
        });
        //condiciones = condiciones.slice(0, -1);
        resultadostabla();
    });

    // Para que al introducir un alias en un input se actualice la consulta enseguida                   
    //$(".nuevacondicion").change(function(){                                                                                                                    
    $(document).on("keydown", ".nuevoalias", function(){                                                 
        seleccionado = [];
        $('input[name="seleccionacampos"]').each(function(){
            if($(this).is(":checked")){
                seleccionado.push($(this).val());
            }
        });
        // Para introducir los alias                                                                                                
        columnas = "";
        for(var i=0; i<seleccionado.length; i++){
            columnas += seleccionado[i] + " ";
            if($("input[alias='" + seleccionado[i] + "']").val() != "") {
                columnas += " AS '" + $("input[alias='" + seleccionado[i] + "']").val() + "' ";
            }
            columnas += ",";                                              
        }
        columnas = columnas.slice(0, -1);   // Para quitar la última coma
        
        resultadostabla();
    });
                                                                                                        
    $("#limite").change(function(){
        limite = " LIMIT " + $(this).val() + " ";
        resultadostabla();
    });
});

function resultadostabla(){
    sentencia = peticion + columnas + desde + tabla + condiciones + ordenar + limite;                   // *NUEVO* - + ordenar
    $("#sql").text(sentencia);
    $("#resultadostabla").load("php/resultadostabla.php?sql=" + encodeURI(sentencia));
}