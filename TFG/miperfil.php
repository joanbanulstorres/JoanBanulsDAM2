<!DOCTYPE html>
<?php
    session_start();
    include "config.php";
    $mysqli = new  mysqli($mydbserver, $mydbuser, $mydbpassword, $mydb);

    if(isset($_SESSION['usuario'])){
        include "mostrarperfil.php";
    }else{
        header('refresh:0; url=login.php');
    }
?>