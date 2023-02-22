<?php
    error_reporting(E_ALL ^ E_NOTICE); 
    class Supercontrolador{                                                 
        function formulario($tabla){                                        
            include "config.php";
            echo '<form action="?" method="POST">';
            echo '<input type="hidden" name="clave" value="procesaformulario">';    // Si no hay una clave 'procesaformulario' enséñame el formulario, pero si la hay, pasa a procesar el formulario
            echo '<input type="hidden" name="tabla" value="'.$tabla.'">';           
            
            $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword, $mydb);     // - Cambiamos los campos según 'config.php'
            
            // Luego quiero ver las columnas
            $consulta = "SHOW FULL COLUMNS FROM ".$tabla;
            $resultado = $mysqli->query($consulta);
            while($fila = $resultado->fetch_assoc()){
                if(json_decode($fila["Comment"])->visible == "true"){   // Para ocultar la clave primaria  - Ocultamos el 'epoch'
                    // json_decode, mínimo y máximo de caracteres
                    preg_match('#\((.*?)\)#', $fila["Type"], $match);
                    echo '
                        <div class="campo">
                            <h3>'.json_decode($fila["Comment"])->titulo.'</h3> 
                            <p>'.json_decode($fila["Comment"])->descripcion.' - Caracteres mínimos '.json_decode($fila["Comment"])->min.' máximos '.$match[1].'</p>
                            '; 
                            if($fila["Null"] == "NO"){echo "<p>*Este campo es requerido</p>";}
                            
                            if(json_decode($fila["Comment"])->deshabilitado == "true"){echo "<p>*Este campo está deshabilitado ya que lo rellena automáticamente el sistema</p>";}
                            
                            echo'
                            <div class="contienecampo">
                                <table><tr><td width="80%">
                                    <input type="'.json_decode($fila["Comment"])->tipodato.'" name="'.$fila["Field"].'" id="'.$fila["Field"].'"
                                        ';
                                        if($fila["Null"] == "NO"){echo " required ";}
                                        if(json_decode($fila["Comment"])->deshabilitado == "true"){echo " readonly ";}
                                        //if($fila["Field"] == "epoch"){echo " disabled ";}
                                        // Para definir el máximo de caracteres en cada campo
                                        preg_match('#\((.*?)\)#', $fila["Type"], $match);
                                        echo '
                                        maxlength = "'.$match[1].'"
                                        minlength = "'.json_decode($fila["Comment"])->min.'"
                                        placeholder = "'.json_decode($fila["Comment"])->placeholder.'"
                                        ';
                                        // Si existe un campo en los json con el campo 'parametroget', le pone su valor en el código html
                                        if(isset(json_decode($fila["Comment"])->parametroget)){
                                            echo ' value = "'.$_GET[json_decode($fila["Comment"])->parametroget].'"';
                                        }
                                        echo '
                                    >
                                    </td><td>
                                <div class="tipocampo"><i class="'.json_decode($fila["Comment"])->icono.'"></i></div>
                                </td><tr></table>
                            </div>
                            <div class="clearfix"></div>
                        </div>
                        
                    ';  // El 'clearfix' borra todas las flotaciones                                                   
                }
            }

            echo '<input type="submit">';
            $mysqli -> close();
        }
        function procesaformulario(){   
            // Vamos a analizar qué es lo que viene antes de meterlo
            foreach($_REQUEST as $nombre_campo => $valor){  // REQUEST lo atrapa todo
                //echo "El campo es: ".$nombre_campo." y el valor es: ".$valor;
                // Para evitar ataques de inyecciones SQL
                if(preg_match('~\b(delete|drop|truncate)\b~i',$nombre_campo)){
                    // 'implode' une elementos de un array en un string
                    $volcado = implode(",", $_REQUEST).", ".$_SERVER['REMOTE_ADDR'].", ".$_SERVER['HTTP_USER_AGENT']."\n";  // REMOTE_ADDR guara la ip y HTTP_USER_AGENT el navegador
                    $myfile = fopen("volcado.txt", "a");
                    fwrite($myfile, $volcado);
                    die("Ejecución detenida");
                }
                if(preg_match('~\b(delete|drop|truncate)\b~i',$valor)){
                    $volcado = implode(",", $_REQUEST).", ".$_SERVER['REMOTE_ADDR'].", ".$_SERVER['HTTP_USER_AGENT']."\n";
                    $myfile = fopen("volcado.txt", "a");
                    fwrite($myfile, $volcado);
                    die("Ejecución detenida");
                }
            }
            
            include "config.php";
            $listadocolumnas = "";
            $listadovalores = "";
            foreach($_POST as $nombre_campo => $valor){
                //echo "Recibo el campo ".$nombre_campo." con el valor ".$valor."<br>";
                if($nombre_campo != 'tabla' && $nombre_campo != 'clave'){   // Metemos los valores del POST en una cadena...
                    $listadocolumnas .= ",".$nombre_campo."";
                    $listadovalores   .= ",'".$valor."'";     
                }
            }

            
            //////////////////// ▼ CORREO ELECTRÓNICO ▼ ////////////////////
            $cabeceras = 'From: info@joanbanyulstorres.es' . "\r\n" .       // noreply@joanbanyulstorres.es
            'Reply-To: info@joanbanyulstorres.es' . "\r\n" .
            'X-Mailer: PHP/' . phpversion();
            $cabeceras .= 'MIME-Version: 1.0' . "\r\n";
            $cabeceras .= 'Content-type: text/html; charset=iso-8859-1' . "\r\n";
            $mensaje = "<h1>Has enviado un formulario al sistema de entregas</h1><br><p>A continuación te mostramos un comprobante de los campos que has enviado desde formulario</p><br>";
            foreach($_POST as $nombre_campo => $valor){
                if($nombre_campo != 'tabla' && $nombre_campo != 'clave'){   // Metemos los valores del POST en una cadena...
                    $mensaje .= "".ucfirst($nombre_campo).": <b>".$valor."</b><br>";    // 'ucfirst' pone la primera letra en mayúscula
                }
            }

            $mensaje .= "<br><p>Puedes consultar tus entregas previamente realizadas haciendo click: ";
            $mensaje .= "<a href='https://joanbanyulstorres.es/proyectos/entregas/informe.php?clave=".codifica($_POST['email'])."'>AQUI</a></p>";
            $mensaje .= "<p style='color:red'>IMPORTANTE: Este enlace contiene una clave con tu identificación - no compartas este correo electrónico con nadie</p><br>";

            mail(
                $_POST['email'],
                "Formulario enviado",
                $mensaje,
                $cabeceras
            );
            //////////////////// ▲ CORREO ELECTRÓNICO ▲ ////////////////////

            $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword ,$mydb);
            $consulta = "INSERT INTO ".$_POST['tabla']." (Identificador".$listadocolumnas.") VALUES (NULL".$listadovalores.")";     // Y los lanzamos en una consulta
            //echo $consulta;

            $mysqli->query($consulta);                                          // Metemos la información en la BD
            include "registro.php";     // Despúes de guardar un formulario, se registra
            echo '
                <div class="notice">
                    <h1>Registro guardado correctamente</h1>
                    <p>Tu registro se ha guardado correctamente en la aplicación. Redirigiendo en 5 segundos...</p>
                </div>
            ';
            echo '<meta http-equiv="refresh" content="5"; url=?/>';
             
        }

        function leer($tabla){
            include "config.php";
            //echo "A continuación se muestra el contenido de la tabla: " . $tabla;
            $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword, $mydb); 
            $consulta = "SHOW FULL COLUMNS FROM ". $tabla;
            $resultado = $mysqli->query($consulta);
            echo '<table>';
            
			echo '<tr>';
			$contadorcolumna = 0;
            while($fila = $resultado->fetch_assoc()){
                echo '<th>'.json_decode($fila["Comment"])->titulo.'</th>';
				// Nombres de las columnas en el panel de control
				$nombrecolumna[$contadorcolumna] = $fila["Field"];
				$contadorcolumna++;
            }
            echo '<th>Operaciones</th>';
			echo '</tr>';
			
			//////////////////// ▼ BUSCADORES POR CAMPO ▼ ////////////////////
			$consulta = "SHOW FULL COLUMNS FROM ". $tabla;
			$resultado = $mysqli->query($consulta);
			echo '<tr>';
			echo '<form action="?tabla='.$tabla.'&buscar=si" method="POST">';
            
			// Para guardar los comentarios
			$contadorcolumna = 0;
			
			while($fila = $resultado->fetch_assoc()){
                echo '<th><input type="text" name="'.$fila["Field"].'" class="campobuscador"><i class="fa-solid fa-magnifying-glass iconobusca"></i></th>';
				$comentarios[$contadorcolumna] = $fila['Comment'];
				$contadorcolumna++;
			}
			echo '<th><input type="submit" value="Buscar"></th>';
			echo '</form>';
			echo '</tr>';
			//////////////////// ▲ BUSCADORES POR CAMPO ▲ ////////////////////
			
			//////////////////// ▼ CONSULTA LEER ▼ ////////////////////--------------------- *NUEVO: cambio en la estructura de la consulta*
			$consulta = "
			SELECT * FROM ".$tabla." ";
			if(isset($_GET['buscar'])){
				$consulta .= " WHERE ";
				foreach($_POST as $clave=> $valor){
					$consulta .= $clave." LIKE '%".$valor."%' AND ";
				}
				$consulta .= " true";
			}
			if(!isset($_GET['buscar'])){		// Para anular el OFFSET al realizar una búsqueda
				$consulta .=" LIMIT ".$_SESSION['elementosporpagina']." ";
				$consulta .=" OFFSET ".($_SESSION['elementosporpagina']*$_SESSION['pagina'])." ";
			}
			$resultado = $mysqli->query($consulta);
			//////////////////// ▲ CONSULTA LEER ▲ ////////////////////
			
			while($fila = $resultado->fetch_assoc()){
				$identificador = "";	// Carga del indetificador
				
				echo '<tr>';
				
				$contadorcolumna = 0;
				
				foreach($fila as $nombre_campo => $valor){
					if($nombrecolumna[$contadorcolumna] == "Identificador"){$identificador = $valor;}	// Para poner el identificador a cada registro
					if(json_decode($comentarios[$contadorcolumna])->FKtabla != ""){	// petición cruzada que lleva a la tabla asignaturas*
						$consulta2 = "SELECT ".json_decode($comentarios[$contadorcolumna])->FKmostrar." AS campo FROM ".json_decode($comentarios[$contadorcolumna])->FKtabla." WHERE ".json_decode($comentarios[$contadorcolumna])->FKclave." = '".$valor."'";
						$resultado2 = $mysqli->query($consulta2);
						echo '<td externo="si" tabla="'.$tabla.'" claveexterna="'.json_decode($comentarios[$contadorcolumna])->FKclave.'" tablaexterna="'.json_decode($comentarios[$contadorcolumna])->FKtabla.'" columna="'.$nombrecolumna[$contadorcolumna].'" identificador="'.$identificador.'" columnaexterna="'.json_decode($comentarios[$contadorcolumna])->FKmostrar.'">';
						while($fila2 = $resultado2->fetch_assoc()){
							echo '<b>'.$valor."</b> - ".$fila2['campo'].'';
						}
						echo '</td>';
					}else{
						echo '<td externo="no"  class="'.$nombrecolumna[$contadorcolumna].'" columna="'.$nombrecolumna[$contadorcolumna].'" tabla="'.$tabla.'" identificador="'.$identificador.'" ';
						// URLs y EMAILs clickables
						if(filter_var($valor, FILTER_VALIDATE_URL)){echo "urlsi";}
						echo '">';
						if(filter_var($valor, FILTER_VALIDATE_URL)){echo "<a href='".$valor."' target='_blank'>";}	// target='_blank' -> abre el enlace en una nueva pestaña del navegador
						if(filter_var($valor, FILTER_VALIDATE_EMAIL)){echo "<a href='mailto:".$valor."' target='_blank'>";}
						echo $valor; 
						if(filter_var($valor, FILTER_VALIDATE_EMAIL)){echo "</a>";}
						if(filter_var($valor, FILTER_VALIDATE_URL)){echo "</a>";}
						
						/* // Miniaturas de los vídeos
						if(filter_var($valor, FILTER_VALIDATE_URL)){ 
							$url = $valor;
							$parsed = parse_url($url);
							if($parsed['host'] == "www.youtube.com" || $parsed['host'] == "youtu.be"){
								$partes = parse_url($url);
								parse_str($partes['query'], $query);
								$miparte = $query['v'];
								echo '<iframe width="300" height="200" src="https://www.youtube.com/embed/'.$miparte.'" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>';
							}
						} */
						
						echo '</td>';
					}
					$contadorcolumna++;	
				}
				echo '<td>';
				echo '<a href="?tabla='.$_GET['tabla'].'&informe='.$fila['Identificador'].'"><i class="fa-solid fa-file"></i></a>';		// ------------------------- *NUEVO*				
				echo '<a href="?tabla='.$_GET['tabla'].'&update='.$fila['Identificador'].'"><i class="fa-solid fa-pen"></i></a>';
				echo '<a href="?tabla='.$_GET['tabla'].'&delete='.$fila['Identificador'].'"><i class="fa-solid fa-trash"></i></a>';
				
				echo '</td>';
				echo '</tr>';
			}
			
			echo '</table>';
			echo '<a href="?create='.$_GET['tabla'].'" id="create"><i class="fa-solid fa-circle-plus"></i>';
			
			// Botones de paginación
			echo '<div class="paginacion">	
				<a href="?tabla='.$_GET['tabla'].'&pagina=primera"><i class="fa-solid fa-backward"></i></i></a>
				<a href="?tabla='.$_GET['tabla'].'&pagina=anterior"><i class="fa-solid fa-circle-left"></i></a>
				<a href="?tabla='.$_GET['tabla'].'&pagina=siguiente"><i class="fa-solid fa-circle-right"></i></a>
				<a href="?tabla='.$_GET['tabla'].'&pagina=ultima"><i class="fa-solid fa-forward"></i></a>
			</div>';	
        }
		
		function informe($tabla, $identificador){		// -------------------------------------------------------------------------------------------------------- *NUEVO*
			echo '<h1>Informe</h1>';
			
			include "config.php";
            $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword, $mydb); 
            $consulta = "SELECT * FROM ". $tabla." WHERE Identificador = ".$identificador." ";
            $resultado = $mysqli->query($consulta);
            
			// Tabla con los datos de los campos del registro seleccionado
			echo '<table>';
            while($fila = $resultado->fetch_assoc()){
				foreach($fila as $indice=>$valor){
					echo '<tr><td>'.$indice.'</td><td>'.$valor.'</td></tr>';
				}
			}
			echo '</table>';
			
			echo '<table>';
			$consulta = "SELECT * FROM informes WHERE tabla = '".$tabla."'";
            $resultado = $mysqli->query($consulta);
            while($fila = $resultado->fetch_assoc()){
				echo "La petición que se ve a realizar es: ".str_replace('[X]',$identificador, $fila['consulta']);
				$consulta2 = str_replace('[X]',$identificador, $fila['consulta']);
				$resultado2 = $mysqli -> query($consulta2);
				while($fila2 = $resultado2->fetch_assoc()){
					echo '<tr>';
					foreach($fila2 as $clave=>$valor){
						echo '<td>'.$valor.'</td>';
					}
					echo '</tr>';
				}
			}
			echo '</table>';
		}

		function insertar($tabla){  // Misma función que 'formulario'                                      
            include "config.php";
			echo '<form action="?tabla='.$tabla.'" method="POST">';					// Cuando procesa, vuelve a la tabla original
			echo '<input type="hidden" name="clave" value="procesainsertar">';
            echo '<input type="hidden" name="tabla" value="'.$tabla.'">';           
            
            $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword, $mydb);
            
            // Luego quiero ver las columnas
            $consulta = "SHOW FULL COLUMNS FROM ".$tabla;
            $resultado = $mysqli->query($consulta);
            while($fila = $resultado->fetch_assoc()){
                if(json_decode($fila["Comment"])->visible == "true"){   // Para ocultar la clave primaria  - Ocultamos el 'epoch'
                    // json_decode, mínimo y máximo de caracteres
                    preg_match('#\((.*?)\)#', $fila["Type"], $match);
                    echo '
                        <div class="campo">
                            <h3>'.json_decode($fila["Comment"])->titulo.'</h3> 
                            <p>'.json_decode($fila["Comment"])->descripcion.' - Caracteres mínimos '.json_decode($fila["Comment"])->min.' máximos '.$match[1].'</p>
                            '; 
                            if($fila["Null"] == "NO"){echo "<p>*Este campo es requerido</p>";}
                            
                            if(json_decode($fila["Comment"])->deshabilitado == "true"){echo "<p>*Este campo está deshabilitado ya que lo rellena automáticamente el sistema</p>";}
                            
                            echo'
                            <div class="contienecampo">
                                <table><tr><td width="80%">
                                    <input type="'.json_decode($fila["Comment"])->tipodato.'" name="'.$fila["Field"].'" id="'.$fila["Field"].'"
                                        ';
                                        if($fila["Null"] == "NO"){echo " required ";}
                                        if(json_decode($fila["Comment"])->deshabilitado == "true"){echo " readonly ";}
                                        //if($fila["Field"] == "epoch"){echo " disabled ";}
                                        // Para definir el máximo de caracteres en cada campo
                                        preg_match('#\((.*?)\)#', $fila["Type"], $match);
                                        echo '
                                        maxlength = "'.$match[1].'"
                                        minlength = "'.json_decode($fila["Comment"])->min.'"
                                        placeholder = "'.json_decode($fila["Comment"])->placeholder.'"
                                        ';
                                        // Si existe un campo en los json con el campo 'parametroget', le pone su valor en el código html
                                        if(isset(json_decode($fila["Comment"])->parametroget)){
                                            echo ' value = "'.$_GET[json_decode($fila["Comment"])->parametroget].'"';
                                        }
                                        echo '
                                    >
                                    </td><td>
                                <div class="tipocampo"><i class="'.json_decode($fila["Comment"])->icono.'"></i></div>
                                </td><tr></table>
                            </div>
                            <div class="clearfix"></div>
                        </div>
                        
                    ';  // El 'clearfix' borra todas las flotaciones                                                   
                }
            }

            echo '<input type="submit">';
            $mysqli -> close();
        }
		
		
		function procesainsertar(){
            // Vamos a analizar qué es lo que viene antes de meterlo
            foreach($_REQUEST as $nombre_campo => $valor){  // REQUEST lo atrapa todo
                //echo "El campo es: ".$nombre_campo." y el valor es: ".$valor;
                // Para evitar ataques de inyecciones SQL
                if(preg_match('~\b(delete|drop|truncate)\b~i',$nombre_campo)){
                    // 'implode' une elementos de un array en un string
                    $volcado = implode(",", $_REQUEST).", ".$_SERVER['REMOTE_ADDR'].", ".$_SERVER['HTTP_USER_AGENT']."\n";  // REMOTE_ADDR guara la ip y HTTP_USER_AGENT el navegador
                    $myfile = fopen("volcado.txt", "a");
                    fwrite($myfile, $volcado);
                    die("Ejecución detenida");
                }
                if(preg_match('~\b(delete|drop|truncate)\b~i',$valor)){
                    $volcado = implode(",", $_REQUEST).", ".$_SERVER['REMOTE_ADDR'].", ".$_SERVER['HTTP_USER_AGENT']."\n";
                    $myfile = fopen("volcado.txt", "a");
                    fwrite($myfile, $volcado);
                    die("Ejecución detenida");
                }
            }
            
            include "config.php";
            $listadocolumnas = "";
            $listadovalores = "";
            foreach($_POST as $nombre_campo => $valor){
                //echo "Recibo el campo ".$nombre_campo." con el valor ".$valor."<br>";
                if($nombre_campo != 'tabla' && $nombre_campo != 'clave'){   // Metemos los valores del POST en una cadena...
                    $listadocolumnas .= ",".$nombre_campo."";
                    $listadovalores   .= ",'".$valor."'";     
                }
            }

            $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword ,$mydb);
            $consulta = "INSERT INTO ".$_POST['tabla']." (Identificador".$listadocolumnas.") VALUES (NULL".$listadovalores.")";     // Y los lanzamos en una consulta
            //echo $consulta;

            $mysqli->query($consulta);                                          // Metemos la información en la BD
            include "registro.php";     // Despúes de guardar un formulario, se registra
            
        }
		
		function delete($tabla, $identificador){
            
            include "config.php";

            $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword ,$mydb);
            $consulta = "DELETE FROM ".$tabla." WHERE Identificador = ".$identificador." ";     // Y los lanzamos en una consulta
            //echo $consulta;

            $mysqli->query($consulta);  // Metemos la información en la BD
            include "registro.php";     // Despúes de guardar un formulario, se registra
            
        }
		
		function update($tabla, $identificador){                                   
            include "config.php";
			echo '<form action="?tabla='.$tabla.'" method="POST">';					// Cuando procesa, vuelve a la tabla original
			echo '<input type="hidden" name="clave" value="procesaupdate">';
            echo '<input type="hidden" name="tabla" value="'.$tabla.'">';
			echo '<input type="hidden" name="identificador" value="'.$identificador.'">';			
            
            $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword, $mydb);     // Cambiamos los campos según 'config.php'
            
            // Luego quiero ver las columnas
            $consulta = "SHOW FULL COLUMNS FROM ".$tabla;
            $resultado = $mysqli->query($consulta);
            while($fila = $resultado->fetch_assoc()){
                if(json_decode($fila["Comment"])->visible == "true"){   // Para ocultar la clave primaria  - Ocultamos el 'epoch'
                    // json_decode, mínimo y máximo de caracteres
                    preg_match('#\((.*?)\)#', $fila["Type"], $match);
                    echo '
                        <div class="campo">
                            <h3>'.json_decode($fila["Comment"])->titulo.'</h3> 
                            <p>'.json_decode($fila["Comment"])->descripcion.' - Caracteres mínimos '.json_decode($fila["Comment"])->min.' máximos '.$match[1].'</p>
                            '; 
                            if($fila["Null"] == "NO"){echo "<p>*Este campo es requerido</p>";}
                            
                            if(json_decode($fila["Comment"])->deshabilitado == "true"){echo "<p>*Este campo está deshabilitado ya que lo rellena automáticamente el sistema</p>";}
                            
                            echo'
                            <div class="contienecampo">
                                <table><tr><td width="80%">
                                    <input type="'.json_decode($fila["Comment"])->tipodato.'" name="'.$fila["Field"].'" id="'.$fila["Field"].'"
                                        ';
                                        if($fila["Null"] == "NO"){echo " required ";}
                                        if(json_decode($fila["Comment"])->deshabilitado == "true"){echo " readonly ";}
                                        //if($fila["Field"] == "epoch"){echo " disabled ";}
                                        // Para definir el máximo de caracteres en cada campo
                                        preg_match('#\((.*?)\)#', $fila["Type"], $match);
                                        echo '
                                        maxlength = "'.$match[1].'"
                                        minlength = "'.json_decode($fila["Comment"])->min.'"
                                        placeholder = "'.json_decode($fila["Comment"])->placeholder.'"
                                        ';
                                        
										// Me conecto a la base de datos y busco el valor
										$consulta2 = "SELECT * FROM " .$tabla. " WHERE Identificador = " .$identificador." ";
										$resultado2 = $mysqli -> query($consulta2);
										while($fila2 = $resultado2 -> fetch_assoc()){
											echo 'value = "'.$fila2[$fila["Field"]].'"';
										}
										
                                        echo '
                                    >
                                    </td><td>
                                <div class="tipocampo"><i class="'.json_decode($fila["Comment"])->icono.'"></i></div>
                                </td><tr></table>
                            </div>
                            <div class="clearfix"></div>
                        </div>
                        
                    ';  // El 'clearfix' borra todas las flotaciones                                                   
                }
            }

            echo '<input type="submit">';
            $mysqli -> close();
        }
		
		
		function procesaupdate($tabla, $identificador){
            // Vamos a analizar qué es lo que viene antes de meterlo
            foreach($_REQUEST as $nombre_campo => $valor){  // REQUEST lo atrapa todo
                //echo "El campo es: ".$nombre_campo." y el valor es: ".$valor;
                // Para evitar ataques de inyecciones SQL
                if(preg_match('~\b(delete|drop|truncate)\b~i',$nombre_campo)){
                    // 'implode' une elementos de un array en un string
                    $volcado = implode(",", $_REQUEST).", ".$_SERVER['REMOTE_ADDR'].", ".$_SERVER['HTTP_USER_AGENT']."\n";  // REMOTE_ADDR guara la ip y HTTP_USER_AGENT el navegador
                    $myfile = fopen("volcado.txt", "a");
                    fwrite($myfile, $volcado);
                    die("Ejecución detenida");
                }
                if(preg_match('~\b(delete|drop|truncate)\b~i',$valor)){
                    $volcado = implode(",", $_REQUEST).", ".$_SERVER['REMOTE_ADDR'].", ".$_SERVER['HTTP_USER_AGENT']."\n";
                    $myfile = fopen("volcado.txt", "a");
                    fwrite($myfile, $volcado);
                    die("Ejecución detenida");
                }
            }
            
            include "config.php";
            $cadena = "";
            foreach($_POST as $nombre_campo => $valor){
                //echo "Recibo el campo ".$nombre_campo." con el valor ".$valor."<br>";
                if($nombre_campo != 'tabla' && $nombre_campo != 'clave'){   // Metemos los valores del POST en una cadena...
                    $cadena .= $nombre_campo."='".$valor."',"; 
                }
            }
			$cadena = substr($cadena, 0, -1);

            $mysqli = new mysqli($mydbserver, $mydbuser, $mydbpassword ,$mydb);
			$consulta = "UPDATE ".$tabla." SET ".$cadena." WHERE Identificador = ".$identificador." ";
			
            //echo $consulta;

            $mysqli->query($consulta);                                          // Metemos la información en la BD
            include "registro.php";     // Despúes de guardar un formulario, se registra
            
        }
		
    }
?>