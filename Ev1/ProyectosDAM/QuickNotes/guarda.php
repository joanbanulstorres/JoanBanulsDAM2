<?php
    $myfile = fopen("E:/nuevoxampp/htdocs/ProyectosDAM/QuickNotes/vault/users/joan/Desarrollo de aplicaciones multiplataforma/".$_POST['idasignatura']."/".$_POST['nombredocumento'].".html", "w") or die("No ha sido posible abrir el archivo");
    $txt = $_POST['datos'];
    fwrite($myfile, $txt);
    fclose($myfile);
?>