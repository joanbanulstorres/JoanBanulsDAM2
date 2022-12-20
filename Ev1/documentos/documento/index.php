<?php session_start();?>    <!-- *NUEVO* -->
<html>
    <head>
        <script src="https://code.jquery.com/jquery-3.6.1.js" integrity="sha256-3zlB5s2uwoUzrXK3BT7AX3FyvojsraNFxCc2vC/7pNI=" crossorigin="anonymous"></script>
        <link rel="Stylesheet" href="estilo/estilo.css">
        <script src="js/codigo.js"></script>
    </head>
    <body>
        <table border=0px width=100% height=100%>
            <tr id="menu">
                <td>Menu</td>
            </tr>
            <tr height=20px id="barranombredocumento">
                <td>
                    <input type="text" id="documentname" placeholder="Nombre del documento" value="<?php echo explode(".", $_GET['file'])[0] ?>">   <!-- value="..." para que aparezca el nombre del documento en el input  -->
                </td>
            </tr>
            <tr height=50px id="herramientas">
                <td>
                    <button id="guardar"><img src="../img/bootstrap-icons-1.9.1/save.svg" class="icon"></button> <!-- *NUEVO* - icono de guardar -->
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
                    <input id="fontsize" type="number" value="10">
                    <button id="bold"><img src="../img/bootstrap-icons-1.9.1/type-bold.svg" class="icon"></button>  <!-- *NUEVO* - icono -->
                    <button id="cursive"><img src="../img/bootstrap-icons-1.9.1/type-italic.svg" class="icon"></button> <!-- *NUEVO* - icono -->
                    <button id="underline"><img src="../img/bootstrap-icons-1.9.1/type-underline.svg" class="icon"></button>    <!-- *NUEVO* - icono -->
                    <input type="color" id="fontcolor">
                    <button id="orderedlist"><img src="../img/bootstrap-icons-1.9.1/list-ol.svg" class="icon"></button>    <!-- *NUEVO* - -->
                    <button id="unorderedlist"><img src="../img/bootstrap-icons-1.9.1/list-ul.svg" class="icon"></button>    <!-- *NUEVO* - -->
                    <button id="alignleft"><img src="../img/bootstrap-icons-1.9.1/text-left.svg" class="icon"></button>    <!-- *NUEVO* - -->
                    <button id="alignright"><img src="../img/bootstrap-icons-1.9.1/text-right.svg" class="icon"></button>    <!-- *NUEVO* - -->
                    <button id="aligncenter"><img src="../img/bootstrap-icons-1.9.1/text-center.svg" class="icon"></button>    <!-- *NUEVO* - -->
                    <button id="alignjustify"><img src="../img/bootstrap-icons-1.9.1/justify-left.svg" class="icon"></button>    <!-- *NUEVO* - -->
                </td>
            </tr>
            <tr>
                <td id="fondopagina">
                    <div id ="pagina" contenteditable="true">
                        <?php include "E:/nuevoxampp/htdocs/documentos/documento/vault/users/".$_SESSION['user']."/".$_GET['file'] ?>    <!-- Para cargar el contenido guardado -->
                    </div>
                </td>
            </tr>
        </table>
    </body>
</html>