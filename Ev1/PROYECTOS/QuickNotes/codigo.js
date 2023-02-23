$(document).ready(function(){
    
    
    
    $("#asignaturas").accordion();
    $("#dialog").dialog();
    
    $(".editar").click(function(){
        ////////// ▽ NOMBRE DEL DOCUMENTO EN NEGRITA ▽ //////////
        var nombres_documento = document.getElementsByClassName("nombre");      // Se crea un array con todos los elementos que sean un nombre
        for(var i=0; i<nombres_documento.length; i++){
            //console.log(nombres_documento[i]);
            nombres_documento[i].style.setProperty("font-weight", "normal");    // Se cambia la letra de cada uno de esos elementos
        }
        
        // Ahora se cambia la letra del documento seleccionado a negrita
        var miDocumento = $(this).attr("class").split(' ')[1];                  // Se parte el atributo clase en 2 ya que se va a trabajar con la segunda ('nombredocumento')
        var arrayclase = document.getElementsByClassName(miDocumento);          // Se crea un array con los elementos que comparten clase con el botón pulsado
        arrayclase[0].style.setProperty("font-weight", "bold");                 // Se modifica el primer elemento del array, es decir, el nombre del documento
        ////////// △ NOMBRE DEL DOCUMENTO EN NEGRITA △ //////////
        
        ////////// ▽ DECLARACIÓN DEL DOCUMENTO Y ASIGNATURA ACTUAL ▽ //////////
        // Se declara el documento seleccionado como documento actual
        documento_actual = miDocumento;
        document.getElementById("documentoactual").value = documento_actual;
        console.log(document.getElementById("documentoactual").value);
        
        // Se declara la asignatura del documento seleccionado como actual
        var asignatura_actual = $(this).attr("class").split(' ' + documento_actual + ' ')[1];
        document.getElementById("asignaturaactual").value = asignatura_actual;
        ////////// △ DECLARACIÓN DEL DOCUMENTO Y ASIGNATURA ACTUAL △ //////////
        
        ////////// ▽ SE MUESTRA EL CONTENIDO DEL DOCUMENTO SELECCIONADO ▽ //////////
        // Borra el contenido del documento
        document.getElementById("pagina").innerHTML = "";
        // Carga el contenido del documento seleccionado
        
//        $.ajax({
//            url: "lee.php",
//            data: {nombredocumento: $("#documentoactual").val(), idasignatura: $("#asignaturaactual").val()},
//            type: "POST",
//            sucess: function(result){
//                console.log("OK" + result);
///           }
//            return:result},
//        });
        ////////// △ SE MUESTRA EL CONTENIDO DEL DOCUMENTO SELECCIONADO △ //////////
    });
    
    // Esta función elimina un documento al hacer click sobre un botón
    $(".eliminar").click(function(){
        // Declaración del documento actual
        var miDocumento = $(this).attr("class").split(' ')[1];
        documento_actual = miDocumento;
        document.getElementById("documentoactual").value = documento_actual;
        console.log(document.getElementById("documentoactual").value);
        
        $.ajax({
            url: "eliminar_documento.php",
            data: {nombredocumento: $("#documentoactual").val()},
            type: "POST",
            sucess: function(result){
                console.log("OK" + result);
            }
        });
    });
    
    // Esta función crea un documento al hacer click sobre un botón
    $(".nuevodocumento").click(function(){
        if(nuevodoc_habilitado == true){
            nuevodoc_habilitado = false;
            // Se obtiene el id del la asignatura sobra la que se ha hecho click
            var asignatura_actual = $(this).attr("class").split(' ')[1];
            document.getElementById("asignaturaactual").value = asignatura_actual;
            
            $(".nuevodoc " + asignatura_actual).append("<div id='dialog' title='Nuevo documento'>"+
                "<br><input id='nombrenuevodoc' placeholder='Introduce un nombre'>"+
                "<button id='enviarnombredoc'><img src='estilo/bootstrap-icons-1.9.1/file-earmark-check.svg'></button>"
            );
    //        $.ajax({
    //            url: "insertar_documento.php",
    //            data: {nombredocumento: $("#documentoactual").val(), idasignatura: $("#asignaturaactual").val()},
    //            type: "POST",
    //            succes: function(result){
    //                console.log("OK" + result);
    //            }
    //        });
        }
    });
    
    // Esta función la asignatura seleccionada una asignatura al hacer click sobre un botón
    $(".eliminarasignatura").click(function(){
        // Se obtiene el id del la asignatura sobra la que se ha hecho click
        var asignatura_actual = $(this).attr("class").split(' ')[1];
        document.getElementById("asignaturaactual").value = asignatura_actual;
        $.ajax({
            url: "eliminar_asignatura.php",
            data: {idasignatura: $("#asignaturaactual").val()},
            type: "POST",
            sucess: function(result){
                console.log("OK" + result);
            }
        });
    });
    
    // Esta función crea y o guarda un documento al hacer click sobre un botón
    $("#guardar").click(function(){
        //console.log(documento_actual);
        $.ajax({
            url: "guarda.php",
            data: {datos: $("#pagina").html(), nombredocumento: $("#documentoactual").val(), idasignatura: $("#asignaturaactual").val()},
            type: "POST",
            sucess: function(result){
                console.log("OK" + result);
            }
        });
    });
    
    // Estas funciones crean una asignatura al hacer click sobre un botón
    $("#nuevaasignatura").click(function(){
        if(nuevaasig_habilitada == true){
            nuevaasig_habilitada = false;
            $(".nuevaasig").append("<br><input id='nombrenuevaasig' value='' placeholder='Introduce un nombre'>"+
                                   "<button id='enviarnombreasig'><img src='estilo/bootstrap-icons-1.9.1/plus-circle.svg'></button>"
            );

        }
    });
    $("#enviarnombreasig").click(function(){
        console.log("Enviar");
        console.log(document.getElementById("nombrenuevaasig").value);
//            $.ajax({
//                url: "insertar_asignatura.php",
//                data: {nombrenuevaasignatura: },
//                type: "POST",
//                sucess: function(result){
//                    console.log("OK" + result);
//                }
//            });
    });
    
    
    
    $("#tipotexto").change(function(){
        $("#pagina").append("<"+$(this).val()+">"+$(this).val()+"</"+$(this).val()+">");
    });
    $("#selectfont").change(function(){
        $("#pagina").append("<span style='font-family:"+$(this).val()+"'>"+$(this).val()+"</span>");
    });
    $("#fontsize").change(function(){
        $("#pagina").append("<span style='font-size:"+$(this).val()+"px'>"+$(this).val()+"</span>");
    });
    $("#bold").click(function(){
        $("#pagina").append("<span style='font-weight:bold'>Negrita</span>");
    });
    $("#cursive").click(function(){
        $("#pagina").append("<span style='font-style:cursive'>Cursiva</span>");
    });
    $("#underline").click(function(){
        $("#pagina").append("<span style='text-decoration:underline'>Subrayado</span>");
    });
    $("#fontcolor").change(function(){
        $("#pagina").append("<span style='color:"+$(this).val()+"'>"+$(this).val()+"</span>");
    });
    $("#orderedlist").click(function(){
        $("#pagina").append("<ol><li></li></ol>");
    });
    $("#unorderedlist").click(function(){
        $("#pagina").append("<ul><li></li></ul>");
    });
    $("#alignleft").click(function(){
        $("#pagina").append("<div style='text-align:left'>Texto alineado a la izquierda<br><br></div>");
    });
    $("#alignright").click(function(){
        $("#pagina").append("<div style='text-align:right'>Texto alineado a la derecha<br><br></div>");
    });
    $("#aligncenter").click(function(){
        $("#pagina").append("<div style='text-align:center'>Texto centrado<br><br></div>");
    });
    $("#alignjustify").click(function(){
        $("#pagina").append("<div style='text-align:justify'>Texto justificado<br><br></div>");
    });
    
    var nuevozoom = 130;
    $("#zoomin").click(function(){
        nuevozoom += 10;
        document.getElementById("pagina").style.setProperty("zoom", nuevozoom + "%");
        document.querySelector("nav").style.setProperty("height", nuevozoom + "%");
        document.querySelector("main").style.setProperty("height", nuevozoom+ "%");
    });
    $("#zoomout").click(function(){
        nuevozoom -= 10;
        document.getElementById("pagina").style.setProperty("zoom", nuevozoom + "%");
        document.querySelector("nav").style.setProperty("height", nuevozoom + "%");
        document.querySelector("main").style.setProperty("height", nuevozoom+ "%");
    }); 
});