from __future__ import annotations
# So the module can be run both as a script (inside restaurante_app/) or as a package
try:
    # when executed as `python main.py` with cwd=restaurante_app
    from modelos.producto import Producto
    from modelos.bebida import Bebida
    from modelos.cliente import Cliente
    from servicios.restaurante import Restaurante
    from explicaciones import (
        mostrar_intro_solid,
        mostrar_menu_solid,
        mostrar_ejemplo_codigo,
    )
except Exception:
    # when executed from project root or as a package
    from restaurante_app.modelos.producto import Producto
    from restaurante_app.modelos.bebida import Bebida
    from restaurante_app.modelos.cliente import Cliente
    from restaurante_app.servicios.restaurante import Restaurante
    from restaurante_app.explicaciones import (
        mostrar_intro_solid,
        mostrar_menu_solid,
        mostrar_ejemplo_codigo,
    )


def solicitar_texto(prompt: str) -> str:
    return input(prompt).strip()


def solicitar_precio(prompt: str) -> float:
    while True:
        valor = input(prompt).strip()
        try:
            precio = float(valor)
            if precio < 0:
                raise ValueError()
            return precio
        except ValueError:
            print("Precio inválido. Ingrese un número positivo (p. ej. 12.50).")


def registrar_producto(serv: Restaurante) -> None:
    print("--- Registrar producto ---")
    codigo = solicitar_texto("Código: ")
    nombre = solicitar_texto("Nombre: ")
    categoria = solicitar_texto("Categoría: ")
    precio = solicitar_precio("Precio: ")
    producto = Producto(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio)
    try:
        serv.registrar_producto(producto)
        print("Producto registrado correctamente.")
    except ValueError as e:
        print(f"Error: {e}")


def registrar_bebida(serv: Restaurante) -> None:
    print("--- Registrar bebida ---")
    codigo = solicitar_texto("Código: ")
    nombre = solicitar_texto("Nombre: ")
    categoria = solicitar_texto("Categoría: ")
    precio = solicitar_precio("Precio: ")
    tamano = solicitar_texto("Tamaño (p. ej. 330ml, 1L): ")
    envase = solicitar_texto("Envase (p. ej. botella, lata): ")
    bebida = Bebida(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio, tamano=tamano, envase=envase)
    try:
        serv.registrar_producto(bebida)
        print("Bebida registrada correctamente.")
    except ValueError as e:
        print(f"Error: {e}")


def registrar_cliente(serv: Restaurante) -> None:
    print("--- Registrar cliente ---")
    identificacion = solicitar_texto("Identificación: ")
    nombre = solicitar_texto("Nombre: ")
    correo = solicitar_texto("Correo: ")
    cliente = Cliente(identificacion=identificacion, nombre=nombre, correo=correo)
    try:
        serv.registrar_cliente(cliente)
        print("Cliente registrado correctamente.")
    except ValueError as e:
        print(f"Error: {e}")


def listar_productos(serv: Restaurante) -> None:
    print("--- Lista de productos ---")
    productos = serv.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    for info in productos:
        print(info)


def listar_clientes(serv: Restaurante) -> None:
    print("--- Lista de clientes ---")
    clientes = serv.listar_clientes()
    if not clientes:
        print("No hay clientes registrados.")
        return
    for info in clientes:
        print(info)


def mostrar_menu() -> None:
    print("========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Aprender sobre SOLID")
    print("----------------------------------------")
    print("7. Salir")


def main() -> None:
    mostrar_intro_solid()  # Mostrar intro SOLID
    serv = Restaurante()
    while True:
        mostrar_menu()
        opcion = solicitar_texto("Seleccione una opción: ")
        if opcion == "1":
            registrar_producto(serv)
        elif opcion == "2":
            registrar_bebida(serv)
        elif opcion == "3":
            registrar_cliente(serv)
        elif opcion == "4":
            listar_productos(serv)
        elif opcion == "5":
            listar_clientes(serv)
        elif opcion == "6":
            mostrar_menu_solid()
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        print()


if __name__ == "__main__":
    main()

