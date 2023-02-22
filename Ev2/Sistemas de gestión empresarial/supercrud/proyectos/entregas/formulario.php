<!doctype html>
<html>
    <head>
        <script src="https://kit.fontawesome.com/d67157ffdf.js" crossorigin="anonymous"></script>
        <style>
            body{font-family:sans-serif; background:rgb(220, 220, 220);} 
            .campo{margin-bottom:20px;}
            .campo label{font-size:2em; padding:0px; margin:0px;}
            .campo p{font-size:1em; padding:0px; margin:0px;}
            .campo input{padding:5px; background:rgb(230, 230, 230); border:none; margin:4px; width: 95%; clear:both;}     
            #formulario{width:50%; background:white; margin:auto; padding:20px; box-shadow:0px 10px 20px rgba(0, 0, 0, 0.4); border-radius:10px; text-align:center;}
            #formulario h1{color:rgb(100, 100, 100); font-size:20px; padding:0px; margin:0px; margin-bottom:20px;}
            #formulario h3{text-align:left; margin:0px; padding:0px;}
            #formulario p{text-align:left; font-size:10px;}
            #formulario input[type="submit"]{
                border:none; padding:10px; width:200px; margin:auto;
            }
            input{transition:all 1s;}   
            .contienecampo input{
                float:left;
                width:97%;
                margin-right:0px;
                height:20px;
                border-radius:5px 0px 0px 5px;
                box-shadow:0px 4px 8px rgba(0, 0, 0, 0.1)inset; /* inset = por dentro */
            }
            .contienecampo .tipocampo{
                float:right;
                width:100%;
                background:rgb(200, 200, 200);
                height:30px;
                line-height:30px;
                border-radius:0px 5px 5px 0px;
            }
            .contienecampo table{width:100%;}
            .clearfix{clear:both;}  /* Borra todas las flotaciones */
        </style> 
    </head>
    <body>
        
        <div id="formulario">
            
            <h1>Introduce los datos en este formulario</h1>
            <p>En este formulario puedes introducir tus datos rellenando aquellos campos que se te piden</p>
            <?php
                include "controlador.php";
                include "codificador.php";
                $miformulario = new Supercontrolador();

                if(isset($_POST['clave']) && $_POST['clave'] = 'procesaformulario'){    // Si es cierto que se está enviando un campo 'clave' y además es cierto que dicho campo es igual a 'procesaformulario'...
                    $miformulario -> procesaformulario("entregas");                     // Procesa el formulario
                }else{                                                                  // Si no es cierto...
                    $miformulario -> formulario("entregas");                            // Muestra el formulario
                }
                //$miformulario -> formulario("entregas");                              // Llama al método 'formulario' que hay en en el controlador
                include "registro.php";
            ?>
        </div>
    </body>
</html>