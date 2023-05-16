<?php

    session_start();

    include "config.php";

    $mysqli = new  mysqli($mydbserver, $mydbuser, $mydbpassword, $mydb);
    $consulta = "SELECT * FROM usuarios WHERE `usuario` = '".$_POST['usuarioemail']."' OR `email` = '".$_POST['usuarioemail']."' AND `contrasena` = '".$_POST['contrasena']."'";
    $resultado = $mysqli -> query($consulta);

    $fila = $resultado->fetch_assoc();
    $_SESSION['usuario'] = $fila['usuario'];

    /* if(preg_match('~\b(delete|drop|truncate)\b~i', $_POST['usuario']) || preg_match('~\b(delete|drop|truncate)\b~i', $_POST['contrasena'])){
        echo '<p style="font-family:sans-serif; color:red">Se ha intentado modificar el contenido de la BD</p>';
    } */
    
    $pasas = false;
    if(mysqli_num_rows($resultado) > 0){    // Si la consulta devuelve un resultado, significa que existe un registro con el usuario y la contraseña introducidos
        $pasas = true;
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