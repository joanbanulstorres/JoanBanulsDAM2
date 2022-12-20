// Creamos una plantilla para un personaje 
class Npc{
    // Dotamos al personaje de una serie de propiedades iniciales
    constructor(x, y, z, direccion, direccionisometrica, tiemponacimiento, estadoanimacion_npc, energia, color){
        this.x = Math.random()*(terrenox2-terrenox1)+terrenox1;    //Los npcs solo pueden nacer dentro del terreno (amplitud del terreno + posición inicial)
        this.y = Math.random()*(terrenoy2-terrenoy1)+terrenoy1;
        this.direccion = Math.PI*2*Math.random(); // Cada NPC tiene un ángulo de dirección distinto
        this.direccionisometrica = Math.floor(Math.random()*4); // Redondeando (hacia abajo) para que no hayan decimales
        this.tiemponacimiento = 0;
        this.estadoanimacion_npc = Math.floor(Math.random()*7);  // Cada NPC tiene une frame de animación incial aleatorio
        this.energia = 100;
        this.color = Math.floor(Math.random()*6);
    }
    // Creamos un método para gestionar el movimiento de los NPCs
    mueve(){
        // Los NPCs va envejeciendo
        this.tiemponacimiento += 1;

        // Actualizamos el ángulo en radianes según la nomenclatura de ángulos de 0 a 3
        if(this.direccionisometrica == 0){
            this.direccion = 0;
        }else if(this.direccionisometrica == 1){
            this.direccion = Math.PI/2;
        }else if(this.direccionisometrica == 2){
            this.direccion = Math.PI;
        }else if(this.direccionisometrica == 3){
            this.direccion = Math.PI*1.5;
        }
        
        // Se actualiza la posición de los NPCs
        this.x -= Math.cos(this.direccion);     // -= Para que los NPCs caminen hacia delante y no hacia atrás
        this.y -= Math.sin(this.direccion);
        
        // Va cambiando la animación de caminar
        this.estadoanimacion_npc++;
        if(this.estadoanimacion_npc > 7){this.estadoanimacion_npc = 0;}  // Así nos movemos entre 0 y 7
        
        // Cada 100 iteraciones, pierde un punto de energía
        if(this.tiemponacimiento % 100 == 0){this.pierdeenergia();}
        
        // Cambia de dirección
        //this.cambiadireccion();
        
        // Calcula las colisiones
        this.colisiona();      
    }
    
    // *NUEVO*
    persigue(){
        this.estadoanimacion_npc++;
        if(this.estadoanimacion_npc > 7){this.estadoanimacion_npc = 0;}
        // Para ver en en cuál de los dos ejes les conviene moverse a los npcs
        //var distanciax = Math.abs(posx - this.x);
        //var distanciay = Math.abs(posy - this.y);
        
        // Para que los npcs persigan al personaje
        this.x -= (this.x - posx)/100;
        this.y -= (this.y - posy)/100;
        
        //this.x -= Math.cos(this.direccion);     
        //this.y -= Math.sin(this.direccion);
        
        this.colisiona();     /* NUEVO */
    }
    
    // Los NPCs cambian de dirección cada 100 uds de vida 
    cambiadireccion(){
            if(this.tiemponacimiento % 100 == 0){
                this.direccionisometrica = Math.floor(Math.random()*4)
            } 
    }
    
    // Para que los NPCs no se puedan salir del terreno
    colisiona(){
/*        if(
            this.x > terrenox2
            ||
            this.x < terrenox1
            ||
            this.y > terrenoy2
            ||
            this.y < terrenoy1
            ){
                if(this.direccionisometrica == 1){this.direccionisometrica = 3;}
                else if(this.direccionisometrica == 3){this.direccionisometrica = 1;}
                else if(this.direccionisometrica == 0){this.direccionisometrica = 2;}
                else if(this.direccionisometrica == 2){this.direccionisometrica = 0;}
            }   // Cuando un NPC se vaya a salir por la derecha, por la izquierda, por abajo o por arriba hace un giro de 180º(PI radianes)*/
        
        /* NUEVO */
        var colisionapixel = contextomapa.getImageData(this.x/50+1, this.y/50+1, 1, 1); // 1:1 -> 1 pixel / +1 para ajustar hasta dónde llegan los npcs
        var alpha = colisionapixel.data[3]; // 3 -> transparencia
        if(alpha == 0){
            if(this.direccionisometrica == 1){this.direccionisometrica = 3;}
                else if(this.direccionisometrica == 3){this.direccionisometrica = 1;}
                else if(this.direccionisometrica == 0){this.direccionisometrica = 2;}
                else if(this.direccionisometrica == 2){this.direccionisometrica = 0;}
        }
        
    }
    pierdeenergia(){
        this.energia -= 1;
    }
}