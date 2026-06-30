from .producto import Producto

class Platillo(Producto):
    """
    Clase hija que representa un platillo, hereda de Producto.
    """
    def __init__(self, nombre, precio, calorias, disponibilidad=True):
        # Utilización de super() para inicializar atributos de la clase padre
        super().__init__(nombre, precio, disponibilidad)
        self.calorias = calorias
        
    def mostrar_informacion(self):
        """Sobrescribe el método de la clase padre para mostrar detalles específicos del platillo."""
        # Se llama al método obtener_precio() ya que __precio está encapsulado en la clase padre
        estado = "Disponible" if self.disponibilidad else "Agotado"
        return f"[Platillo] {self.nombre} | Precio: ${self.obtener_precio():.2f} | Calorías: {self.calorias} kcal | Estado: {estado}"
