from __future__ import annotations

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante


def solicitar_texto(prompt: str) -> str:
    return input(prompt).strip()


def solicitar_precio(prompt: str) -> float:
    while True:
        valor = input(prompt).strip()
        try:
            precio = float(valor)
            if precio <= 0:
                raise ValueError
            return precio
        except ValueError:
            print("El precio debe ser un número positivo.")


def cargar_productos_iniciales(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    productos = archivo_servicio.cargar_productos()
    restaurante.cargar_productos(productos)
    if productos:
        print(f"Se cargaron {len(productos)} productos desde el archivo JSON.")
    else:
        print("No existen productos guardados. El archivo está vacío o aún no existe.")


def registrar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    print("--- Registrar producto ---")
    codigo = solicitar_texto("Código: ")
    nombre = solicitar_texto("Nombre: ")
    categoria = solicitar_texto("Categoría: ")
    precio = solicitar_precio("Precio: ")

    producto = Producto(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio)
    try:
        restaurante.registrar_producto(producto)
        archivo_servicio.guardar_productos(restaurante.listar_productos())
        print("Producto registrado correctamente.")
    except ValueError as error:
        print(f"Error: {error}")
    except PermissionError as error:
        print(f"Error: {error}")


def listar_productos(restaurante: Restaurante) -> None:
    print("--- Listado de productos ---")
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    for producto in productos:
        print(producto.mostrar_informacion())


def buscar_producto(restaurante: Restaurante) -> None:
    print("--- Buscar producto ---")
    codigo = solicitar_texto("Código a buscar: ")
    producto = restaurante.obtener_producto_por_codigo(codigo)
    if producto is None:
        print("No se encontró un producto con ese código.")
        return
    print(producto.mostrar_informacion())


def actualizar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    print("--- Actualizar producto ---")
    codigo = solicitar_texto("Código del producto a actualizar: ")
    nombre = solicitar_texto("Nuevo nombre (deje vacío para mantenerlo): ")
    categoria = solicitar_texto("Nueva categoría (deje vacío para mantenerla): ")
    precio_str = solicitar_texto("Nuevo precio (deje vacío para mantenerlo): ")

    precio: float | None = None
    if precio_str:
        try:
            precio = float(precio_str)
            if precio <= 0:
                raise ValueError
        except ValueError:
            print("El precio debe ser un número positivo.")
            return

    try:
        restaurante.actualizar_producto(
            codigo=codigo,
            nombre=nombre or None,
            categoria=categoria or None,
            precio=precio,
        )
        archivo_servicio.guardar_productos(restaurante.listar_productos())
        print("Producto actualizado correctamente.")
    except ValueError as error:
        print(f"Error: {error}")
    except PermissionError as error:
        print(f"Error: {error}")


def eliminar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    print("--- Eliminar producto ---")
    codigo = solicitar_texto("Código a eliminar: ")
    try:
        if not restaurante.eliminar_producto(codigo):
            print(f"No existe el producto con código '{codigo}'.")
            return
        archivo_servicio.guardar_productos(restaurante.listar_productos())
        print(f"Producto '{codigo}' eliminado correctamente.")
    except PermissionError as error:
        print(f"Error: {error}")


def registrar_usuario(restaurante: Restaurante) -> None:
    print("--- Registrar usuario ---")
    nombre = solicitar_texto("Nombre: ")
    correo = solicitar_texto("Correo: ")
    usuario = Usuario(nombre=nombre, correo=correo)
    try:
        restaurante.registrar_usuario(usuario)
        print("Usuario registrado correctamente.")
    except ValueError as error:
        print(f"Error: {error}")


def listar_usuarios(restaurante: Restaurante) -> None:
    print("--- Listado de usuarios ---")
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for usuario in usuarios:
        print(usuario.mostrar_informacion())


def mostrar_menu() -> None:
    print("=======================================")
    print("       RESTAURANTE APP - SEMANA 10")
    print("=======================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Registrar usuario")
    print("7. Listar usuarios")
    print("8. Salir")
    print("=======================================")


def main() -> None:
    archivo_servicio = ArchivoServicio()
    restaurante = Restaurante()
    cargar_productos_iniciales(restaurante, archivo_servicio)

    while True:
        mostrar_menu()
        opcion = solicitar_texto("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto(restaurante, archivo_servicio)
        elif opcion == "2":
            listar_productos(restaurante)
        elif opcion == "3":
            buscar_producto(restaurante)
        elif opcion == "4":
            actualizar_producto(restaurante, archivo_servicio)
        elif opcion == "5":
            eliminar_producto(restaurante, archivo_servicio)
        elif opcion == "6":
            registrar_usuario(restaurante)
        elif opcion == "7":
            listar_usuarios(restaurante)
        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

        print()


if __name__ == "__main__":
    main()
