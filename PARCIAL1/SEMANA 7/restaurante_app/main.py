# Archivo principal del sistema de restaurante
# Punto de arranque del programa con menú interactivo


from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def mostrar_menu():
    """Muestra el menú interactivo del sistema."""
    print("\n" + "=" * 50)
    print("        SISTEMA DE RESTAURANTE".center(50))
    print("=" * 50)
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("-" * 50)
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("-" * 50)
    print("7. Salir")
    print("=" * 50)


def registrar_producto(restaurante):
    """
    Registra un nuevo producto en el sistema.
    Solicita datos al usuario y crea un objeto Producto.
    """
    print("\n--- Registrar Nuevo Producto ---")
    try:
        nombre = input("Nombre del producto: ").strip()
        categoria = input("Categoría (ej: Bebidas, Alimentos, Postres): ").strip()
        precio = input("Precio del producto: ").strip()
        
        # Crear objeto Producto con validación del constructor y setters
        producto = Producto(nombre, categoria, precio)
        restaurante.registrar_producto(producto)
        print(f"✓ Producto '{producto.nombre}' registrado exitosamente.")
    except ValueError as e:
        print(f"✗ Error al registrar producto: {e}")


def listar_productos(restaurante):
    """Lists all registered products."""
    print("\n--- Listado de Productos ---")
    productos = restaurante.listar_productos()
    
    if not productos:
        print("No hay productos registrados.")
        return
    
    print(f"\nTotal de productos: {restaurante.cantidad_productos()}\n")
    for idx, producto in enumerate(productos, 1):
        print(f"{idx}. {producto.mostrar_informacion()}")


def buscar_producto(restaurante):
    """
    Busca un producto por nombre en el sistema.
    Muestra las opciones de búsqueda disponibles.
    """
    print("\n--- Buscar Producto ---")
    print("1. Buscar por nombre")
    print("2. Buscar por categoría")
    opcion = input("Seleccione opción: ").strip()
    
    if opcion == "1":
        nombre = input("Ingrese nombre del producto: ").strip()
        producto = restaurante.buscar_producto_por_nombre(nombre)
        if producto:
            print(f"\n✓ Producto encontrado:")
            print(f"  {producto.mostrar_informacion()}")
        else:
            print(f"\n✗ No se encontró un producto con el nombre '{nombre}'")
    
    elif opcion == "2":
        categoria = input("Ingrese categoría: ").strip()
        productos = restaurante.buscar_productos_por_categoria(categoria)
        if productos:
            print(f"\n✓ Se encontraron {len(productos)} producto(s) en la categoría '{categoria}':")
            for idx, producto in enumerate(productos, 1):
                print(f"  {idx}. {producto.mostrar_informacion()}")
        else:
            print(f"\n✗ No se encontraron productos en la categoría '{categoria}'")
    else:
        print("✗ Opción no válida")


def registrar_cliente(restaurante):
    """
    Registra un nuevo cliente en el sistema.
    Solicita datos al usuario y crea un objeto Cliente (dataclass).
    """
    print("\n--- Registrar Nuevo Cliente ---")
    try:
        id_cliente = input("ID del cliente: ").strip()
        nombre = input("Nombre del cliente: ").strip()
        correo = input("Correo del cliente: ").strip()
        
        # Validaciones básicas
        if not id_cliente or not nombre or not correo:
            raise ValueError("Los campos no pueden estar vacíos")
        
        # Crear objeto Cliente usando dataclass
        cliente = Cliente(id_cliente=id_cliente, nombre=nombre, correo=correo)
        restaurante.registrar_cliente(cliente)
        print(f"✓ Cliente '{cliente.nombre}' registrado exitosamente.")
    except ValueError as e:
        print(f"✗ Error al registrar cliente: {e}")


def listar_clientes(restaurante):
    """Lists all registered clients."""
    print("\n--- Listado de Clientes ---")
    clientes = restaurante.listar_clientes()
    
    if not clientes:
        print("No hay clientes registrados.")
        return
    
    print(f"\nTotal de clientes: {restaurante.cantidad_clientes()}\n")
    for idx, cliente in enumerate(clientes, 1):
        print(f"{idx}. {cliente.mostrar_informacion()}")


def buscar_cliente(restaurante):
    """
    Busca un cliente en el sistema.
    Muestra las opciones de búsqueda disponibles.
    """
    print("\n--- Buscar Cliente ---")
    print("1. Buscar por ID")
    print("2. Buscar por nombre")
    opcion = input("Seleccione opción: ").strip()
    
    if opcion == "1":
        id_cliente = input("Ingrese ID del cliente: ").strip()
        cliente = restaurante.buscar_cliente_por_id(id_cliente)
        if cliente:
            print(f"\n✓ Cliente encontrado:")
            print(f"  {cliente.mostrar_informacion()}")
        else:
            print(f"\n✗ No se encontró un cliente con el ID '{id_cliente}'")
    
    elif opcion == "2":
        nombre = input("Ingrese nombre del cliente: ").strip()
        clientes = restaurante.buscar_cliente_por_nombre(nombre)
        if clientes:
            print(f"\n✓ Se encontraron {len(clientes)} cliente(s):")
            for idx, cliente in enumerate(clientes, 1):
                print(f"  {idx}. {cliente.mostrar_informacion()}")
        else:
            print(f"\n✗ No se encontraron clientes con el nombre '{nombre}'")
    else:
        print("✗ Opción no válida")


def main():
    """
    Función principal que inicia el sistema de restaurante.
    Mantiene el menú interactivo en ejecución hasta que el usuario seleccione salir.
    """
    # Crear instancia del restaurante (objeto de servicio)
    restaurante = Restaurante("Restaurant Express")
    
    print("\n¡Bienvenido al Sistema de Restaurante!")
    print(f"Restaurante: {restaurante.nombre}")
    
    # Bucle principal del menú
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            registrar_producto(restaurante)
        
        elif opcion == "2":
            listar_productos(restaurante)
        
        elif opcion == "3":
            buscar_producto(restaurante)
        
        elif opcion == "4":
            registrar_cliente(restaurante)
        
        elif opcion == "5":
            listar_clientes(restaurante)
        
        elif opcion == "6":
            buscar_cliente(restaurante)
        
        elif opcion == "7":
            print("\n¡Gracias por usar el Sistema de Restaurante! ¡Hasta luego!")
            break
        
        else:
            print("✗ Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()

