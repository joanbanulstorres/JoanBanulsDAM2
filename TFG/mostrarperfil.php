<!DOCTYPE html>
<html>
    <?php
        include "config.php";
        $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword, $mydb);

        $consulta = "SELECT * FROM usuarios WHERE `usuario` = '".$_SESSION['usuario']."'";
        $resultado = $mysqli -> query($consulta);
        $fila = $resultado -> fetch_assoc();
        // var_dump($fila['usuario']);

    ?>
    <head>
        <script src="https://code.jquery.com/jquery-3.6.4.js" integrity="sha256-a9jBBRygX1Bh5lt8GZjXDzyOB+bWve9EiO7tROUtj/E=" crossorigin="anonymous"></script>
        <meta charset="utf-8">
        <link rel="stylesheet" href="estilo/estilo.css">
        <script src="https://kit.fontawesome.com/d67157ffdf.js" crossorigin="anonymous"></script>
        <title>Mi perfil</title>
    </head>
    <body>
        <?php include("header.php") ?>
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
                        <div>
                            <h3 style="display: inline; margin-right:5px;">Cerrar sesión</h3>
                            <button class="btn_header"><a href="logout.php"><i class="fa-solid fa-right-from-bracket" style="color: #000000;"></a></i></button>
                        </div>
                        <h2>Mis incursiones</h2>
                        <button class="btn_3"><a href="crearincursion.php">Crear incursión</a></button>
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
            
            $consulta = "SELECT * FROM incursionespersonales JOIN incursiones ON id_incursion = incursiones.Identificador WHERE incursionespersonales.id_usuario = ".$_SESSION['id_usuario']." ORDER BY `incursiones`.`fecha` ASC";
            $resultado = $mysqli -> query($consulta);
            while($fila = $resultado -> fetch_assoc()){
                echo '
                        <tr>
                            <td>
                                <div>
                                    <h4>'.$fila['nombre'].'</h4>';
                                    if($fila['imagen'] != NULL){echo '<img src="imagenes/'.$fila['imagen'].'"/>';}
                                echo '    
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