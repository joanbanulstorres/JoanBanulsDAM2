<!doctype HTML>
<html>
    <head>
        <style>
            body{background:rgb(220,220,220); font-family:sans-serif;}
            table{width:1200px; margin:auto; padding:30px; background:white; box-shadow:0px 10px 20px rgba(0, 0, 0, 0.4);}
            h1{text-align:center;}
        </style>
    </head>    
    <body>

        <?php include "codificador.php"; ?>
        <h1>Entregas de <?php echo descodifica($_GET['clave']) ?></h1>
        <table>
            <tr><th>URL</th><th>Asignatura</th><th>Práctica</th><th>fecha</th><th>Video</th></tr>
            <?php
                
                include "config.php";
                $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword, $mydb);     // - Cambiamos los campos según 'config.php'
                $consulta = "SELECT * FROM entregas WHERE email = '".descodifica($_GET['clave'])."'";
                $resultado = $mysqli->query($consulta);
                while($fila = $resultado->fetch_assoc()){
                    
                    // Para coger la parte de la url correspondiente al video
                    $partes = parse_url($fila['url']);
                    parse_str($partes['query'], $query);
                    $miparte = $query['v'];
                    //echo $miparte;

                    echo '<tr>';
                    echo '<td><a href="'.$fila['url'].'">'.$fila['url'].'</a></td>';
                    echo '<td>'.$fila['asignatura'].'</td>';
                    echo '<td>'.$fila['practica'].'</td>';
                    echo '<td>'.$fila['epoch'].'</td>';
                    echo '<td>';
                    echo '<iframe width="300" height="200" src="https://www.youtube.com/embed/'.$miparte.'" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>';
                    echo '</td>';
                    echo "</tr>";

                }
            ?>
        </table>

    </body>
</html>