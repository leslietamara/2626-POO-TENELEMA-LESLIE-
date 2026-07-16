"""
Módulo que contiene la clase Usuario.

Esta clase demuestra el uso de @dataclass como una forma moderna
de crear automáticamente el constructor.
"""

from dataclasses import dataclass


@dataclass
class Usuario:
    """
    Representa un usuario dentro del sistema Biblioteca.
    """

    nombre: str
    correo: str
    id_usuario: int

    def mostrar_informacion(self) -> str:
        """
        Devuelve la información del usuario en formato legible.
        """

        return (
            f"ID: {self.id_usuario} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )