class Restaurante:
    """
    Clase de servicio encargada de administrar los productos.
    """
    def __init__(self, nombre_restaurante):
        self.nombre_restaurante = nombre_restaurante
        self.lista_productos = []
        
    def agregar_producto(self, producto):
        """Agrega un objeto producto a la lista del restaurante."""
        self.lista_productos.append(producto)
        
    def mostrar_menu(self):
        """Recorre la lista de productos y demuestra el polimorfismo."""
        print(f"\n--- Menú de {self.nombre_restaurante} ---")
        for producto in self.lista_productos:
            # Aquí se evidencia el polimorfismo: se llama al mismo método, 
            # pero el comportamiento depende del tipo de objeto (Platillo o Bebida)
            print(producto.mostrar_informacion())
        print("----------------------------------\n")
