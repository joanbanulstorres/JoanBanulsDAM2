<?php
    include 'bd_config.php';
    $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword ,$mydb);
    $consulta_eliminarasig = "DELETE FROM asignaturas WHERE Idasignatura = '".$_POST['idasignatura']."'";
    $resultado_eliminarasig = $mysqli->query($consulta_eliminarasig);
?>