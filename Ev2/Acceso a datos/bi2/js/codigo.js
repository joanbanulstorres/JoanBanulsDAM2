var peticion = "SELECT ";
var columnas = " * ";
var desde = " FROM ";
var tabla = "";
var condiciones = "";                                                                                   // *NUEVO*
var limite = " LIMIT 1000000000 ";                                                                      // *NUEVO*

$(document).ready(function(){
    $("#seleccionatabla").load("php/cargatablas.php");
    resultadostabla();
    $("#seleccionatabla").change(function(){
        tabla = $(this).val();
        resultadostabla();
        $("#seleccionacampos").load("php/cargacampos.php?tabla=" + tabla);
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
            if($("input[alias='" + seleccionado[i] + "']").val() != "") {                               // *NUEVO*
                columnas += " AS '" + $("input[alias='" + seleccionado[i] + "']").val() + "' ";
            }
            columnas += ",";                                              
        }
        columnas = columnas.slice(0, -1);   // Para quitar la última coma
        resultadostabla();
                                                                                                        // *NUEVO*
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
                                                                                                        // *NUEVO*
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

    // Para que al introducir un alias en un input se actualice la consulta enseguida                   // *NUEVO*
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
                                                                                                        // *NUEVO*
    $("#limite").change(function(){
        limite = " LIMIT " + $(this).val() + " ";
        resultadostabla();
    });
});

function resultadostabla(){
    $("#sql").text(peticion + columnas + desde + tabla + condiciones + limite);
    $("#resultadostabla").load("php/resultadostabla.php?sql=" + encodeURI(peticion + columnas + desde + tabla + condiciones + limite));
}