"""
Módulo que contiene la clase Biblioteca.

Esta clase administra los libros y usuarios registrados
dentro del sistema Biblioteca.
"""

from modelos.libro import Libro
from modelos.usuario import Usuario

class Biblioteca:
    """
    Administra los libros y usuarios del sistema.
    """

    def __init__(self):
        """
        Inicializa las colecciones del sistema.
        """

        self.libros = []
        self.usuarios = []

    # ==================================================
    # Métodos para gestionar libros
    # ==================================================

    def agregar_libro(self, libro: Libro):
        """
        Agrega un libro a la biblioteca.
        """

        self.libros.append(libro)

    def listar_libros(self):
        """
        Devuelve la lista de libros registrados.
        """

        return self.libros

    def buscar_libro(self, titulo: str):
        """
        Busca un libro por su título.
        """

        for libro in self.libros:

            if libro.titulo.lower() == titulo.lower():
                return libro

        return None

    # ==================================================
    # Métodos para gestionar usuarios
    # ==================================================

    def agregar_usuario(self, usuario: Usuario):
        """
        Agrega un usuario a la biblioteca.
        """

        self.usuarios.append(usuario)

    def listar_usuarios(self):
        """
        Devuelve la lista de usuarios registrados.
        """

        return self.usuarios

    def buscar_usuario(self, id_usuario: int):
        """
        Busca un usuario por su identificador.
        """

        for usuario in self.usuarios:

            if usuario.id_usuario == id_usuario:
                return usuario

        return None