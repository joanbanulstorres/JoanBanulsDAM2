<!doctype html>
<html>
    <head>
        <meta charset="UTF-8">
        <style>
            body{background:rgb(240,240,240);}
            form{width:300px; height:300px; padding:20px; margin:auto;background:white; box-shadow:0px 10px 20px rgba(0,0,0,0.3); border-radius:10px;}
            input{width:100%; margin-top:10px; margin-bottom:10px; border:0px; padding-top:5px; padding-bottom:5px;}  
        </style>
    </head>
    <body>
        <form action="login.php" method="POST">
            <input type="text" name="usuario" placeholder="Introducir nombre">
            <input type="password" name="contrasena" placeholder="Introducir contraseña">
            <input type="submit">
        </form>
    </body>
</html>
