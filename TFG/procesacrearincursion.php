<?php

    session_start();
    include "config.php";
    $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword, $mydb);
    
    // Se inserta la incursión creada en la tabla de incursiones (generales)
    $consulta_incursion = "INSERT INTO `incursiones` (
                                            `Identificador`,
                                            `nombre`,
                                            `descripcion`,
                                            `imagen`,
                                            `fecha`,
                                            `localizacion`,
                                            `linklocalizacion`,
                                            `lider`,
                                            `minparticipantes`,
                                            `participantesactuales`
                                        )
                                VALUES (
                                            NULL,
                                            '".$_POST['nombre']."',
                                            '".$_POST['descripcion']."',
                                            NULL,
                                            '".$_POST['fecha']."',
                                            '".$_POST['localizacion']."',
                                            NULL,
                                            '".$_SESSION['usuario']."',
                                            '".$_POST['minparticipantes']."',
                                            '1'
                                        )
    ";
    $mysqli->query($consulta_incursion);

    // Se guarda el id del último registro (el que se acaba de insertar)
    $consulta_ultimo_id = "SELECT Identificador FROM incursiones ORDER BY Identificador DESC LIMIT 1";
    $resultado = $mysqli -> query($consulta_ultimo_id);
    $fila = $resultado -> fetch_assoc();
    foreach($fila as $campo => $valor){
        $ultimo_id = $valor;
    }

    // Se inserta la incursión creada en la tabla de incursiones personales
    $consulta_incursion_personal = "INSERT INTO incursionespersonales (
                                            `Identificador`,
                                            `id_incursion`,
                                            `id_usuario`,
                                            `cargo`
                                        )
                                VALUES (
                                            NULL,
                                            $ultimo_id,
                                            '".$_SESSION['id_usuario']."',
                                            'líder'
                                        )
    ";
    $mysqli->query($consulta_incursion_personal);

    header('refresh:0; url=miperfil.php');

?>