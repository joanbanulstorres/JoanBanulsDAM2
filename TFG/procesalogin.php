<?php

    //error_reporting(E_ALL ^ E_NOTICE);
    session_start();
    include "config.php";
    $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword, $mydb);

    $consulta = "SELECT * FROM usuarios WHERE (`usuario` = '".$_POST['usuarioemail']."' OR `email` = '".$_POST['usuarioemail']."') AND `contrasena` = '".$_POST['contrasena']."'";
    $resultado = $mysqli -> query($consulta);

    $fila = $resultado->fetch_assoc();

    /* if(preg_match('~\b(delete|drop|truncate)\b~i', $_POST['usuario']) || preg_match('~\b(delete|drop|truncate)\b~i', $_POST['contrasena'])){
        echo '<p style="font-family:sans-serif; color:red">Se ha intentado modificar el contenido de la BD</p>';
    } */
    
    $pasas = false;
    if(mysqli_num_rows($resultado) > 0){    // Si la consulta devuelve un resultado, significa que existe un registro con el usuario y la contraseña introducidos
        $pasas = true;
        $_SESSION['usuario'] = $fila['usuario'];

        // Se averigua el id del usuario y se define como id de la sesión
        $consulta_id = "SELECT * FROM usuarios WHERE usuario = '".$_SESSION['usuario']."'";
        $resultado_id = $mysqli -> query($consulta);
        $fila_id = $resultado_id -> fetch_assoc();
        $_SESSION['id_usuario']  = $fila_id['Identificador'];
    }

    if($pasas == true){
        header('refresh:0; url=index.php');
    }else{
        echo '
        <html>
            <head>
                <meta charset="utf-8">
                <title>Crear cuenta</title>
                <link rel="stylesheet" href="estilo/estilo.css">
            </head>
            <body>
                <div id="contieneformulario">
                    <h3>Datos de acceso incorrectos</h3>
                </div>
            </body>
        </html>
        ';
        header('refresh:3; url=login.php');
    }

?>