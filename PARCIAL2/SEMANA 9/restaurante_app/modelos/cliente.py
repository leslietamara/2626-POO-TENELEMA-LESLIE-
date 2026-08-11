from __future__ import annotations


class Cliente:
    """Representa a un cliente registrado."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    def mostrar_informacion(self) -> str:
        return f"ID: {self.identificacion} | Nombre: {self.nombre} | Correo: {self.correo}"

    def to_dict(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Cliente":
        return cls(
            identificacion=str(datos["identificacion"]),
            nombre=str(datos["nombre"]),
            correo=str(datos["correo"]),
        )

    def __repr__(self) -> str:
        return f"Cliente(id={self.identificacion!r}, nombre={self.nombre!r})"
