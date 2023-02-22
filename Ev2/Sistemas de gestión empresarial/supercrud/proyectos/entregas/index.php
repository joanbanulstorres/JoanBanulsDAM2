<?php
    session_start();
    include "../config.php"; 
    include "../controlador.php";
    $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword, $mydb);
    $miformulario = new Supercontrolador();
?>
<html>
    <head>
        <meta charset="utf-8">
        <style>
            /* ESTILOS GENERALES */
            body, html{height:100%; background:rgb(220, 220, 220); font-family:sans-serif; padding:0px; margin:0px;}
            /* ESTILOS DEL FORMULARIO DE LOGIN */
            #formulariologin{width:200px; height:200px; background:white; margin:auto; padding:30px; border-radius:20px; text-align:center;}
            #formulariologin input{width:100%; padding-top:10px; padding-bottom:10px; border:0px; margin-top:10px; outline:none; background:rgb(240, 240, 240); border-radius:5px;}
            #formulariologin input[type="text"], #formulariologin input[type="password"]{box-shadow:0px 4px 8px rgba(0, 0, 0, 0.3) inset;}
            #formulariologin input[type="submit"]{box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);}
            .notice{position:absolute; top:0px; width:400px; background:red; color:white; height:20px; left:50%; margin-left:-200px; padding:10px; text-align:center;}
            aside{width:20%; height:100%; float:left; box-shadow:-20px 0px 20px rgba(0, 0, 0, 0.3) inset;}
            /* ESTILOS DEL PANEL DE CONTROL */
            section{width:80%; height:100%; float:right;}
            #contienemenu{padding:10px;}
            #contienemenu ul{list-style-type:none; padding:0px; margin:0px}
            #contienemenu ul li{padding:10px; margin:0px; border-bottom:1px solid grey;}
            #contienemenu ul li a{color:inherit; text-decoration:none;}
            #contienecontenido{padding:10px;}
            #contienecontenido table{width:100%;}
        </style>
    </head>
    <body>

        <?php
		echo "oook";
            if(isset($_POST['usuario'])){         
                $consulta = "SELECT * FROM usuarios WHERE usuario = '".$_POST['usuario']."' AND contrasena = '".$_POST['contrasena']."'";
                $resultado = $mysqli->query($consulta);
                $pasas = "no";
                while($fila = $resultado->fetch_assoc()){
                    $pasas = "si";
                    $_SESSION['usuario'] = $fila['usuario'];
					echo "ok has pasado";
                }
                if($pasas == "si"){}else{
                    echo '<div class="notice">Intento de acceso denegado</div>';
                }
            }
        ?>
        <?php
            if(isset($_SESSION['usuario'])){
                var_dump($_SESSION['usuario']);
                echo '
                    <aside>
                        <div id="contienemenu"><ul>';
                        $consulta = "SHOW TABLES";
                        $resultado = $mysqli->query($consulta);
                        while($fila = $resultado->fetch_array()){
                            echo '<li><a href="?tabla='.$fila[0].'">'.$fila[0].'</a></li>';
                        }
                        echo '</ul>
                        </div>
                    </aside>
                    <section>
                        <div id="contienecontenido">
                            ';
                                if(isset($_GET['tabla'])){
                                    echo '<script>console.log("Mostrando el contenido de la tabla seleccionada");</script>';
                                    echo "Contenido de la tabla: ".$_GET['tabla'];
                                    $miformulario -> leer($_GET['tabla']);
                                }else{
                                    echo '<script>console.log("No se ha seleccionado una tabla");</script>';
                                    echo "No se ha seleccionado una tabla"; 
                                }
                                
                            echo '
                        </div>
                    </section>
                ';
            }else{
                echo '
                    <form action= "?" method="POST" id="formulariologin">
                        <input type="text" name="usuario" placeholder="usuario">
                        <input type="password" name="contrasena" placeholder="contraseña">
                        <input type="submit">
                    </form>
                ';
            }
        ?>

    </body>
</html>