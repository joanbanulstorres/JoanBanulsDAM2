<?php
    //session_start();
    include "bd_config.php";
    $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword, $mydb);

    $consulta = "SELECT * FROM usuarios WHERE user = '".$_POST['user']."' AND password = '".$_POST['password']."'";
    
    $resultado = $mysqli->query($consulta);

    $pasas = false;

    while($fila = $resultado->fetch_assoc()){
        $pasas = true;
        $_SESSION['user'] = $fila['user'];
    }
    if($pasas == true){
        echo "Los datos introducidos son correctos. Dirigiendo a la aplicación...";
        echo '<meta http-equiv="Refresh" content="3; url=index.php"/>';        // Si los datos son correctos, dirije a la página principal
    }else{
        echo "Los datos introducidos son incorrectos. Redirigiendo al formulario...";
        echo '<meta http-equiv="Refresh" content="3; url=formulario.php"/>';   // Si los datos son incorrectos, redirije al formulario
    }
?>