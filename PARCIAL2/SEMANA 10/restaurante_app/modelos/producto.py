from __future__ import annotations


class Producto:
    """Representa un producto del restaurante."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo: str = self._validar_codigo(codigo)
        self.nombre: str = self._validar_texto(nombre, "nombre")
        self.categoria: str = self._validar_texto(categoria, "categoría")
        self.precio: float = self._validar_precio(precio)

    @staticmethod
    def _validar_codigo(codigo: str) -> str:
        if not isinstance(codigo, str):
            raise ValueError("El código del producto debe ser texto.")
        codigo_limpio = codigo.strip()
        if not codigo_limpio:
            raise ValueError("El código del producto no puede estar vacío.")
        return codigo_limpio.upper()

    @staticmethod
    def _validar_texto(valor: str, nombre_campo: str) -> str:
        if not isinstance(valor, str):
            raise ValueError(f"El campo {nombre_campo} debe ser texto.")
        valor_limpio = valor.strip()
        if not valor_limpio:
            raise ValueError(f"El campo {nombre_campo} no puede estar vacío.")
        return valor_limpio

    @staticmethod
    def _validar_precio(precio: float) -> float:
        try:
            precio_numero = float(precio)
        except (TypeError, ValueError) as exc:
            raise ValueError("El precio debe ser un número válido.") from exc
        if precio_numero <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        return precio_numero

    def to_dict(self) -> dict[str, str | float]:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Producto":
        if not isinstance(datos, dict):
            raise TypeError("El registro del producto debe ser un diccionario.")

        claves_requeridas = ("codigo", "nombre", "categoria", "precio")
        claves_faltantes = [clave for clave in claves_requeridas if clave not in datos]
        if claves_faltantes:
            raise KeyError(f"Faltan claves requeridas: {', '.join(claves_faltantes)}.")

        return cls(
            codigo=datos["codigo"],
            nombre=datos["nombre"],
            categoria=datos["categoria"],
            precio=datos["precio"],
        )

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: ${self.precio:.2f}"
        )

    def __repr__(self) -> str:
        return (
            f"Producto(codigo={self.codigo!r}, nombre={self.nombre!r}, "
            f"categoria={self.categoria!r}, precio={self.precio!r})"
        )
