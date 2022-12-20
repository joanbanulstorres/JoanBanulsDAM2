<?php
    include 'bd_config.php';
    $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword ,$mydb);
    $consulta_insertarasig = "INSERT INTO asignaturas VALUES (NULL, '".$_POST['nombredocumento']."','' ,'".$_POST['idasignatura']."')";
    $resultado4_insertarasig = $mysqli->query($consulta_insertarasig);
?>