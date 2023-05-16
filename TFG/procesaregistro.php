<?php

    include "config.php";

    $mysqli = new  mysqli($mydbserver, $mydbuser, $mydbpassword, $mydb);
    $consulta = "SELECT * FROM usuarios WHERE `email` = '".$_POST['email']."' OR `usuario` = '".$_POST['usuario']."'";
    $resultado = $mysqli -> query($consulta);

    $existe = false;
    if(mysqli_num_rows($resultado) > 0){    // Si la consulta devuelve un resultado, significa que existe un registro con el email introducido
        $existe = true;
    }

    if($existe == false){
        $consulta2 = " INSERT INTO usuarios (
                                                `Identificador`,
                                                `nombre`,
                                                `apellidos`,
                                                `email`,
                                                `usuario`,
                                                `contrasena`
                                            ) 
                                    VALUES (
                                                NULL,
                                                '".$_POST['nombre']."',
                                                '".$_POST['apellidos']."',
                                                '".$_POST['email']."',
                                                '".$_POST['usuario']."',
                                                '".$_POST['contrasena']."'
                                            )
        ";
        $mysqli->query($consulta2);

        session_start();
        $_SESSION['usuario'] = $_POST['usuario'];

        echo '
        <html>
            <head>
                <meta charset="utf-8">
                <title>Crear cuenta</title>
                <link rel="stylesheet" href="estilo/estilo.css">
            </head>
            <body>
                <div id="contenedor">
                    <div id="contieneformulario">
                        <h3>Te has registrado correctamente. Redirigiendo a la página principal...</h3>
                    </div>
                </div>
            </body>
        </html>
        ';
        header('refresh:3; url=index.php');
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
                    <h3 style="color: red;">Ya existe un registro con el usuario o email introducidos</h3>
                </div>
            </body>
        </html>
        ';
        header('refresh:3; url=registro.php');
    }

?>