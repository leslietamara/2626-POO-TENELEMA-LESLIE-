# Módulo producto del sistema de restaurante
# Contiene la clase Producto con constructor tradicional, properties y setters


class Producto:
    """
    Clase que representa un producto del restaurante.
    Implementa constructor tradicional __init__, decoradores @property y @setter
    para control de atributos.
    """
    
    def __init__(self, nombre, categoria, precio, disponible=True):
        """
        Constructor de la clase Producto.
        
        Args:
            nombre (str): Nombre del producto
            categoria (str): Categoría del producto
            precio (float): Precio del producto
            disponible (bool): Estado de disponibilidad (por defecto True)
        """
        self._nombre = None
        self._categoria = None
        self._precio = None
        self._disponible = disponible
        
        # Usar los setters para validación
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
    
    @property
    def nombre(self):
        """Obtiene el nombre del producto."""
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        """Establece el nombre del producto con validación."""
        if not valor or not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("El nombre del producto no puede estar vacío")
        self._nombre = valor.strip()
    
    @property
    def categoria(self):
        """Obtiene la categoría del producto."""
        return self._categoria
    
    @categoria.setter
    def categoria(self, valor):
        """Establece la categoría del producto con validación."""
        if not valor or not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("La categoría del producto no puede estar vacía")
        self._categoria = valor.strip()
    
    @property
    def precio(self):
        """Obtiene el precio del producto."""
        return self._precio
    
    @precio.setter
    def precio(self, valor):
        """Establece el precio del producto con validación."""
        try:
            precio_float = float(valor)
            if precio_float <= 0:
                raise ValueError("El precio debe ser mayor que cero")
            self._precio = precio_float
        except ValueError as e:
            if "El precio debe ser" in str(e):
                raise e
            raise ValueError("El precio debe ser un número válido mayor que cero")
    
    @property
    def disponible(self):
        """Obtiene el estado de disponibilidad del producto."""
        return self._disponible
    
    @disponible.setter
    def disponible(self, valor):
        """Establece el estado de disponibilidad del producto."""
        self._disponible = bool(valor)
    
    def mostrar_informacion(self):
        """
        Muestra la información del producto de forma legible.
        
        Returns:
            str: Información formateada del producto
        """
        estado = "Disponible" if self._disponible else "No disponible"
        return f"[{self._categoria.upper()}] {self._nombre} - ${self._precio:.2f} - {estado}"
    
    def __str__(self):
        """Retorna la representación en string del producto."""
        return self.mostrar_informacion()

