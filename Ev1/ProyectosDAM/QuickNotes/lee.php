<?php
    $myfile = fopen("E:/nuevoxampp/htdocs/ProyectosDAM/QuickNotes/vault/users/joan/Desarrollo de aplicaciones multiplataforma/".$_POST['idasignatura']."/".$_POST['nombredocumento'], "r") or die("No ha sido posible abrir el archivo");
    // Output one line until end-of-file
    while(!feof($myfile)) { // 'feof' comprueba si el puntero a un archivo está al final del archivo
      echo fgets($myfile) . "<br>";
    }
    fclose($myfile);
?>