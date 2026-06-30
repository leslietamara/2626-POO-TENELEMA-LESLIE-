class Producto:
    """
    Clase padre que representa un producto general del restaurante.
    """
    def __init__(self, nombre, precio, disponibilidad=True):
        self.nombre = nombre
        self.__precio = precio # Atributo encapsulado (privado)
        self.disponibilidad = disponibilidad
        
    def obtener_precio(self):
        """Método de acceso para el precio encapsulado."""
        return self.__precio
        
    def cambiar_precio(self, nuevo_precio):
        """Método de modificación para el precio, incluye validación."""
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Error: El precio no puede ser negativo ni cero.")
            
    def mostrar_informacion(self):
        """Muestra la información general del producto."""
        estado = "Disponible" if self.disponibilidad else "Agotado"
        return f"Producto: {self.nombre} | Precio: ${self.__precio:.2f} | Estado: {estado}"
