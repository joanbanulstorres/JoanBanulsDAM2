<!-- Código importado desde la página de A-Frame -->
<html>
  <head>
    <script src="https://aframe.io/releases/1.4.0/aframe.min.js"></script>
  </head>
  <body>

    <a-scene light="defaultLightsEnabled: false">
        <a-entity light="type: ambient; intensity: 0.5;"></a-entity>
        <a-sky color="#BFE6FF"></a-sky>  
        <?php
            $randomparedes = 1;
            for($x=0; $x<20; $x+=4){
                for($z=0; $z<20; $z+=4){
                    echo '<a-box position="'.$x.' 0 '.$z.'" rotation="0 0 0" scale="4 0.1 4" color="#CC0000" shadow="cast: true" material="src:tiles.jpg; color:white; roughness:0.5; metalness:0.2"></a-box>';
                    echo '<a-box position="'.$x.' 3 '.$z.'" rotation="0 0 0" scale="4 0.1 4" color="#CC0000" shadow="cast: true" material="src:ceiling.jpg; color:white; roughness:0.5; metalness:0.2"></a-box>';
                    if(rand(0,10)<$randomparedes){
                        echo '<a-box position="'.($x+2).' 1.5 '.$z.'" rotation="0 0 0" scale="0.1 3 4" color="#CC0000" shadow="cast: true" material="src:wall.jpg; color:white; roughness:0.5; metalness:0.2"></a-box>';
                    }
                    if(rand(0,10)<$randomparedes){
                        echo '<a-box position="'.($x-2).' 1.5 '.$z.'" rotation="0 0 0" scale="0.1 3 4" color="#CC0000" shadow="cast: true" material="src:wall.jpg; color:white; roughness:0.5; metalness:0.2"></a-box>';
                    }
                    if(rand(0,10)<$randomparedes){
                        echo '<a-box position="'.$x.' 1.5 '.($z+2).'" rotation="0 90 0" scale="0.1 3 4" color="#CC0000" shadow="cast: true" material="src:wall.jpg; color:white; roughness:0.5; metalness:0.2"></a-box>';
                    }
                    if(rand(0,10)<$randomparedes){
                        echo '<a-box position="'.$x.' 1.5 '.($z-2).'" rotation="0 90 0" scale="0.1 3 4" color="#CC0000" shadow="cast: true" material="src:wall.jpg; color:white; roughness:0.5; metalness:0.2"></a-box>';
                    }
                    if(rand(0,10)<$randomparedes){
                        echo '
                            <a-entity light="type: spot;
                            castShadow: true;
                            intensity: 0.4;
                            penumbra: 0.5;
                            shadowCameraVisible: false;"
                            position="'.$x.' 3 '.$z.'";
                            rotation="-90 0 0"
                            ></a-entity>
                        ';
                    }
                }
            }
        ?>
    </a-scene>

  </body>
</html>