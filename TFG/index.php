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
            <button id="inicio" class="btn_1"><a>Inicio</a></button>
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
        <div class="contienetabla contenedor">
            <table>
                <tr>
                    <th>Incursión</th>
                    <th>Descripción</th>
                    <th>Localización</th>
                    <th>Fecha</th>
                    <th>Participantes</th>
                    <th>Inscribirme</th>
                </tr>
                <?php
                    $consulta = "SELECT * FROM incursiones ORDER BY fecha";
                    $resultado = $mysqli->query($consulta);
                    while($fila = $resultado->fetch_assoc()){
                        echo '
                            <tr>
                                <td>
                                    <div>
                                        <h4>'.$fila['nombre'].'</h4>
                                        <p>organizada por '.$fila['lider'].'</p>
                                        <img src="imagenes/'.$fila['imagen'].'"/>
                                    </div>
                                </td>
                                <td>'.$fila['descripcion'].'</td>
                                <td style="text-align:center"><a class="link_localizacion" href="'.$fila['linklocalizacion'].'">'.$fila['localizacion'].'</a></td>
                                <td style="text-align:center">'.$fila['fecha'].'</td>
                                <td style="text-align:center">'.$fila['participantesactuales'].'/'.$fila['minparticipantes'].'</td>
                                <td style="text-align:center"><button class="btn_2">+</button></td>
                            </tr>
                        ';
                    }
                ?>
            </table>
        </div>
    </body>
</html>