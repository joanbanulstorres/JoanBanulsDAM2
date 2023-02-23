<html>
    <head>
        <meta charset="UTF-8">
        <style>
            @font-face{
                font-family:gravity-bold;
                src:url(estilo/gravity/Gravity-Bold.otf);
            }
            body{background:rgb(202, 207, 210); font-family:gravity-bold}
            h1{margin-top:50px; font-size:4em; text-align:center;}
            h2{margin-top:50px; font-size:3em; text-align:center;}
            form{background:white; padding:20px; margin:auto; margin-top:50px; width:20%;}
            input{width:100%; padding-top:10px; padding-bottom:10px; margin-top:10px; margin-bottom:10px;}
        </style>
    </head>
    <body>
        <h1>QUICK NOTES</h1>
        <h2>Introduce tus datos</h2>
        <form action="login.php" method="POST">
            <input type="text" placeholder="usuario" name="user">
            <input type="password" placeholder="contraseña" name="password">
            <input type="submit">
        </form>
    </body>
</html>