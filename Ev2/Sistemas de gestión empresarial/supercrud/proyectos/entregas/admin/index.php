<?php
    session_start();
    include "../config.php";
    include "../controlador.php";
	include "inc/condicionesdeinicio.php";
    $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword, $mydb);
    $miformulario = new Supercontrolador();
?>
<html>
    <head>
        <meta charset="utf-8">
		<script src="https://kit.fontawesome.com/d67157ffdf.js" crossorigin="anonymous"></script>
		<script src="lib/jquery-3.6.3.min.js"></script>
        <script src="js/codigo.js"></script>
		<link rel="stylesheet" href="css/estilo.css">
		<!-- Librería SELECT2 -->
		<link href="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/css/select2.min.css" rel="stylesheet" />
		<script src="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/js/select2.min.js"></script>
    </head>
    <body>
        <?php
			// Páginas
			if(isset($_GET['pagina'])){
				switch($_GET['pagina']){
					case "anterior": 
						if($_SESSION['pagina'] > 0){
							$_SESSION['pagina']--;
						}
						break;
					case "siguiente";
						$_SESSION['pagina']++;
						break;
					case "primera";
						$_SESSION['pagina'] = 0;
						break;
					// *El botón para ir a la última página aún no está configurado
				}
			}
			
            if(isset($_POST['usuario']) && !isset($_SESSION['usuario'])){         
                $consulta = "SELECT * FROM usuarios WHERE usuario = '".$_POST['usuario']."' AND contrasena = '".$_POST['contrasena']."'";
                $resultado = $mysqli->query($consulta);
                $pasas = "no";
                while($fila = $resultado->fetch_assoc()){
                    $pasas = "si";
                    $_SESSION['usuario'] = $fila['usuario'];
                }
                if($pasas == "si"){}else{
                    echo '<div class="notice">Intento de acceso denegado</div>';
                }
            }
        ?>
        <?php
            if(isset($_SESSION['usuario'])){
                echo '
                    <aside>
                        <div id="contienemenu"><ul>';	// ---------------------------------------------------------- *NUEVO: modificaciones en 'contienemenu'*
                        $consulta = "SHOW TABLES";
                        $resultado = $mysqli->query($consulta);
                        while($fila = $resultado->fetch_array()){
                            $consulta2 = "SHOW TABLE STATUS WHERE Name='".$fila[0]."' ";
							$resultado2 = $mysqli -> query($consulta2);
							while($fila2 = $resultado2->fetch_array()){
								if(json_decode($fila2["Comment"])->titulo == ""){
									// Tablas SIN comentario de tabla
									echo '<li><a href="?tabla='.$fila[0].'"><i class="fa-solid fa-table"></i>'.$fila[0].'</a></li>';
								}else{
									// Tablas CON comentario de tabla
									echo '<li><a href="?tabla='.$fila[0].'" title="'.json_decode($fila2["Comment"])->descripcion.'"><i class="'.json_decode($fila2["Comment"])->icono.'"></i>'.json_decode($fila2["Comment"])->titulo.'</a></li>';
								}
								
							}
                        }
						echo '</ul>
                        </div>
                    </aside>
                    <section>
                        <div id="contienecontenido">
                            ';
								if(isset($_GET['informe'])){$miformulario -> informe($_GET['tabla'], $_GET['informe']);}	// ------------------------------------------ *NUEVO*
								if(isset($_GET['delete'])){$miformulario -> delete($_GET['tabla'], $_GET['delete']);}
								if(isset($_GET['update'])){echo'<div id="formulario">'; $miformulario -> update($_GET['tabla'], $_GET['update']); echo '</div>';}
								if($_POST['clave'] == "procesainsertar"){$miformulario->procesainsertar();}
								if($_POST['clave'] == "procesaupdate"){$miformulario->procesaupdate($_POST['tabla'], $_POST['identificador']);}
                                
								// ---------------------------------------------------------------- *NUEVO: 'if' para que al mostrar un informe no se muestre también la tabla*
								if(isset($_GET['tabla']) && !isset($_GET['informe']) && !isset($_GET['delete']) && !isset($_GET['update'])){
									$miformulario -> leer($_GET['tabla']);
								}
								
								if(isset($_GET['create'])){echo'<div id="formulario">'; $miformulario -> insertar($_GET['create']); echo '</div>';}
							echo '
                        </div>
                    </section>
                ';
            }else{
                echo '
                    <form action= "?" method="POST" id="formulariologin">
                        <input type="text" name="usuario" placeholder="usuario">
                        <input type="password" name="contrasena" placeholder="contraseña">
                        <input type="submit">
                    </form>
                ';
            }
        ?>
	<div id="ajax"></div>
    </body>
</html>