<html>
    <head>
        <meta charset="utf-8">
        <title>Iniciar sesión</title>
        <script src="https://code.jquery.com/jquery-3.6.4.js" integrity="sha256-a9jBBRygX1Bh5lt8GZjXDzyOB+bWve9EiO7tROUtj/E=" crossorigin="anonymous"></script>
        <link rel="stylesheet" href="estilo/estilo.css">
        <script src="codigo.js"></script>
    </head>
    <body>
        <div id="contieneformulario">
        <h1>Limpiadores Medioambientales</h1>
        <h2>Iniciar sesión</h2>
            <form id="form_login" action="procesalogin.php" method="POST">
                <div class="form_div">
                    <input id="usuarioemail" name="usuarioemail" class="form_input form_usuarioemail" type="text" data-estado="vacio" placeholder=" " required>
                    <label id="usuarioemail_label" for="" class="form_label form_usuarioemail">Nombre de usuario o email</label>
                </div>
                <div id="contienecontrasena" class="form_div">
                    <input id="contrasena" class="form_input" name="contrasena" type="password" data-estado="vacio" placeholder=" " required>
                    <label id="contrasena_label" for="">Contraseña</label>
                    <button id="ver_contrasena" type="button"><img id="icono_ver" src="estilo/img/ver1.png" alt="Ver"></img></button>
                </div>
                <input id="enviar_registro" name="submit" type="submit" value="Continuar" class="form_btn">
                <p>¿No tienes una cuenta? <a href="registro.php" style="text-decoration:none">Regístrate</a></p>
            </form>
        </div>
    </body>
</html>