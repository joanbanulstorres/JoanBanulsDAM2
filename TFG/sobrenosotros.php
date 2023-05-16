<!DOCTYPE html>
<html>
    <?php
        session_start();
        include "config.php";
        $mysqli = new  mysqli($mydbserver, $mydbuser, $mydbpassword, $mydb);
    ?>
    <head>
        <script src="https://code.jquery.com/jquery-3.6.4.js" integrity="sha256-a9jBBRygX1Bh5lt8GZjXDzyOB+bWve9EiO7tROUtj/E=" crossorigin="anonymous"></script>
        <meta charset="utf-8">
        <link rel="stylesheet" href="estilo/estilo.css">
        <script src="https://kit.fontawesome.com/d67157ffdf.js" crossorigin="anonymous"></script>
        <title>Index</title>
    </head>
    <body>
        <header>
            <h1>TFG</h1>
            <button id="inicio" class="btn_1"><a href="index.php">Inicio</a></button>
            <div class="separador"></div>
            <button id="calendario" class="btn_1">Calendario</button>
            <div class="separador"></div>
            <button id="sobrenosotros" class="btn_1"><a>Sobre TFG</a></button>
            <div class="separador"></div>
            <div class="seudo_btn">
                <i id="icono_miperfil" class="fa-solid fa-user"></i>
                    <?php
                        if(isset($_SESSION['usuario'])){
                            echo '<button id="miperfil" class="btn_1 btn_perfil"><a href="miperfil.php">'.$_SESSION['usuario'].'</a></button>';
                        }else{
                            echo '<button id="miperfil" class="btn_1 btn_perfil"><a href="login.php">Iniciar sesión</a></button>';
                        }
                    ?>
                </button>
            </div> 
        </header>
        <div id="contienesobrenosotros" class="contenedor">
            <h1>Sobre nosotros</h1>
            <p>TFG es un sitio web orientado a la organización de grupos de limpieza para entornos naturales, teniendo como objetivo la conservación y protección del medio ambiente.</p>
        </div>
    </body>
</html>