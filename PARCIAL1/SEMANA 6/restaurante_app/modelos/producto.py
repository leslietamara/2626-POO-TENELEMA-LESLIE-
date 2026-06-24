# Clase Producto - Representa un producto del restaurante

class Producto:
    """
    Clase que representa un producto disponible en el restaurante.
    Contiene información sobre el producto y su precio.
    """

    def __init__(self, nombre: str, descripcion: str, precio: float, categoria: str) -> None:
        """
        Constructor de la clase Producto.

        Args:
            nombre: Nombre del producto
            descripcion: Descripción breve del producto
            precio: Precio del producto en moneda local
            categoria: Categoría del producto (ej: Entrada, Plato Principal, Bebida)
        """
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.precio: float = precio
        self.categoria: str = categoria

    def __str__(self) -> str:
        """
        Representación en texto del producto.
        Retorna una cadena con la información del producto.
        """
        return f"{self.nombre} (${self.precio:.2f}) - {self.descripcion}"

    def obtener_informacion(self) -> dict:
        """
        Método que retorna la información completa del producto.
        """
        return {
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "categoria": self.categoria
        }

    def mostrar_detalles(self) -> None:
        """
        Muestra los detalles del producto de forma formateada.
        """
        print(f"\n  Producto: {self.nombre}")
        print(f"  Descripción: {self.descripcion}")
        print(f"  Precio: ${self.precio:.2f}")
        print(f"  Categoría: {self.categoria}")


