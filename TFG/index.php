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
        <script src="codigo.js"></script>
        <script src="https://kit.fontawesome.com/d67157ffdf.js" crossorigin="anonymous"></script>
        <title>Inicio</title>
    </head>
    <body>
        <?php include("header.php") ?>
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

                    // Se guardan las IDs de las incursiones en las que está inscrito el usuario ************************************************************
                    $ids_inc = array();
                    if(isset($_SESSION['id_usuario'])){
                        $consulta_ids_inc = "SELECT `id_incursion` FROM `incursionespersonales` WHERE `id_usuario` = '".$_SESSION['id_usuario']."'";
                        $resultado_ids_inc = $mysqli -> query($consulta_ids_inc);
                        while($fila_ids_inc = $resultado_ids_inc -> fetch_assoc()){
                            array_push($ids_inc, $fila_ids_inc['id_incursion']);
                        }
                    }
                   
                    $consulta = "SELECT * FROM `incursiones` ORDER BY fecha";
                    $resultado = $mysqli -> query($consulta);
                    while($fila = $resultado -> fetch_assoc()){
                        echo '
                            <tr>
                                <td>
                                    <div>
                                        <h4>'.$fila['nombre'].'</h4>
                                            <p>organizada por '.$fila['lider'].'</p>';
                                            if($fila['imagen'] != NULL){
                                                echo '<img src="imagenes/'.$fila['imagen'].'"/>';
                                            }
                                    echo '
                                    </div>
                                </td>
                                <td>'.$fila['descripcion'].'</td>
                                <td style="text-align:center"><a class="link_localizacion" href="'.$fila['linklocalizacion'].'">'.$fila['localizacion'].'</a></td>
                                <td style="text-align:center">'.$fila['fecha'].'</td>
                                <td style="text-align:center">'.$fila['participantesactuales'].'/'.$fila['minparticipantes'].'</td>';
                                if(isset($_SESSION['usuario'])){
                                    $inscrito = false; 
                                    foreach($ids_inc as $id_inc){
                                        if($id_inc == $fila['Identificador']){$inscrito = true;}
                                    }
                                    if($inscrito == false){
                                        echo '<td style="text-align:center"><button class="btn_inscribirse" data-id_incursion="'.$fila['Identificador'].'">+</button></td>';
                                    }else{
                                        echo '<td style="text-align:center"><button class="btn_check">✓</button></td>';
                                    }
                                }else{
                                    echo '<td style="text-align:center"><button class="btn_inscribirse"><a href="login.php">+</a></button></td>';
                                }
                            echo '
                            </tr>
                        ';
                    }
                ?>
            </table>
        </div>
    </body>
</html>