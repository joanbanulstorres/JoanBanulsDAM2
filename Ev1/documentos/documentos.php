<?php session_start();?>    <!-- *NUEVO* -->
    <html>
        <head>
            <script src="https://code.jquery.com/jquery-3.6.1.js" integrity="sha256-3zlB5s2uwoUzrXK3BT7AX3FyvojsraNFxCc2vC/7pNI=" crossorigin="anonymous"></script>
            <script>
                $(document).ready(function(){
                    $("#carpetaactual").load("leecarpeta.php?user=<?php echo $_SESSION['user']?>"); // *NUEVO* - cargamos la carpeta del usuario que se haya logeado
                    $(document).on("click", ".item", function(){    // Instrucción 'on' para archivos que se cargan de forma dinámica
                        if($(this).attr("filetype") == "html"){
                            window.location = "documento/index.php?file="+$(this).attr("filename")  // Carga el archivo en el hipervínculo
                        }
                    }) 
                })
            </script>
            <style>
                .item{
                    width:300px;
                    height:300px;
                    padding:5px; margin:5px;
                    border:1px solid gray;
                    border-radius:5px;
                    float:left;
                    position:relative;
                    display:table-cell;
                    text-align:center;
                    vertical-align:middle;
                }
                .documentname{position:absolute; bottom:5px; width:100%; left:5px;}
                .iconfile img, .iconfolder img{width:50%; margin:auto}
            </style>
        </head>
        <body>
            <header>

            </header>
            <main>
                <h3>Listado de documentos</h3>
                <div id="carpetaactual"></div>
            </main>
            <footer>

            </footer>
        </body>
    </html>