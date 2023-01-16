<!-- Código importado desde la página de A-Frame -->
<html>
  <head>
    <script src="https://aframe.io/releases/1.4.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene light="defaultLightsEnabled: false">
      <a-entity light="type: ambient; color: #CCC"></a-entity>
      <a-entity light="type: directional;
                   castShadow: true;
                   intensity: 0.4;
                   shadowCameraVisible: true;"
                position="-5 3 1.5"></a-entity>
        <?php
          for($x = -5; $x<5; $x+=2){
            for($y = -5; $y<5; $y+=2){
              for($z = -5; $z<5; $z+=2){
                echo '
                  <a-box position="'.$x.' '.$y.' '.$z.'" rotation="0 45 0" scale="0.5 0.5 0.5" color="#4CC3D9" shadow="cast: true"></a-box>
                ';
              }
            }
          }
        ?>
      <a-sky color="#ECECEC"></a-sky>
    </a-scene>
  </body>
</html>