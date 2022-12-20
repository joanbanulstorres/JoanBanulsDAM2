<?php
    $mysqli = new mysqli("localhost", "docs", "docs", "docs");                  //Conexión a la base de datos
    $consulta = "SELECT * FROM cms";
    $resultado = $mysqli -> query($consulta);
    while($fila = $resultado -> fetch_assoc()){
        $cms[$fila['elemento']] = $fila['contenido'];                           //Metemos la información de la tabla de mysqli en una matriz php
    }
?>
<!doctype html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="Stylesheet" href="inc/estilo.css">
    </head>
    <body>
        <header>
            <h1><?php echo $cms['titulo']?></h1>
            <h2><?php echo $cms['subtitulo']?></h2>
            <nav>
                <ul>
                    <li><a href="?">Inicio</a></li>
                    <li><a href="?p=productos">Productos</a></li>
                    <li><a href="?p=blog">Blog</a></li>
                    <li><a href="?p=contacto">Contacto</a></li>
                </ul>
            </nav>
        </header>
        <main>
            <?php 
                if(isset($_GET['p'])){                                          //Si existe p, haz...
                    include "inc/".$_GET['p'].".php";
                }else{
                    include "inc/inicio.php";
                }
            ?>
        </main>
        <footer>
            <h1><?php echo $cms['copyright']?></h1>
        </footer>
    </body>
</html>