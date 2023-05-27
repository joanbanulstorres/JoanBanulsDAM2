<?php

    include "config.php";

    $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword, $mydb);
    $consulta = "SELECT * FROM usuarios WHERE `usuario` = '".$_POST['usuarioemail']."' OR `email` = '".$_POST['usuarioemail']."'";
    $resultado = $mysqli -> query($consulta);

    $existe = false;
    if(mysqli_num_rows($resultado) > 0){    // Si la consulta devuelve un resultado, significa que existe un registro con el email introducido
        $existe = true;
    }

    if($existe == true){
        echo 'si';
    }else{
        echo 'no';
    }
 
?>