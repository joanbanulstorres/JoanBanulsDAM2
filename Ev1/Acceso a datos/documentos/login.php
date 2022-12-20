<?php
    session_start();
    $mysqli = new mysqli("localhost", "documentos", "documentos", "documentos");

    $consulta = "SELECT * FROM usuarios WHERE user = '".$_POST['user']."' AND password = '".$_POST['password']."'";
    
    $resultado = $mysqli->query($consulta);

    $pasas = false;

    while($fila = $resultado->fetch_assoc()){
        $pasas = true;
        $_SESSION['user'] = $fila['user'];
    }
    if($pasas == true){
        echo "Los datos introducidos son correctos. Dirigiendo a la aplicación...";
        echo '<meta http-equiv="Refresh" content="3; url=documentos.php" />';  // Si los datos son correctos, dirije a la página principal
    }else{
        echo "Los datos introducidos son incorrectos.";
        echo '<meta http-equiv="Refresh" content="3; url=index.php" />';     // Si los datos son incorrectos, redirije al formulario
    }
?>