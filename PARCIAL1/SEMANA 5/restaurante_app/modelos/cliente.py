# Clase Cliente - Representa un cliente del restaurante

class Cliente:
    """
    Clase que representa a un cliente del restaurante.
    Almacena información personal y de contacto del cliente.
    """

    def __init__(self, nombre, email, telefono, direccion=""):
        """
        Constructor de la clase Cliente.

        Args:
            nombre: Nombre completo del cliente
            email: Correo electrónico del cliente
            telefono: Número de teléfono del cliente
            direccion: Dirección del cliente (opcional)
        """
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.ordenes = []  # Lista para almacenar historial de órdenes

    def __str__(self):
        """
        Representación en texto del cliente.
        Retorna una cadena con el nombre y contacto del cliente.
        """
        return f"{self.nombre} ({self.email})"

    def obtener_informacion(self):
        """
        Método que retorna la información completa del cliente.
        """
        return {
            "nombre": self.nombre,
            "email": self.email,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "cantidad_ordenes": len(self.ordenes)
        }

    def agregar_orden(self, numero_orden):
        """
        Agrega un número de orden al historial del cliente.

        Args:
            numero_orden: Identificador de la orden
        """
        self.ordenes.append(numero_orden)

    def mostrar_detalles(self):
        """
        Muestra los detalles del cliente de forma formateada.
        """
        print(f"\n  Cliente: {self.nombre}")
        print(f"  Email: {self.email}")
        print(f"  Teléfono: {self.telefono}")
        if self.direccion:
            print(f"  Dirección: {self.direccion}")
        print(f"  Órdenes realizadas: {len(self.ordenes)}")


