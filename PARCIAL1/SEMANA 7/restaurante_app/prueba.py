# Script de prueba del sistema de restaurante
# Automatiza las pruebas del menú interactivo

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def prueba_completa():
    """Ejecuta pruebas automáticas del sistema."""
    print("=" * 60)
    print("PRUEBAS DEL SISTEMA DE RESTAURANTE".center(60))
    print("=" * 60)

    # Crear instancia del restaurante
    restaurante = Restaurante("Restaurant Express")
    print(f"\n✓ Restaurante '{restaurante.nombre}' creado")

    # ============= PRUEBAS DE PRODUCTOS =============
    print("\n" + "-" * 60)
    print("PRUEBAS DE PRODUCTOS".center(60))
    print("-" * 60)

    # Prueba 1: Crear productos válidos
    print("\n1. Creando productos válidos...")
    try:
        p1 = Producto("Pizza Margherita", "Alimentos", "15.99")
        restaurante.registrar_producto(p1)
        print(f"   ✓ {p1.mostrar_informacion()}")

        p2 = Producto("Café Espresso", "Bebidas", "3.50")
        restaurante.registrar_producto(p2)
        print(f"   ✓ {p2.mostrar_informacion()}")

        p3 = Producto("Tiramisú", "Postres", "8.99")
        restaurante.registrar_producto(p3)
        print(f"   ✓ {p3.mostrar_informacion()}")
    except Exception as e:
        print(f"   ✗ Error: {e}")

    # Prueba 2: Intentar crear producto con nombre vacío
    print("\n2. Intentando crear producto con nombre vacío...")
    try:
        p_invalido = Producto("", "Alimentos", "10.00")
        print("   ✗ Debería haber lanzado una excepción")
    except ValueError as e:
        print(f"   ✓ Validación correcta: {e}")

    # Prueba 3: Intentar crear producto con precio negativo
    print("\n3. Intentando crear producto con precio negativo...")
    try:
        p_invalido = Producto("Producto", "Alimentos", "-5.00")
        print("   ✗ Debería haber lanzado una excepción")
    except ValueError as e:
        print(f"   ✓ Validación correcta: {e}")

    # Prueba 4: Listar productos
    print("\n4. Listando todos los productos...")
    productos = restaurante.listar_productos()
    print(f"   Total: {restaurante.cantidad_productos()} productos")
    for idx, producto in enumerate(productos, 1):
        print(f"   {idx}. {producto.mostrar_informacion()}")

    # Prueba 5: Buscar producto por nombre
    print("\n5. Buscando producto por nombre 'Café Espresso'...")
    producto = restaurante.buscar_producto_por_nombre("Café Espresso")
    if producto:
        print(f"   ✓ Encontrado: {producto.mostrar_informacion()}")
    else:
        print("   ✗ No encontrado")

    # Prueba 6: Buscar productos por categoría
    print("\n6. Buscando productos en la categoría 'Alimentos'...")
    productos = restaurante.buscar_productos_por_categoria("Alimentos")
    print(f"   ✓ Se encontraron {len(productos)} producto(s)")
    for idx, producto in enumerate(productos, 1):
        print(f"   {idx}. {producto.mostrar_informacion()}")

    # Prueba 7: Modificar atributo usando setter
    print("\n7. Modificando precio de un producto...")
    try:
        p1.precio = 16.99
        print(f"   ✓ Nuevo precio: ${p1.precio:.2f}")
    except Exception as e:
        print(f"   ✗ Error: {e}")

    # Prueba 8: Cambiar disponibilidad
    print("\n8. Cambiar disponibilidad de producto...")
    p1.disponible = False
    print(f"   ✓ {p1.mostrar_informacion()}")

    # ============= PRUEBAS DE CLIENTES =============
    print("\n" + "-" * 60)
    print("PRUEBAS DE CLIENTES (@dataclass)".center(60))
    print("-" * 60)

    # Prueba 9: Crear clientes
    print("\n9. Creando clientes...")
    try:
        c1 = Cliente(id_cliente="CLI001", nombre="Juan Pérez", correo="juan@example.com")
        restaurante.registrar_cliente(c1)
        print(f"   ✓ {c1.mostrar_informacion()}")

        c2 = Cliente(id_cliente="CLI002", nombre="María García", correo="maria@example.com")
        restaurante.registrar_cliente(c2)
        print(f"   ✓ {c2.mostrar_informacion()}")

        c3 = Cliente(id_cliente="CLI003", nombre="Carlos López", correo="carlos@example.com")
        restaurante.registrar_cliente(c3)
        print(f"   ✓ {c3.mostrar_informacion()}")
    except Exception as e:
        print(f"   ✗ Error: {e}")

    # Prueba 10: Intentar registrar cliente con ID duplicado
    print("\n10. Intentando registrar cliente con ID duplicado...")
    try:
        c_duplicado = Cliente(id_cliente="CLI001", nombre="Otro", correo="otro@example.com")
        restaurante.registrar_cliente(c_duplicado)
        print("   ✗ Debería haber lanzado una excepción")
    except ValueError as e:
        print(f"   ✓ Validación correcta: {e}")

    # Prueba 11: Listar clientes
    print("\n11. Listando todos los clientes...")
    clientes = restaurante.listar_clientes()
    print(f"   Total: {restaurante.cantidad_clientes()} clientes")
    for idx, cliente in enumerate(clientes, 1):
        print(f"   {idx}. {cliente.mostrar_informacion()}")

    # Prueba 12: Buscar cliente por ID
    print("\n12. Buscando cliente por ID 'CLI002'...")
    cliente = restaurante.buscar_cliente_por_id("CLI002")
    if cliente:
        print(f"   ✓ Encontrado: {cliente.mostrar_informacion()}")
    else:
        print("   ✗ No encontrado")

    # Prueba 13: Buscar clientes por nombre
    print("\n13. Buscando clientes con 'García' en el nombre...")
    clientes = restaurante.buscar_cliente_por_nombre("García")
    print(f"   ✓ Se encontraron {len(clientes)} cliente(s)")
    for idx, cliente in enumerate(clientes, 1):
        print(f"   {idx}. {cliente.mostrar_informacion()}")

    # ============= RESUMEN FINAL =============
    print("\n" + "=" * 60)
    print("RESUMEN FINAL".center(60))
    print("=" * 60)
    print(f"\nTotal de productos registrados: {restaurante.cantidad_productos()}")
    print(f"Total de clientes registrados: {restaurante.cantidad_clientes()}")
    print("\n✓ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
    print("=" * 60)


if __name__ == "__main__":
    prueba_completa()

