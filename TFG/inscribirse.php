<?php

    session_start();
    include "config.php";
    $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword, $mydb);

    $consulta_incursiones = "UPDATE `incursiones` SET `participantesactuales` = participantesactuales + 1 WHERE `incursiones`.`Identificador` = '".$_POST['id_inc']."'";
    $mysqli -> query($consulta_incursiones);

    $consulta_incursiones_personales = "INSERT INTO incursionespersonales (
                                                                            `Identificador`,
                                                                            `id_incursion`,
                                                                            `id_usuario`,
                                                                            `cargo`
                                                                        )
                                                                VALUES (
                                                                            NULL,                                                                            
                                                                            '".$_POST['id_inc']."',
                                                                            '".$_SESSION['id_usuario']."',
                                                                            'incursionista'
                                                                        )
    ";
    $mysqli -> query($consulta_incursiones_personales);
    //header('refresh:0; url=index.php');
    
?>