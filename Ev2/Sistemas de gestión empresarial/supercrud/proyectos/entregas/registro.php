<?php
    
    include "config.php";

    /* // Prevención de ataques a la BD (sacado de 'controlador.php')
    foreach($_REQUEST as $nombre_campo => $valor){  // REQUEST lo atrapa todo
        //echo "El campo es: ".$nombre_campo." y el valor es: ".$valor;
        // Para evitar ataques de inyecciones SQL
        if(preg_match('~\b(delete|drop|truncate)\b~i',$nombre_campo)){
            // 'implode' une elementos de un array en un string
            $volcado = implode(",", $_REQUEST).", ".$_SERVER['REMOTE_ADDR'].", ".$_SERVER['HTTP_USER_AGENT']."\n";  // REMOTE_ADDR guara la ip y HTTP_USER_AGENT el navegador
            $myfile = fopen("volcado.txt", "a");
            fwrite($myfile, $volcado);
            die("Ejecución detenida");
        }
        if(preg_match('~\b(delete|drop|truncate)\b~i',$valor)){
            $volcado = implode(",", $_REQUEST).", ".$_SERVER['REMOTE_ADDR'].", ".$_SERVER['HTTP_USER_AGENT']."\n";
            $myfile = fopen("volcado.txt", "a");
            fwrite($myfile, $volcado);
            die("Ejecución detenida");
        }
    } */

    $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword ,$mydb);

    // Para coger la url (sacado de stackoverflow)
    $url =  "//{$_SERVER['HTTP_HOST']}{$_SERVER['REQUEST_URI']}";
    $escaped_url = htmlspecialchars( $url, ENT_QUOTES, 'UTF-8' );

    $cadena = "";
    foreach($_REQUEST as $nombre_campo => $valor){
        $cadena .= $nombre_campo. ":" .$valor. "|";
    }

    $consulta = "INSERT INTO registros VALUES (NULL, '".date('U')."', '".$url."', '".$_SERVER['REMOTE_ADDR']."', '".$_SERVER['HTTP_USER_AGENT']."', '".$cadena."')";     // Y los lanzamos en una consulta
    //echo $consulta;
    $mysqli->query($consulta);                                          // Metemos la información en la BD
?>