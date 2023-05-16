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
            <button id="sobrenosotros" class="btn_1"><a href="sobrenosotros.php">Sobre TFG</a></button>
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
        <div id="contiene_crearincursion" class="contenedor">
            <fomr action="procesacrearincursion.php" method="POST">
                <h1>Crear incursión</h1>
            <div>
                <h3>Nombre</h3>
                <input class="form_input" name="nombre"></input>
            </div>
            <div>
                <h3>Descripción</h3>
                <textarea class="form_input" name="descripcion"></textarea>
            </div>
            <!-- <div>
                <h3>Imagen</h3>
                <input name="nombre" type="image"></input>
            </div> -->
            <div>
                <h3>Localización</h3>
                <input class="form_input" name="localizacion"></input>
            </div>
            <div>
                <h3>Fecha</h3>
                <input class="form_input" name="fecha" type="datetime-local"></input>
            </div>
            <div>
                <h3>Mínimo de participantes</h3>
                <input class="form_input" name="minparticipantes" type="number"></input>
            </div>
            <input name="submit" type="submit" value="Continuar" class="form_btn3">
            </form>
        </div>
    </body>
</html>