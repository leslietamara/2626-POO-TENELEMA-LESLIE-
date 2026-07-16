# Módulo restaurante del sistema
# Contiene la clase Restaurante que administra productos y clientes


class Restaurante:
    """
    Clase de servicio que administra las listas de productos y clientes
    del restaurante. Implementa métodos para registrar, listar y buscar
    tanto productos como clientes.
    """
    
    def __init__(self, nombre):
        """
        Constructor de la clase Restaurante.
        
        Args:
            nombre (str): Nombre del restaurante
        """
        self.nombre = nombre
        self.productos = []
        self.clientes = []
    
    # ============= MÉTODOS PARA PRODUCTOS =============
    
    def registrar_producto(self, producto):
        """
        Registra un nuevo producto en el restaurante.
        
        Args:
            producto (Producto): Objeto de tipo Producto a registrar
        """
        self.productos.append(producto)
    
    def listar_productos(self):
        """
        Obtiene la lista de todos los productos registrados.
        
        Returns:
            list: Lista de productos
        """
        return self.productos
    
    def buscar_producto_por_nombre(self, nombre):
        """
        Busca un producto por su nombre.
        
        Args:
            nombre (str): Nombre del producto a buscar
        
        Returns:
            Producto o None: El producto encontrado o None si no existe
        """
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None
    
    def buscar_productos_por_categoria(self, categoria):
        """
        Busca todos los productos de una categoría específica.
        
        Args:
            categoria (str): Categoría a buscar
        
        Returns:
            list: Lista de productos en esa categoría
        """
        resultados = []
        for producto in self.productos:
            if producto.categoria.lower() == categoria.lower():
                resultados.append(producto)
        return resultados
    
    def cantidad_productos(self):
        """
        Retorna la cantidad de productos registrados.
        
        Returns:
            int: Número de productos
        """
        return len(self.productos)
    
    # ============= MÉTODOS PARA CLIENTES =============
    
    def registrar_cliente(self, cliente):
        """
        Registra un nuevo cliente en el restaurante.
        
        Args:
            cliente (Cliente): Objeto de tipo Cliente a registrar
        """
        # Validar que no exista un cliente con el mismo ID
        if self.buscar_cliente_por_id(cliente.id_cliente):
            raise ValueError(f"Ya existe un cliente con el ID {cliente.id_cliente}")
        self.clientes.append(cliente)
    
    def listar_clientes(self):
        """
        Obtiene la lista de todos los clientes registrados.
        
        Returns:
            list: Lista de clientes
        """
        return self.clientes
    
    def buscar_cliente_por_id(self, id_cliente):
        """
        Busca un cliente por su ID.
        
        Args:
            id_cliente (str): ID del cliente a buscar
        
        Returns:
            Cliente o None: El cliente encontrado o None si no existe
        """
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None
    
    def buscar_cliente_por_nombre(self, nombre):
        """
        Busca clientes por nombre (búsqueda parcial).
        
        Args:
            nombre (str): Nombre o parte del nombre a buscar
        
        Returns:
            list: Lista de clientes que coinciden
        """
        resultados = []
        for cliente in self.clientes:
            if nombre.lower() in cliente.nombre.lower():
                resultados.append(cliente)
        return resultados
    
    def cantidad_clientes(self):
        """
        Retorna la cantidad de clientes registrados.
        
        Returns:
            int: Número de clientes
        """
        return len(self.clientes)

