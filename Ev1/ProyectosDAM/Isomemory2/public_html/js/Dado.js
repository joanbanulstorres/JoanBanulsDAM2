class Dado{
    constructor(dx, dy, dx_anterior, dy_anterior){
        // La posición inicial de los dados es aleatoria
        this.dx = 473 + 22 + (Math.floor(Math.random() * 5)) * distancia;  // +22 y +15 para corregir un desfase que hay al dibujar los dados
        this.dy = -95 + 15 + (Math.floor(Math.random() * 5)) * distancia;
        
//        this.dx = 587 + 22;
//        this.dy = 19 + 15;
        
        // Se guardan las posiciones del subnivel 1 para poder compararlas con las del subnivel 2
        this.dx_anterior = this.dx;
        this.dy_anterior = this.dy;
    }
}