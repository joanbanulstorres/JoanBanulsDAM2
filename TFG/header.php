<header>
    <h1>Limpiadores Medioambientales</h1>
    <button id="inicio" class="btn_header"><a href="index.php">Inicio</a></button>
    <div class="separador"></div>
    <button id="sobrenosotros" class="btn_header"><a href="sobrenosotros.php">Sobre Limpiadores Medioambientales</a></button>
    <div class="separador"></div>
    <div class="seudo_btn">
        <i id="icono_miperfil" class="fa-solid fa-user"></i>
            <?php
                if(isset($_SESSION['usuario'])){
                    echo '<button id="miperfil" class="btn_header btn_perfil" style="color: #000000;"><a href="miperfil.php">'.$_SESSION['usuario'].'</a></button>';
                }else{
                    echo '<button id="miperfil" class="btn_header btn_perfil" style="color: #000000;"><a href="login.php">Iniciar sesión</a></button>';
                }
            ?>
        </button>
    </div>
</header>