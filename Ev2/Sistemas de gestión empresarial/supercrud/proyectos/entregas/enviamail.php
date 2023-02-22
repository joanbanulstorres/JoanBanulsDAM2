<!-- *NUEVO* documento -->
<?php

    $cabeceras = 'From: info@joanbanyulstorres.es' . "\r\n" .
    'Reply-To: info@joanbanyulstorres.es' . "\r\n" .
    'X-Mailer: PHP/' . phpversion();
    $cabeceras .= 'MIME-Version: 1.0' . "\r\n";
    $cabeceras .= 'Content-type: text/html; charset=iso-8859-1' . "\r\n";
    
    mail(
        "info.jobato@gmail.com",
        "Este es el asunto del mensaje",
        "<h1>Titulo</h1><p>Este es el cuerpo del mensaje</p>",
        $cabeceras
    );
?>