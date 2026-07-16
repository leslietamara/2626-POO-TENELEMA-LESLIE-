"""
Módulo que contiene la clase Libro.

Esta clase demuestra el uso del constructor tradicional (__init__),
@property y @setter.
"""


class Libro:
    """
    Representa un libro dentro del sistema Biblioteca.
    """

    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool = True):
        """
        Inicializa un nuevo libro.
        """

        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, nuevo_titulo: str):
        if not nuevo_titulo.strip():
            raise ValueError("El título no puede estar vacío.")

        self._titulo = nuevo_titulo

    @property
    def autor(self) -> str:
        return self._autor

    @autor.setter
    def autor(self, nuevo_autor: str):
        if not nuevo_autor.strip():
            raise ValueError("El autor no puede estar vacío.")

        self._autor = nuevo_autor

    @property
    def isbn(self) -> str:
        return self._isbn

    @isbn.setter
    def isbn(self, nuevo_isbn: str):
        if not nuevo_isbn.strip():
            raise ValueError("El ISBN no puede estar vacío.")

        self._isbn = nuevo_isbn

    @property
    def disponible(self) -> bool:
        return self._disponible

    @disponible.setter
    def disponible(self, estado: bool):
        self._disponible = estado

    def mostrar_informacion(self) -> str:
        """
        Devuelve la información del libro en formato legible.
        """

        estado = "Disponible" if self.disponible else "Prestado"

        return (
            f"Título: {self.titulo} | "
            f"Autor: {self.autor} | "
            f"ISBN: {self.isbn} | "
            f"Estado: {estado}"
        )