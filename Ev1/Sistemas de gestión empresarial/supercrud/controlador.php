<?php
    error_reporting(E_ALL ^ E_NOTICE); 
    class Supercontrolador{                                                 
        function formulario($tabla){                                        
            include "config.php";
            echo '<form action="?" method="POST">';
            echo '<input type="hidden" name="clave" value="procesaformulario">';    // Si no hay una clave 'procesaformulario' enséñame el formulario, pero si la hay, pasa a procesar el formulario
            echo '<input type="hidden" name="tabla" value="'.$tabla.'">';           
            
            $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword ,$mydb);     // - Cambiamos los campos según 'config.php'
            
            // Luego quiero ver las columnas
            $consulta = "SHOW FULL COLUMNS FROM ".$tabla;
            $resultado = $mysqli->query($consulta);
            while($fila = $resultado->fetch_assoc()){
                if(json_decode($fila["Comment"])->visible == "true"){   // Para ocultar la clave primaria  - Ocultamos el 'epoch'
                    // *NUEVO* - json_decode, mínimo y máximo de caracteres
                    preg_match('#\((.*?)\)#', $fila["Type"], $match);
                    echo '
                        <div class="campo">
                            <h3>'.json_decode($fila["Comment"])->titulo.'</h3> 
                            <p>'.json_decode($fila["Comment"])->descripcion.' - Caracteres mínimos '.json_decode($fila["Comment"])->min.' máximos '.$match[1].'</p>
                            '; 
                            if($fila["Null"] == "NO"){echo "<p>*Este campo es requerido</p>";}
                            
                            echo'
                            <div class="contienecampo">
                                <table><tr><td width="80%">
                                    <input type="'.json_decode($fila["Comment"])->tipodato.'" name="'.$fila["Field"].'" id="'.$fila["Field"].'"
                                        ';
                                        if($fila["Null"] == "NO"){echo " required ";}
                                        if(json_decode($fila["Comment"])->deshabilitado == "true"){echo " readonly ";}
                                        //if($fila["Field"] == "epoch"){echo " disabled ";}
                                        // Para definir el máximo de caracteres en cada campo
                                        preg_match('#\((.*?)\)#', $fila["Type"], $match);
                                        echo '
                                        maxlength = "'.$match[1].'"
                                        minlength = "'.json_decode($fila["Comment"])->min.'"
                                        placeholder = "'.json_decode($fila["Comment"])->placeholder.'"
                                        ';
                                        //Para el código de la asignatura
                                        if(isset(json_decode($fila["Comment"])->parametroget)){
                                            echo 'value = "'.$_GET[json_decode($fila["Comment"])->parametroget].'"';
                                        }
                                        echo '
                                    >
                                    </td><td>
                                <div class="tipocampo"><i class="'.json_decode($fila["Comment"])->icono.'"></i></div>
                                </td><tr></table>
                            </div>
                            <div class="clearfix"></div>
                        </div>
                        
                    ';  // El 'clearfix' borra todas las flotaciones                                                   
                }
            }

            echo '<input type="submit">';
            $mysqli -> close();
        }
        function procesaformulario(){   
            // *NUEVO*
            // Vamos a analizar qué es lo que viene antes de meterlo
            foreach($_REQUEST as $nombre_campo => $valor){  // REQUEST lo atrapa todo *NUEVO*
                //echo "El campo es: ".$nombre_campo." y el valor es: ".$valor;
                // Para evitar ataques de inyecciones SQL *NUEVO*
                if(preg_match('~\b(delete|drop|truncate)\b~i',$nombre_campo)){
                    // 'implode' une elementos de un array en un string
                    $volcado = implode(",", $_REQUEST).", ".$_SERVER['REMOTE_ADDR'].", ".$_SERVER['HTTP_USER_AGENT']."\n";  // REMOTE_ADDR guara la ip y HTTP_USER_AGENT el navegador
                    $myfile = fopen("volcado.txt", "a");
                    fwrite($myfile, $volcado);
                    die("Ejecución detenida");
                }
                if(preg_match('~\b(delete|drop|truncate)\b~i',$valor)){
                    $volcado = implode(",", $_REQUEST).", ".$_SERVER['REMOTE_ADDR'].", ".$_SERVER['HTTP_USER_AGENT']."\n";
                    $myfile = fopen("volcado.txt", "a");
                    fwrite($myfile, $volcado);
                    die("Ejecución detenida");
                }
            }
            
            include "config.php";
            $listadocolumnas = "";
            $listadovalores = "";
            foreach($_POST as $nombre_campo => $valor){
                //echo "Recibo el campo ".$nombre_campo." con el valor ".$valor."<br>";
                if($nombre_campo != 'tabla' && $nombre_campo != 'clave'){   // Metemos los valores del POST en una cadena...
                    $listadocolumnas .= ",".$nombre_campo."";
                    $listadovalores   .= ",'".$valor."'";     
                }
            }
            $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword ,$mydb);
            $consulta = "INSERT INTO ".$_POST['tabla']." (Identificador".$listadocolumnas.") VALUES (NULL".$listadovalores.")";     // Y los lanzamos en una consulta
            //echo $consulta;

            $mysqli->query($consulta);                                          // Metemos la información en la BD
            echo '
                <div class="notice">
                    <h1>Registro guardado correctamente</h1>
                    <p>Tu registro se ha guardado correctamente en la aplicación. Redirigiendo en 5 segundos...</p>
                </div>
            ';
            echo '<meta http-equiv="refresh" content="5"; url=?/>';
             
        }
    }
?>


    

