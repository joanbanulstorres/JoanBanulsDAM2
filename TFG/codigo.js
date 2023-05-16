// Comprueba que todos los campos del formulario de registro estén completados correctamente, en caso contrario muestra un mensaje de error
function enviar_formulario(){
    var inputs = $('.form_input');
    var contador_errores = inputs.length;
    for(var i=0; i<inputs.length; i++){
        // Por cada campo que esté correctamente completado, se resta uno al contador de errores de los campos
        if(inputs[i].value != '' && inputs[i].value != ' ' && inputs[i].getAttribute('data-estado') == 'correcto'){contador_errores--;}
    }
    // Si el contador es 0 (todos los campos están correctamente completados) se elimina el mensaje de error general
    if(contador_errores == 0){
        return true;                
    }else{      // Si algún campo no se ha completado correctamente...                                                                                                          
        // Añade un mensaje de error general
        if(document.contains(document.getElementById("error_form")) == false){      // Si ya hay un mensaje de error, no se añade otro
            $("#enviar_registro").after('<p id="error_form" style="color:red; font-size:12px; margin-bottom:16px">*Completa correctamente todos los campos</p>');
        }
        return false;
    }
}

$(document).ready(function(){

    ///////////////////////// ▼ FORMULARIOS ▼ /////////////////////////

    // Al enfocar un campo, cambia el color de su borde y el color y posición de su placeholder
    $('.form_input').on('focus', function(){
        segunda_clase = "." + $(this).attr('class').split(' ')[1];    // Se obtiene la segunda clase del input seleccionado para ver si es el de nombre, apellidos, email, usuario o contrasena
        $('.form_input' + segunda_clase).css({
            'border': '2px solid var(--color-focalizado)',
            'padding': '14px'
        });
        $('.form_label' + segunda_clase).css({
            'top': '-.15rem',
            'left': '.5rem',
            'color': 'var(--color-focalizado)',
            'font-size': 'var(--fuente-pequena)',
            'font-weight': '500',
            'z-index': '10'
        });
    });

    // Al enfocar el input para la contraseña, cambia el color de su borde y el color y posición de su placeholder
    $('#contrasena').on('focus', function(){
        $(this).css({
            'border': '2px solid var(--color-focalizado)',
            'border-right': 'none',
            'padding': '14px'
        });
        $('#ver_contrasena').css({
            'border': '2px solid var(--color-focalizado)',
            'border-left': 'none', 
        });
        $('#contrasena_label').css({
            'top': '-.15rem',
            'left': '.5rem',
            'color': 'var(--color-focalizado)',
            'font-size': 'var(--fuente-pequena)',
            'font-weight': '500',
            'z-index': '10'
        });
    });

    // Cambio de color del botón de ver contraseña si se pasa el ratón por encima
    $('#ver_contrasena').on('mouseenter', function(){
        $('#icono_ver').attr('src', 'estilo/img/ver2.png');
    }).on('mouseleave', function(){
        $('#icono_ver').attr('src', 'estilo/img/ver1.png');

    // La contraseña sólo es visible si el botón está pulsado
    }).on('mousedown', function(){
        $('input[name=contrasena]').attr('type', 'text');
    }).on('mouseup', function(){
        $('input[name=contrasena]').attr('type', 'password');
    });

    ///////////////////////// ▲ FORMULARIOS ▲ /////////////////////////

    
    ///////////////////////// ▼ FORMULARIO REGISTRO ▼ /////////////////////////
    
    // Cada vez que se cambia el contenido de un campo, se realizan unas comprobaciones y se modifica el atributo personalizado 'estado' según el resultado
    $('#form_registro .form_input, #form_registro #contrasena').on('change', function(){
        console.log("On change");
        switch($(this).attr('id')){
            case "nombre":
                // ▼ comprobar_campo($(this));
                contenido = $(this).val();
                if(contenido == ""){
                    $(this).attr('data-estado', 'vacio');
                }else{
                    if(!contenido.replace(/ /g, "").length == 0){       // Comprueba que una campo no contenga únicamente espacios en blanco           
                        $(this).attr('data-estado', 'correcto');
                    }else{
                        $(this).attr('data-estado', 'incorrecto');
                    }
                }
                // ▲ comprobar_campo();
            break;
            case "apellidos":
                // ▼ comprobar_contenido($(this));
                contenido = $(this).val();
                if(contenido == ""){
                    $(this).attr('data-estado', 'vacio');
                }else{
                    if(!contenido.replace(/ /g, "").length == 0){          
                        $(this).attr('data-estado', 'correcto');
                    }else{
                        $(this).attr('data-estado', 'incorrecto');
                    }
                }
                // ▲ comprobar_contenido();
            break;
            case "email":
                contenido = $(this).val();
                if(contenido == ""){
                    $("#email").attr('data-estado', 'vacio');
                    if(document.contains(document.getElementById('error_email'))){
                        $('#error_email').remove();
                        $('#contieneemail').css('margin-bottom', '30px');
                    }
                }else{   
                    if(!contenido.replace(/ /g, '').length == 0){
                        $.ajax({
                            type: 'POST',
                            url: 'compruebaemail.php',
                            data: {'email': $(this).val()},
                            success: function(resultado){
                                switch(resultado){
                                    case "si":
                                        $('#email').attr('data-estado', 'incorrecto');
                                        if(!document.contains(document.getElementById('error_email'))){
                                            $('#email').css('margin-bottom', '3px');
                                            $('#contieneemail').css('margin-bottom', '22px');
                                            $('#contieneemail').append("<p id='error_email' class='error' style='color:red; font-size:12px;'>*Este email ya está en uso</p>");
                                        }
                                    break;
                                    case "no":
                                        $('#email').attr('data-estado', 'correcto');
                                        if(document.contains(document.getElementById('error_email'))){
                                            $('#error_email').remove();
                                            $('#contieneemail').css('margin-bottom', '30px');
                                        }
                                    break;
                                    default:
                                        console.log("otro resultado");
                                    break;
                                }
                            },
                            error: function(error){
                                alert(error);
                            }
                        });
                    }else{
                        $('#email').attr('data-estado', 'incorrecto');
                    }
                }
            break;
            case "usuario":
                contenido = $(this).val();
                if(contenido == ""){
                    $("#usuario").attr('data-estado', 'vacio');
                    if(document.contains(document.getElementById('error_email'))){
                        $('#error_usuario').remove();
                        $('#contieneusuario').css('margin-bottom', '30px');
                    }
                }else{   
                    if(!contenido.replace(/ /g, "").length == 0){                          
                        $.ajax({
                            type: 'POST',
                            url: 'compruebausuario.php',
                            data: {'usuario': $(this).val()},
                            success: function(resultado){
                                switch(resultado){
                                    case "si":
                                        $("#usuario").attr('data-estado', 'incorrecto');
                                        if(!document.contains(document.getElementById('error_usuario'))){
                                            $('#usuario').css('margin-bottom', '3px');
                                            $('#contieneusuario').css('margin-bottom', '22px');
                                            $('#contieneusuario').append("<p id='error_usuario' class='error' style='color:red; font-size:12px;'>*Este usuario ya está en uso</p>");
                                        }
                                    break;
                                    case "no":
                                        $("#usuario").attr('data-estado', 'correcto');
                                        if(document.contains(document.getElementById('error_usuario'))){
                                            $('#error_usuario').remove();
                                            $('#contieneusuario').css('margin-bottom', '30px');
                                        }
                                    break;
                                    default:
                                        console.log("otro resultado");
                                    break;
                                }
                            },
                            error: function(error){
                                alert(error);
                            }
                        });
                    }else{
                        $('#usuario').attr('data-estado', 'incorrecto');
                    }
                }
            break;
            case 'contrasena':
                contenido = $(this).val();
                if(contenido == ""){
                    $(this).attr('data-estado', 'vacio');
                }else{
                    if(!contenido.replace(/ /g, "").length == 0){       // Comprueba que una campo no contenga únicamente espacios en blanco           
                        $(this).attr('data-estado', 'correcto');
                    }else{
                        $(this).attr('data-estado', 'incorrecto');
                    }
                }
            break;
            default:
                console.log('Otro id');
            break;
        }

        // Cada vez que se cambia el contenido de un campo, se comprueba que errores en todos los campos para eliminar el mensaje de error de formulario (si lo hay)
        setTimeout(function(){      // Para dar tiempo a que se carguen los errores que trabajan con AJAX
            var inputs = $('.form_input');
            var contador_errores = inputs.length;
            for(var i=0; i<inputs.length; i++){
                // Por cada campo que esté correctamente completado, se resta uno al contador de errores de los campos
                if(inputs[i].value != '' && inputs[i].value != ' ' && inputs[i].getAttribute('data-estado') == 'correcto'){contador_errores--;}
            }
            // Si el contador es 0 (todos los campos están correctamente completados) se elimina el mensaje de error general
            if(contador_errores == 0){
                $('#error_form').remove();                
            }
        }, 100);
    });

    // Cada vez que se desenfoca un campo, se modifica su estilo según el valor de su atributo personalizado 'estado'
    $('#form_registro .form_input').on('focusout', function(){
        segunda_clase = "." + $(this).attr('class').split(' ')[1];    // Se obtiene la segunda clase del input seleccionado para ver si es el de nombre, apellidos, email, usuario o contrasena
        switch($(this).attr("data-estado")){
            case "correcto":
                $('.form_input' + segunda_clase).css({
                    'border': '1px solid var(--color-verde-oscuro)'
                });
                $('.form_label' + segunda_clase).css({
                    'color': 'var(--color-verde-oscuro)'
                });
            break;
            case "incorrecto":
                $('.form_input' + segunda_clase).css({
                    'border': '1px solid var(--color-rojo)'
                });
                $('.form_label' + segunda_clase).css({
                    'color': 'var(--color-rojo)'
                });
            break;
            case "vacio":
                $('.form_input' + segunda_clase).css({
                    'border': '1px solid var(--color-base)',
                });
                $('.form_label' + segunda_clase).css({
                    'top': '50%',
                    'left': '10px',
                    'color': 'var(--color-base)',
                    'font-size': 'var(--fuente-normal)',
                    'font-weight': '500',
                    'z-index': '0'
                });
            break;
            default:
                console.log("Otro tipo de valor de estado");
            break; 
        }
        $('.form_input' + segunda_clase).css({
            'padding': '15px'
        });         
    });

    $('#form_registro #contrasena').on('focusout', function(){
        switch($(this).attr("data-estado")){
            case "correcto":
                $($(this)).css({
                    'border': '1px solid var(--color-verde-oscuro)',
                    'border-right' : 'none'
                });
                $("#ver_contrasena").css({
                    'border': '1px solid var(--color-verde-oscuro)',
                    'border-left' : 'none'
                });
                $("#contrasena_label").css({
                    'color' : 'var(--color-verde-oscuro)'
                });
            break;
            case "incorrecto":
                $($(this)).css({
                    'border': '1px solid var(--color-rojo)',
                    'border-right' : 'none'
                });
                $("#ver_contrasena").css({
                    'border': '1px solid var(--color-rojo)',
                    'border-left' : 'none'
                });
                $("#contrasena_label").css({
                    'color' : 'var(--color-rojo)'
                });
            break;
            case "vacio":
                $($(this)).css({
                    'border': '1px solid var(--color-base)',
                    'border-right' : 'none'
                });
                $("#ver_contrasena").css({
                    'border': '1px solid var(--color-base)',
                    'border-left' : 'none'
                });
                $("#contrasena_label").css({
                    'top': '50%',
                    'left': '10px',
                    'color': 'var(--color-base)',
                    'font-size': 'var(--fuente-normal)',
                    'font-weight': '500',
                    'z-index': '0'
                });
            break;
            default:
                console.log("Otro tipo de valor de incorrecto");
            break; 
        }
        $(this).css({
            'padding': '15px'
        });
    });
    
    ///////////////////////// ▲ FORMULARIO REGISTRO ▲ /////////////////////////


    ///////////////////////// ▼ FORMULARIO INICIO DE SESIÓN ▼ /////////////////////////

    $('#form_login .form_input, #form_login #contrasena').on('change', function(){
        // ▼ comprobar_campo($(this));
        contenido = $(this).val();
        if(contenido == ""){
            $(this).attr('data-estado', 'vacio');
        }else{   
            if(!contenido.replace(/ /g, '').length == 0){
                $(this).attr('data-estado', 'correcto');
            }else{
                $(this).attr('data-estado', 'incorrecto');
            }
        }
        // ▲ comprobar_campo(); 
    });

    // Cada vez que se desenfoca un campo, se modifica su estilo según el valor de su atributo personalizado 'estado'
    $('#form_login .form_input').on('focusout', function(){
        segunda_clase = "." + $(this).attr('class').split(' ')[1];
        switch($(this).attr("data-estado")){
            case "correcto":
                $('.form_input' + segunda_clase).css({
                    'border': '1px solid var(--color-base)'
                });
                $('.form_label' + segunda_clase).css({
                    'color': 'var(--color-base)'
                });
            break;
            case "incorrecto":
                $('.form_input' + segunda_clase).css({
                    'border': '1px solid var(--color-rojo)'
                });
                $('.form_label' + segunda_clase).css({
                    'color': 'var(--color-rojo)'
                });
            break;
            case "vacio":
                $('.form_input' + segunda_clase).css({
                    'border': '1px solid var(--color-base)',
                });
                $('.form_label' + segunda_clase).css({
                    'top': '50%',
                    'left': '10px',
                    'color': 'var(--color-base)',
                    'font-size': 'var(--fuente-normal)',
                    'font-weight': '500',
                    'z-index': '0'
                });
            break;
            default:
                console.log("Otro tipo de estado");
            break; 
        }
        $('.form_input' + segunda_clase).css({
            'padding': '15px'
        });         
    });

    $('#form_login #contrasena').on('focusout', function(){
        switch($(this).attr("data-estado")){
            case "correcto":
                $($(this)).css({
                    'border': '1px solid var(--color-base)',
                    'border-right' : 'none'
                });
                $("#ver_contrasena").css({
                    'border': '1px solid var(--color-base)',
                    'border-left' : 'none'
                });
                $("#contrasena_label").css({
                    'color' : 'var(--color-base)'
                });
            break;
            case "incorrecto":
                $($(this)).css({
                    'border': '1px solid var(--color-rojo)',
                    'border-right' : 'none'
                });
                $("#ver_contrasena").css({
                    'border': '1px solid var(--color-rojo)',
                    'border-left' : 'none'
                });
                $("#contrasena_label").css({
                    'color' : 'var(--color-rojo)'
                });
            break;
            case "vacio":
                $($(this)).css({
                    'border': '1px solid var(--color-base)',
                    'border-right' : 'none'
                });
                $("#ver_contrasena").css({
                    'border': '1px solid var(--color-base)',
                    'border-left' : 'none'
                });
                $("#contrasena_label").css({
                    'top': '50%',
                    'left': '10px',
                    'color': 'var(--color-base)',
                    'font-size': 'var(--fuente-normal)',
                    'font-weight': '500',
                    'z-index': '0'
                });
            break;
            default:
                console.log("Otro tipo de valor de estado");
            break; 
        }
        $(this).css({
            'padding': '15px'
        });
    });

    ///////////////////////// ▲ FORMULARIO INICIO DE SESIÓN ▲ /////////////////////////
});