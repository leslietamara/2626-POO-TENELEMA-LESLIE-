from __future__ import annotations
from .producto import Producto

class Bebida(Producto):
    """Clase que representa una bebida. Hereda de Producto."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, tamano: str, envase: str) -> None:
        super().__init__(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio)
        self.tamano: str = tamano  # p. ej. "330ml", "1L"
        self.envase: str = envase  # p. ej. "botella", "lata"

    def mostrar_informacion(self) -> str:
        base = super().mostrar_informacion()
        return f"{base} | Tamaño: {self.tamano} | Envase: {self.envase}"

    def __repr__(self) -> str:
        return f"Bebida(codigo={self.codigo!r}, nombre={self.nombre!r}, tamano={self.tamano!r})"
