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
        <title>Crear incursión</title>
    </head>
    <body>
        <header>
            <h1>Limpiadores Medioambientales</h1>
            <button id="inicio" class="btn_header"><a href="index.php">Inicio</a></button>
            <div class="separador"></div>
            <button id="sobrenosotros" class="btn_header"><a href="sobrenosotros.php">Sobre Limpiadores Medioambientales</a></button>
            <div class="separador"></div>
            <div class="seudo_btn">
                <i id="icono_miperfil" class="fa-solid fa-user"></i>
                    <?php
                        if(isset($_SESSION['usuario'])){
                            echo '<button id="miperfil" class="btn_header btn_perfil"><a href="miperfil.php">'.$_SESSION['usuario'].'</a></button>';
                        }else{
                            echo '<button id="miperfil" class="btn_header btn_perfil"><a href="login.php">Iniciar sesión</a></button>';
                        }
                    ?>
                </button>
            </div> 
        </header>
        <div id="contienecrearincursion" class="contenedor">
            <form action="procesacrearincursion.php" method="POST">
                <h1>Crear incursión</h1>
                <div class="form_div">
                    <h3>Nombre</h3>
                    <input class="form_input" name="nombre" required></input>
                </div>
                <div class="form_div">
                    <h3>Descripción</h3>
                    <textarea class="form_input" name="descripcion" required></textarea>
                </div>
                <!-- <div>
                    <h3>Imagen</h3>
                    <input name="nombre" type="image"></input>
                </div> -->
                <div class="form_div">
                    <h3>Localización</h3>
                    <input id="localizacion" class="form_input" name="localizacion" required></input>
                </div>
                <div class="form_div">
                    <h3>Fecha</h3>
                    <input class="form_input" name="fecha" type="datetime-local" required></input>
                </div>
                <div class="form_div">
                    <h3>Mínimo de participantes</h3>
                    <input class="form_input" name="minparticipantes" type="number" required></input>
                </div>
                <input id="btn_crear_incursion" class="form_btn" type="submit" value="Continuar">
                <!-- <input id="enviar_registro" class="form_btn" type="submit" value="Continuar"> -->
            </form>
        </div>
    </body>
</html>