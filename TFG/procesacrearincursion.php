<?php

    session_start();

    include "config.php";

    $mysqli = new  mysqli($mydbserver, $mydbuser, $mydbpassword, $mydb);
    
    $consulta = " INSERT INTO incursiones (
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
                                            '".$_SESSION['usuario'] = $_POST['usuario']."',
                                            '".$_POST['localizacion']."',
                                            '1'
                                        )
    ";
    $mysqli->query($consulta);

?>