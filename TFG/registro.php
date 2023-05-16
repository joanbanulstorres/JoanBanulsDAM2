<html>
    <head>
        <meta charset="utf-8">
        <title>Crear cuenta</title>
        <script src="https://code.jquery.com/jquery-3.6.4.js" integrity="sha256-a9jBBRygX1Bh5lt8GZjXDzyOB+bWve9EiO7tROUtj/E=" crossorigin="anonymous"></script>
        <link rel="stylesheet" href="estilo/estilo.css">
        <script src="codigo.js"></script>
    </head>
    <body>
        <div id="contieneformulario">
            <h1>TFG</h1>
            <h2>Crear cuenta</h2>
            <form id="form_registro" name="form_registo" onsubmit="return enviar_formulario()" action="procesaregistro.php" method="POST">
                <div class="form_div">
                    <input id="nombre" class="form_input form_nombre" name="nombre" type="text" data-estado="vacio" placeholder=" " required>
                    <label id="nombre_label" for="" class="form_label form_nombre">Nombre</label>
                </div>
                <div class="form_div">
                    <input id="apellidos" class="form_input form_apellidos" name="apellidos" type="text" data-estado="vacio" placeholder=" " required>
                    <label for="" class="form_label form_apellidos">Apellidos</label>
                </div>
                <div id="contieneemail" class="form_div">
                    <input id="email" class="form_input form_email" name="email" type="email" data-estado="vacio" placeholder=" " required>
                    <label id="email_label" for="" class="form_label form_email">Email</label>
                </div>
                <div id="contieneusuario" class="form_div">
                    <input id="usuario" class="form_input form_usuario" name="usuario" type="text" data-estado="vacio" placeholder=" " required>
                    <label id="usuario_label" for="" class="form_label form_usuario">Usuario</label>
                </div>
                <div id="contienecontrasena" class="form_div">
                    <input id="contrasena" name="contrasena" type="password" data-estado="vacio" placeholder=" " required>
                    <label id="contrasena_label" for="">Contraseña</label>
                    <button id="ver_contrasena" type="button"><img id="icono_ver" src="estilo/img/ver1.png" alt="Ver"></img></button>
                </div>
                <input id="enviar_registro" type="submit" value="Continuar">
                <p>¿Ya tienes una cuenta? <a href="login.php" style="text-decoration:none">Inicia sesión</a></p>
            </form>
        </div>
    </body>
</html>