from __future__ import annotations

from .producto import Producto


class Bebida(Producto):
    """Clase que representa una bebida. Hereda de Producto."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, tamano: str, envase: str) -> None:
        super().__init__(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio)
        self.tamano: str = tamano
        self.envase: str = envase

    def mostrar_informacion(self) -> str:
        base = super().mostrar_informacion()
        return f"{base} | Tamaño: {self.tamano} | Envase: {self.envase}"

    def to_dict(self) -> dict:
        datos = super().to_dict()
        datos["tamano"] = self.tamano
        datos["envase"] = self.envase
        return datos

    @classmethod
    def from_dict(cls, datos: dict) -> "Bebida":
        return cls(
            codigo=str(datos["codigo"]),
            nombre=str(datos["nombre"]),
            categoria=str(datos["categoria"]),
            precio=float(datos["precio"]),
            tamano=str(datos["tamano"]),
            envase=str(datos["envase"]),
        )

    def __repr__(self) -> str:
        return f"Bebida(codigo={self.codigo!r}, nombre={self.nombre!r}, tamano={self.tamano!r})"
