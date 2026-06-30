from .producto import Producto

class Bebida(Producto):
    """
    Clase hija que representa una bebida, hereda de Producto.
    """
    def __init__(self, nombre, precio, volumen_ml, disponibilidad=True):
        # Utilización de super() para inicializar atributos de la clase padre
        super().__init__(nombre, precio, disponibilidad)
        self.volumen_ml = volumen_ml
        
    def mostrar_informacion(self):
        """Sobrescribe el método de la clase padre para mostrar detalles específicos de la bebida."""
        estado = "Disponible" if self.disponibilidad else "Agotado"
        return f"[Bebida] {self.nombre} | Precio: ${self.obtener_precio():.2f} | Volumen: {self.volumen_ml} ml | Estado: {estado}"
