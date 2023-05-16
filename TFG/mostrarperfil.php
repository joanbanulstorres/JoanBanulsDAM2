<!DOCTYPE html>
<html>
    <?php
        include "config.php";
        $mysqli = new  mysqli($mydbserver, $mydbuser, $mydbpassword, $mydb);

        $consulta = "SELECT * FROM usuarios WHERE `usuario` = '".$_SESSION['usuario']."'";
        $resultado = $mysqli->query($consulta);
        $fila = $resultado->fetch_assoc();
        // var_dump($fila['usuario']);

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
                            echo '<button id="sesioniniciada" class="btn_1 btn_perfil">'.$_SESSION['usuario'].'</button>';
                        }else{
                            echo '<button id="iniciarsesion" class="btn_1 btn_perfil">Iniciar sesión</button>';
                        }
                    ?>
                </button>
            </div> 
        </header>
        <?php
            echo '
                <div id="contienemiperfil" class="contenedor">
                    <div id="contienedatosperfil">
                        <h1>Mi perfil</h1>
                        <div>
                            <h3 style="display: inline; margin-right:5px;">Nombre de usuario:</h3>
                            <h3 style="font-weight: normal; display: inline; margin-left:5px;">'.$fila['usuario'].'</h3>
                        </div>
                        <div>
                            <h3 style="display: inline; margin-right:5px;">Email:</h3>
                            <h3 style="font-weight: normal; display: inline; margin-left:5px;">'.$fila['email'].'</h3>
                        </div>
                        <div>
                            <h3 style="display: inline; margin-right:5px;">Incursiones completadas:</h3>
                            <h3 style="font-weight: normal; display: inline; margin-left:5px;">'.$fila['incursionescompletadas'].'</h3>
                        </div>
                        <button class="btn_3"><a href="crearincursion.php">Crear incursión</a></button>
                        <h2>Mis incursiones pendientes</h2>
                    </div> 
                    <table id="tablamiperfil" class="contienetabla">
                    <tr>
                        <th>Incursión</th>
                        <th>Descripción</th>
                        <th>Localización</th>
                        <th>Fecha</th>
                        <th>Participantes</th>
                        <th>Cargo</th>
                    </tr>                
            ';
            
            // Se averigua el id del usuario y se define como id de la sesión
            $consulta_id = "SELECT * FROM usuarios WHERE usuario = '".$_SESSION['usuario']."'";
            $resultado_id = $mysqli->query($consulta);
            $fila_id = $resultado_id->fetch_assoc();
            $_SESSION['id_usuario']  = $fila_id['Identificador'];
            
            $consulta = "SELECT * FROM incursionespersonales JOIN incursiones ON id_incursion = incursiones.Identificador WHERE incursionespersonales.id_usuario = ".$_SESSION['id_usuario']." ORDER BY `incursiones`.`fecha` ASC";
            $resultado = $mysqli->query($consulta);
            while($fila = $resultado->fetch_assoc()){
                echo '
                        <tr>
                            <td>
                                <div>
                                    <h4>'.$fila['nombre'].'</h4>
                                    <img class="img_index" src="imagenes/'.$fila['imagen'].'"/>
                                </div>
                            </td>
                            <td>'.$fila['descripcion'].'</td>
                            <td style="text-align:center"><a class="link_localizacion" href="'.$fila['linklocalizacion'].'">'.$fila['localizacion'].'</a></td>
                            <td style="text-align:center">'.$fila['fecha'].'</td>
                            <td style="text-align:center">'.$fila['participantesactuales'].'/'.$fila['minparticipantes'].'</td>
                            <td style="text-align:center">'.$fila['cargo'].'</td>
                        </tr>
                ';
            }
            echo '
                </table>
                </div>
            ';
        ?>
        
    </body>
</html>