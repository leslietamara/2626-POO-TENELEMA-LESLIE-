"""
Programa principal del sistema Biblioteca.

Este módulo permite interactuar con el usuario mediante
un menú de consola para gestionar libros y usuarios.
"""

from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca import Biblioteca


def mostrar_menu():
    """
    Muestra el menú principal del sistema.
    """

    print("\n" + "=" * 40)
    print("      SISTEMA DE BIBLIOTECA")
    print("=" * 40)
    print("1. Registrar libro")
    print("2. Listar libros")
    print("3. Buscar libro")
    print("-" * 40)
    print("4. Registrar usuario")
    print("5. Listar usuarios")
    print("6. Buscar usuario")
    print("-" * 40)
    print("7. Salir")


def registrar_libro(biblioteca):
    """
    Registra un nuevo libro.
    """

    print("\n--- Registrar libro ---")

    titulo = input("Título: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")

    libro = Libro(titulo, autor, isbn)

    biblioteca.agregar_libro(libro)

    print("\nLibro registrado correctamente.")


def listar_libros(biblioteca):
    """
    Muestra todos los libros registrados.
    """

    print("\n--- Lista de libros ---")

    libros = biblioteca.listar_libros()

    if libros:

        for libro in libros:
            print(libro.mostrar_informacion())

    else:
        print("No existen libros registrados.")


def buscar_libro(biblioteca):
    """
    Busca un libro por su título.
    """

    print("\n--- Buscar libro ---")

    titulo = input("Ingrese el título del libro: ")

    libro = biblioteca.buscar_libro(titulo)

    if libro:
        print("\nLibro encontrado:")
        print(libro.mostrar_informacion())
    else:
        print("\nNo se encontró el libro.")


def registrar_usuario(biblioteca):
    """
    Registra un nuevo usuario.
    """

    print("\n--- Registrar usuario ---")

    nombre = input("Nombre: ")
    correo = input("Correo electrónico: ")
    id_usuario = int(input("ID del usuario: "))

    usuario = Usuario(nombre, correo, id_usuario)

    biblioteca.agregar_usuario(usuario)

    print("\nUsuario registrado correctamente.")


def listar_usuarios(biblioteca):
    """
    Muestra todos los usuarios registrados.
    """

    print("\n--- Lista de usuarios ---")

    usuarios = biblioteca.listar_usuarios()

    if usuarios:

        for usuario in usuarios:
            print(usuario.mostrar_informacion())

    else:
        print("No existen usuarios registrados.")


def buscar_usuario(biblioteca):
    """
    Busca un usuario por su identificador.
    """

    print("\n--- Buscar usuario ---")

    id_usuario = int(input("Ingrese el ID del usuario: "))

    usuario = biblioteca.buscar_usuario(id_usuario)

    if usuario:
        print("\nUsuario encontrado:")
        print(usuario.mostrar_informacion())
    else:
        print("\nNo se encontró el usuario.")


def main():
    """
    Ejecuta el sistema Biblioteca.
    """

    biblioteca = Biblioteca()

    while True:

        mostrar_menu()

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_libro(biblioteca)

        elif opcion == "2":
            listar_libros(biblioteca)

        elif opcion == "3":
            buscar_libro(biblioteca)

        elif opcion == "4":
            registrar_usuario(biblioteca)

        elif opcion == "5":
            listar_usuarios(biblioteca)

        elif opcion == "6":
            buscar_usuario(biblioteca)

        elif opcion == "7":
            print("\nGracias por utilizar el sistema Biblioteca.")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()