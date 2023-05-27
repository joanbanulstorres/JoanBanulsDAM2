<?php

    echo $_POST['contenido_campo'];

    /* include "config.php";
    $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword, $mydb);

    $consulta = "SELECT * FROM usuarios WHERE `".$_POST['nombre_campo']."` = '".$_POST['contenido_campo']."'";
    $resultado = $mysqli -> query($consulta);

    $existe = false;
    while($fila = $resultado -> fetch_assoc()){     // Si la consulta devuelve un resultado, significa que existe un registro con el email introducido
        $existe = true;
    }

    if($existe == true){
        echo 'si';
    }else{
        echo 'no';
    } */
 
?>