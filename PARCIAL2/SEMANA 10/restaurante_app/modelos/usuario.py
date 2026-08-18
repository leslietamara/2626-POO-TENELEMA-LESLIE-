from __future__ import annotations


class Usuario:
    """Representa a un usuario del sistema del restaurante."""

    def __init__(self, nombre: str, correo: str) -> None:
        self.nombre: str = self._validar_texto(nombre, "nombre")
        self.correo: str = self._validar_correo(correo)

    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        if not isinstance(valor, str):
            raise ValueError(f"El campo {campo} debe ser texto.")
        valor_limpio = valor.strip()
        if not valor_limpio:
            raise ValueError(f"El campo {campo} no puede estar vacío.")
        return valor_limpio

    @staticmethod
    def _validar_correo(correo: str) -> str:
        correo_limpio = Usuario._validar_texto(correo, "correo")
        if "@" not in correo_limpio or "." not in correo_limpio:
            raise ValueError("El correo debe contener un formato válido.")
        return correo_limpio

    def mostrar_informacion(self) -> str:
        return f"Nombre: {self.nombre} | Correo: {self.correo}"

    def to_dict(self) -> dict[str, str]:
        return {"nombre": self.nombre, "correo": self.correo}

    def __repr__(self) -> str:
        return f"Usuario(nombre={self.nombre!r}, correo={self.correo!r})"
