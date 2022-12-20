<?php
    error_reporting(E_ALL ^ E_NOTICE); 
    $path = 'documento/vault/users/'.$_GET['user']."/";     // *NUEVO* - La carpeta que se lee depende del usuario que se haya registrado
    // Sacado de internet 'php list all files in directory'
    if($handle = opendir($path)){
        while (false !== ($entry = readdir($handle))) {
            if ($entry != "." && $entry != "..") {
                echo "<div class ='item' filetype='".explode(".", $entry)[1]."'filename='".$entry."'>";  // Dividimos el array en dos a partir del punto y nos quedamos con la segunda parte, la extensión
                // Averiguamos si el archivo es una carpeta
                if(is_dir($path.'/'.$entry)){
                    echo "<div class='iconfolder'><img src='img/bootstrap-icons-1.9.1/folder.svg'></div>";
                }else{
                    echo "<div class='iconfile'><img src='img/bootstrap-icons-1.9.1/filetype-".explode(".", $entry)[1].".svg'></div>";  
                }
                echo "
                <span class='documentname'>".$entry."</span>
                </div>";
            }
        }
        closedir($handle); 
    }
?>