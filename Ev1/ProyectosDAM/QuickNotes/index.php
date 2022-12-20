<html>
    <head>
        <meta charset="UTF-8">
        <title>Quick Notes</title>
        <!-- jQuery -->
        <script src="lib/jquery-3.6.1.min.js"></script>
        <!-- jQuery UI -->
        <script src="lib/jquery-ui-1.13.2/jquery-ui.js"></script>
        <link rel="Stylesheet" href="lib/jquery-ui-1.13.2/jquery-ui.css">
        <!-- Importaciones de otros archivos -->
        <script src="condiciones_iniciales.js"></script>
        <script src="codigo.js"></script>
        <link rel="stylesheet" href="estilo/estilo.css">
    </head>
    <body>
        <header>
            <h1>QUICK NOTES</h1>
            <h2>Crea, edita y organiza tus apuntes</h2>
        </header>
        <nav>
            <h2 id="miscursos">Mis cursos</h2>
            <input id="documentoactual" value="sindocumento" readonly><br>
            <input id="asignaturaactual" value="sinasignatura" readonly><br>
            
            <?php
                
                include 'bd_config.php';
                
                $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword ,$mydb);
                
                $consulta = "SELECT * FROM cursos";
                $resultado = $mysqli -> query($consulta);
                while($fila = $resultado -> fetch_assoc()){
                    echo ' 
                        <h3>'.$fila['nombrecurso'].'</h3>
                        <div id="asignaturas">
                    ';
                }
               
                $consulta2 = "SELECT * FROM asignaturas";
                $resultado2 = $mysqli -> query($consulta2);
                while($fila2 = $resultado2 -> fetch_assoc()){
                    echo ' 
                        <h4 id="'.$fila2['Idasignatura'].'">'.$fila2['nombreasignatura'].'</h4>
                            <table border="0px" padding="0px" margin-left="5px">';
                            
                            $consulta3 = "SELECT * FROM documentos";
                            $resultado3 = $mysqli -> query($consulta3);
                            while($fila3 = $resultado3 -> fetch_assoc()){
                                if($fila3['FK_idasignatura'] == $fila2['Idasignatura']){
                                echo '
                                    <tr>
                                        <td class="nombre '.$fila3['nombredocumento'].' '.$fila3['FK_idasignatura'].'">'.$fila3['nombredocumento'].'</td>
                                        <td><button class="editar '.$fila3['nombredocumento'].' '.$fila3['FK_idasignatura'].'"><img src="estilo/bootstrap-icons-1.9.1/pencil-square.svg"></button></td>
                                        <td><button class="eliminar '.$fila3['nombredocumento'].' '.$fila3['FK_idasignatura'].'"><img src="estilo/bootstrap-icons-1.9.1/trash3-fill.svg"></button></td>
                                    </tr>
                                ';
                                }
                            }
                            echo '
                                <tr>
                                    <td colspan="3" class="nuevodoc '.$fila2['Idasignatura'].'"><button class="nuevodocumento '.$fila2['Idasignatura'].'"><img src="estilo/bootstrap-icons-1.9.1/file-earmark-plus.svg"></button><h5 id="nuevodocumentotxt">Nuevo documento</h5></td>
                                </tr>
                                <tr>
                                    <td colspan="3"><button class="eliminarasignatura '.$fila2['Idasignatura'].'"><img src="estilo/bootstrap-icons-1.9.1/x-square.svg"></button><h5 id="eliminarasignatura">Eliminar asignatura</h5></td>
                                </tr>
                            </table>';
                        '
                    ';
                }
                echo '</div>';
            ?>
            
<!--            <div style="display:none" id="dialog" title="Nuevo documento" >
                <h4>Introduce un nombre para el documento</h4>
                <input id="nombrenuevodocumento">
                <button id="enviarnombre"><img src="estilo/bootstrap-icons-1.9.1/file-earmark-check.svg"></button>
            </div>-->
            <div class="nuevaasig">
                <button id="nuevaasignatura"><img src="estilo/bootstrap-icons-1.9.1/plus.svg"></button><h3 id="nuevaasignaturatxt">Nueva asignatura</h3>
            </div>
            
<!--            <h3>DAM</h3>
            
            <div id="asignaturas">
                
                <h4>Empresa e iniciativa emprendedora</h4>
                    <table id="a1" border="0px" padding="0px" margin-left="5px">
                        <tr>
                            <td class="nombre documento1">documento1</td>
                            <td><button class="editar documento1"><img src="estilo/bootstrap-icons-1.9.1/pencil-square.svg"></button></td>
                            <td><button class="eliminar" class="documento1"><img src="estilo/bootstrap-icons-1.9.1/trash3-fill.svg"></button></td>
                        </tr>
                        <tr>
                            <td class="nombre documento2">documento2</td>
                            <td><button class="editar documento2"><img src="estilo/bootstrap-icons-1.9.1/pencil-square.svg"></button></td>
                            <td><button class="eliminar"><img src="estilo/bootstrap-icons-1.9.1/trash3-fill.svg"></button></td>
                        </tr>
                        <tr>
                            <td class="nombre documento3">documento3</td>
                            <td><button class="editar documento3"><img src="estilo/bootstrap-icons-1.9.1/pencil-square.svg"></button></td>
                            <td><button class="eliminar"><img src="estilo/bootstrap-icons-1.9.1/trash3-fill.svg"></button></td>
                        </tr>
                        <tr>
                            <td class="nombre documento4">documento4</td>
                            <td><button class="editar documento4"><img src="estilo/bootstrap-icons-1.9.1/pencil-square.svg"></button></td>
                            <td><button class="eliminar"><img src="estilo/bootstrap-icons-1.9.1/trash3-fill.svg"></button></td>
                        </tr>
                        <tr>
                            <td colspan="3"><button class="nuevodocumento"><img src="estilo/bootstrap-icons-1.9.1/file-earmark-plus.svg"></button><h5 id="nuevodocumentotxt">Nuevo documento</h5></td>
                        </tr>
                        <tr>
                            <td colspan="3"><button class="eliminarasignatura"><img src="estilo/bootstrap-icons-1.9.1/x-square.svg"></button><h5 id="eliminarasignatura">Eliminar asignatura</h5></td>
                        </tr>
                    </table>
                <h4>Inglés</h4>
                   <table id="a2" border="1px" padding="0px" margin-left="5px">
                        
                        <tr>
                            <td colspan="3"><button class="nuevodocumento"><img src="estilo/bootstrap-icons-1.9.1/file-earmark-plus.svg"></button><h5 id="nuevodocumentotxt">Nuevo documento</h5></td>
                        </tr>
                        <tr>
                            <td colspan="3"><button class="eliminarasignatura"><img src="estilo/bootstrap-icons-1.9.1/x-square.svg"></button><h5 id="eliminarasignatura">Eliminar asignatura</h5></td>
                        </tr>
                    </table>             
                <h4>Programación multimedia y dispositivos móviles</h4>
                <div>
                    <h5>documento4</h5>
                </div>
                <h4>Desarrollo de interfaces</h4>
                <div>
                </div>
                <h4>Sistemas de gestión empresarial</h4>
                <div>
                </div>
                <h4>Programación de servicios y procesos</h4>
                <div>
                </div>
                <h4>Acceso a datos</h4>
                <div>
                </div>
            </div>
            -->
            
        </nav>
        <main>
            <table border="1px" width="70%" height="100%">
                <tr id="barraherramientas" width="100%" height="18px">
                    <td>
                        <button id="guardar"><img src="estilo/bootstrap-icons-1.9.1/save.svg" class="icon"></button>
                        <select id="tipotexto">
                            <option value="p">Texto de parrafo</option>
                            <option value="h1">Encabezado 1</option>
                            <option value="h2">Encabezado 2</option>
                            <option value="h3">Encabezado 3</option>
                            <option value="h4">Encabezado 4</option>
                            <option value="h5">Encabezado 5</option>
                            <option value="h6">Encabezado 6</option>
                            <option value="pre">Texto preformateado</option>
                        </select>
                        <select id="selectfont">
                            <option value="Arial">Arial</option>
                            <option value="Verdana">Verdana</option>
                            <option value="Tahoma">Tahoma</option>
                            <option value="Trebouchet MS">Trebouchet</option>
                            <option value="Times New Roman">Times New Roman</option>
                            <option value="Georgia">Georgia</option>
                            <option value="Garamond">Garamond</option>
                            <option value="Courier New">Courier New</option>
                            <option value="Brush Script">Brush Script</option>
                        </select>
                        <input id="fontsize" type="number" value="16">
                        <button id="bold"><img src="estilo/bootstrap-icons-1.9.1/type-bold.svg" class="icon"></button>
                        <button id="cursive"><img src="estilo/bootstrap-icons-1.9.1/type-italic.svg" class="icon"></button>
                        <button id="underline"><img src="estilo/bootstrap-icons-1.9.1/type-underline.svg" class="icon"></button>
                        <input type="color" id="fontcolor">
                        <button id="orderedlist"><img src="estilo/bootstrap-icons-1.9.1/list-ol.svg" class="icon"></button>
                        <button id="unorderedlist"><img src="estilo/bootstrap-icons-1.9.1/list-ul.svg" class="icon"></button>
                        <button id="alignleft"><img src="estilo/bootstrap-icons-1.9.1/text-left.svg" class="icon"></button>
                        <button id="alignright"><img src="estilo/bootstrap-icons-1.9.1/text-right.svg" class="icon"></button>
                        <button id="aligncenter"><img src="estilo/bootstrap-icons-1.9.1/text-center.svg" class="icon"></button>
                        <button id="alignjustify"><img src="estilo/bootstrap-icons-1.9.1/justify-left.svg" class="icon"></button>
                        <button id="zoomin"><img src="estilo/bootstrap-icons-1.9.1/zoom-in.svg" class="icon"></button>
                        <button id="zoomout"><img src="estilo/bootstrap-icons-1.9.1/zoom-out.svg" class="icon"></button>
                    </td>
                </tr>
                <tr>
                    <td id="fondopagina">
                        <div id="pagina" contenteditable="true"></div>
                    </td>
                </tr>
            </table>
        </main>
    </body>
</html>