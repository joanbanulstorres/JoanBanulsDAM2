<?php
    session_start();    // *NUEVO*
    $myfile = fopen("E:/nuevoxampp/htdocs/documentos/documento/vault/users/".$_SESSION['user']."/".$_POST['nombredocumento'].".html", "w") or die("Unable to open file!");
    $txt = $_POST['datos'];
    fwrite($myfile, $txt);
    fclose($myfile);
?>