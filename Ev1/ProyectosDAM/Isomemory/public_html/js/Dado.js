class Dado{
    constructor(dx, dy, dx_anterior, dy_anterior){
        // La posición inicial de los dados es aleatoria
        this.dx = 425 + (Math.floor(Math.random() * 9)) * 45 + 18;  // + 18 y -12 para corregir un desfase que hay al dibujar los dados
        this.dy = -150 + (Math.floor(Math.random() * 9)) * 45 + 12;
        
        // Se guardan las posiciones del subnivel 1 para poder compararlas con las del subnivel 2
        this.dx_anterior = this.dx;
        this.dy_anterior = this.dy;
    }
}