<?php
    include 'bd_config.php';
    $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword ,$mydb);
    $consulta_insertardoc = "INSERT INTO documentos VALUES (NULL, '".$_POST['nombredocumento']."','' ,'".$_POST['idasignatura']."')";
    $resultado_insertardoc = $mysqli->query($consulta_insertardoc);
?>