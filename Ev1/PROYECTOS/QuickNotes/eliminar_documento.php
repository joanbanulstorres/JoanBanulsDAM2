<?php
    include 'bd_config.php';
    $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword ,$mydb);
    $consulta_eliminardoc = "DELETE FROM documentos WHERE nombredocumento = '".$_POST['nombredocumento']."'";
    $resultado_eliminardoc = $mysqli->query($consulta_eliminardoc);
?>