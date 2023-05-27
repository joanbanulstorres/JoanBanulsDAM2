<!DOCTYPE html>
<html>
    <?php
        session_start();
        include "config.php";
        $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword, $mydb);
    ?>
    <head>
        <script src="https://code.jquery.com/jquery-3.6.4.js" integrity="sha256-a9jBBRygX1Bh5lt8GZjXDzyOB+bWve9EiO7tROUtj/E=" crossorigin="anonymous"></script>
        <meta charset="utf-8">
        <link rel="stylesheet" href="estilo/estilo.css">
        <script src="https://kit.fontawesome.com/d67157ffdf.js" crossorigin="anonymous"></script>
        <title>Sobre nosotros</title>
    </head>
    <body>
        <?php include("header.php") ?>
        <div id="contienesobrenosotros" class="contenedor">
            <h1>Sobre nosotros</h1>
            <p>Limpiadores Medioambientales es un sitio web orientado a la organización de grupos de limpieza para entornos naturales, teniendo como objetivo la conservación y protección del medio ambiente.</p>
        </div>
    </body>
</html>