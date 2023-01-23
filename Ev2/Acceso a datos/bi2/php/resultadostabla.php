
<?php
                                                                                                // *NUEVO*
    include "config.php";
            
    $sql = $_GET['sql']."";

    $result = $mysqli -> query($sql);

    $row = $result -> fetch_assoc();
    $contador = 0;
    while($row = $result -> fetch_assoc()){
        $contador++;
    }
    echo '<p>La búsqueda ha devuelto '.($contador + 1). ' resultados</p>';

?>

<table colpading = 0 colspacing = 0 cellpading = 0 cellspacing = 0 width = 100%>
    
    <?php

        include "config.php";
                
        $sql = $_GET['sql']."";                                                                 // *NUEVO* - "LIMIT 1" -> ""

        $result = $mysqli -> query($sql);

        if($row = $result -> fetch_assoc()){                                                    // *NUEVO* while -> if
            echo '<tr>';
            foreach($row as $campo => $valor){
                echo '<th>'.$campo.'</th>';
            }
            echo '</tr>';
        }

        $sql = $_GET['sql'];
        
        $result = $mysqli -> query($sql);
        
        while($row = $result -> fetch_assoc()){
            echo '<tr>';
            foreach($row as $campo => $valor){
                echo '<td>'.$valor.'</td>';
            }
            echo '</tr>';
        }
        
    ?>
</table>