# Punto de arranque del sistema de gestión de restaurante
# Importar las clases necesarias desde los módulos

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def main():
    """
    Función principal que ejecuta la demostración del sistema.
    Crea objetos, los agrega al restaurante y muestra la información.
    """

    # Crear una instancia del restaurante
    print("\n" + "="*70)
    print("INICIALIZANDO SISTEMA DE GESTIÓN DE RESTAURANTE")
    print("="*70 + "\n")

    restaurante = Restaurante(
        nombre="La Buena Mesa",
        direccion="Calle Principal 123, Centro",
        telefono="+34 912345678"
    )

    # ===== CREAR PRODUCTOS =====
    print("\n[1] AGREGANDO PRODUCTOS AL MENÚ...\n")

    # Entradas
    entrada1 = Producto(
        nombre="Tabla de Quesos y Embutidos",
        descripcion="Selección variada de quesos y jamones ibéricos",
        precio=15.50,
        categoria="Entrada"
    )

    entrada2 = Producto(
        nombre="Camarones al Ajillo",
        descripcion="Camarones frescos al ajillo y limón",
        precio=12.00,
        categoria="Entrada"
    )

    # Platos principales
    plato1 = Producto(
        nombre="Filete de Salmón a la Mantequilla",
        descripcion="Salmón fresco con salsa de mantequilla y limón",
        precio=22.50,
        categoria="Plato Principal"
    )

    plato2 = Producto(
        nombre="Pechuga de Pollo Rellena",
        descripcion="Pollo relleno de jamón y queso, acompañado de ensalada",
        precio=18.75,
        categoria="Plato Principal"
    )

    # Postres
    postre1 = Producto(
        nombre="Tiramisú Casero",
        descripcion="Tradicional tiramisú italiano preparado diariamente",
        precio=8.50,
        categoria="Postre"
    )

    postre2 = Producto(
        nombre="Flan de Huevo",
        descripcion="Flan cremoso con caramelo",
        precio=7.00,
        categoria="Postre"
    )

    # Bebidas
    bebida1 = Producto(
        nombre="Vino Tinto Reserva",
        descripcion="Vino de la región, cosecha 2018",
        precio=25.00,
        categoria="Bebida"
    )

    bebida2 = Producto(
        nombre="Agua Mineral",
        descripcion="Agua mineral sin gas",
        precio=2.50,
        categoria="Bebida"
    )

    # Agregar todos los productos al restaurante
    productos = [entrada1, entrada2, plato1, plato2, postre1, postre2, bebida1, bebida2]
    for producto in productos:
        restaurante.agregar_producto(producto)

    # ===== CREAR CLIENTES =====
    print("\n[2] REGISTRANDO CLIENTES...\n")

    cliente1 = Cliente(
        nombre="María García López",
        email="maria.garcia@email.com",
        telefono="+34 612345678",
        direccion="Av. España 45, Madrid"
    )

    cliente2 = Cliente(
        nombre="Juan Rodríguez Pérez",
        email="juan.rodriguez@email.com",
        telefono="+34 623456789",
        direccion="Calle Mayor 12, Barcelona"
    )

    cliente3 = Cliente(
        nombre="Ana Martínez López",
        email="ana.martinez@email.com",
        telefono="+34 634567890",
        direccion="Plaza Central 7, Valencia"
    )

    # Registrar clientes en el restaurante
    clientes = [cliente1, cliente2, cliente3]
    for cliente in clientes:
        restaurante.registrar_cliente(cliente)

    # ===== CREAR ÓRDENES =====
    print("\n[3] CREANDO ÓRDENES...\n")

    # Orden 1: María pide Entrada + Plato + Postre + Bebida
    orden1_productos = [entrada1, plato1, postre1, bebida1]
    restaurante.crear_orden(cliente1, orden1_productos)

    # Orden 2: Juan pide Entrada + Plato + Postre
    orden2_productos = [entrada2, plato2, postre2]
    restaurante.crear_orden(cliente2, orden2_productos)

    # Orden 3: Ana pide Plato + Bebida
    orden3_productos = [plato1, bebida2]
    restaurante.crear_orden(cliente3, orden3_productos)

    # ===== MOSTRAR INFORMACIÓN =====
    print("\n[4] MOSTRANDO INFORMACIÓN DEL SISTEMA...\n")

    # Mostrar información del restaurante
    restaurante.mostrar_informacion_restaurante()

    # Mostrar menú
    restaurante.mostrar_menu()

    # Mostrar clientes
    restaurante.mostrar_clientes()

    # Mostrar órdenes
    restaurante.mostrar_ordenes()

    # Mostrar detalles de un producto específico
    print("\n" + "="*70)
    print("DETALLES DE UN PRODUCTO ESPECÍFICO")
    print("="*70)
    plato1.mostrar_detalles()
    print("="*70)

    print("\n" + "="*70)
    print("SISTEMA EJECUTADO CORRECTAMENTE")
    print("="*70 + "\n")

if __name__ == "__main__":
    # Ejecutar la función principal
    main()


