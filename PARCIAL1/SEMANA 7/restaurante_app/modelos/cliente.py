# Módulo cliente del sistema de restaurante
# Contiene la clase Cliente implementada con decorador @dataclass

from dataclasses import dataclass


@dataclass
class Cliente:
    """
    Clase que representa un cliente del restaurante.
    Implementada utilizando el decorador @dataclass para simplificar
    la creación de objetos de datos.
    """
    id_cliente: str
    nombre: str
    correo: str
    
    def mostrar_informacion(self):
        """
        Muestra la información del cliente de forma legible.
        
        Returns:
            str: Información formateada del cliente
        """
        return f"[ID: {self.id_cliente}] {self.nombre} - {self.correo}"
    
    def __str__(self):
        """Retorna la representación en string del cliente."""
        return self.mostrar_informacion()

