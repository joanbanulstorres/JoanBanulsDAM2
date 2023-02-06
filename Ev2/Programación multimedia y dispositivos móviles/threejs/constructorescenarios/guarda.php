<?php
    
    $img = $_POST['imgData'];
    $img = str_replace('data:image/png;base64,', '', $img);
    $img = str_replace(' ', '+', $img);
    $FileData = base64_decode($img);
    $fileName = "imagen.png";
    $success = file_put_contents($fileName, $FileData);

?>