from __future__ import annotations

try:
    from modelos.producto import Producto
    from modelos.bebida import Bebida
    from modelos.cliente import Cliente
    from servicios.restaurante import Restaurante
except Exception:
    from restaurante_app.modelos.producto import Producto
    from restaurante_app.modelos.bebida import Bebida
    from restaurante_app.modelos.cliente import Cliente
    from restaurante_app.servicios.restaurante import Restaurante


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


def buscar_producto(serv: Restaurante) -> None:
    print("--- Buscar producto ---")
    codigo = solicitar_texto("Código a buscar: ")
    producto = serv.obtener_producto_por_codigo(codigo)
    if producto is None:
        print("No se encontró un producto con ese código.")
        return
    print(producto.mostrar_informacion())


def buscar_cliente(serv: Restaurante) -> None:
    print("--- Buscar cliente ---")
    identificacion = solicitar_texto("Identificación a buscar: ")
    cliente = serv.obtener_cliente_por_id(identificacion)
    if cliente is None:
        print("No se encontró un cliente con esa identificación.")
        return
    print(cliente.mostrar_informacion())


def eliminar_producto(serv: Restaurante) -> None:
    print("--- Eliminar producto ---")
    codigo = solicitar_texto("Código a eliminar: ")
    if serv.eliminar_producto(codigo):
        print(f"Producto {codigo} eliminado correctamente.")
    else:
        print(f"No se encontró el producto {codigo}.")


def eliminar_cliente(serv: Restaurante) -> None:
    print("--- Eliminar cliente ---")
    identificacion = solicitar_texto("Identificación a eliminar: ")
    if serv.eliminar_cliente(identificacion):
        print(f"Cliente {identificacion} eliminado correctamente.")
    else:
        print(f"No se encontró el cliente {identificacion}.")


def mostrar_menu() -> None:
    print("========================================")
    print("      SISTEMA DE RESTAURANTE JSON")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("6. Buscar producto")
    print("7. Buscar cliente")
    print("8. Eliminar producto")
    print("9. Eliminar cliente")
    print("----------------------------------------")
    print("10. Salir")


def main() -> None:
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
            buscar_producto(serv)
        elif opcion == "7":
            buscar_cliente(serv)
        elif opcion == "8":
            eliminar_producto(serv)
        elif opcion == "9":
            eliminar_cliente(serv)
        elif opcion == "10":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        print()


if __name__ == "__main__":
    main()
