# Clase Restaurante - Gestiona las operaciones principales del sistema

class Restaurante:
    """
    Clase que gestiona las operaciones principales del restaurante.
    Administra productos, clientes y órdenes del sistema.
    """

    def __init__(self, nombre, direccion, telefono):
        """
        Constructor de la clase Restaurante.

        Args:
            nombre: Nombre del restaurante
            direccion: Dirección del restaurante
            telefono: Teléfono de contacto del restaurante
        """
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos = []  # Lista de productos disponibles
        self.clientes = []   # Lista de clientes registrados
        self.ordenes = []    # Lista de órdenes realizadas
        self.contador_ordenes = 0  # Contador para generar IDs de órdenes

    def agregar_producto(self, producto):
        """
        Agrega un producto al menú del restaurante.

        Args:
            producto: Objeto de la clase Producto
        """
        self.productos.append(producto)
        print(f"✓ Producto '{producto.nombre}' agregado al menú.")

    def registrar_cliente(self, cliente):
        """
        Registra un cliente en el sistema del restaurante.

        Args:
            cliente: Objeto de la clase Cliente
        """
        self.clientes.append(cliente)
        print(f"✓ Cliente '{cliente.nombre}' registrado en el sistema.")

    def crear_orden(self, cliente, productos_pedidos):
        """
        Crea una nueva orden para un cliente.

        Args:
            cliente: Objeto de la clase Cliente
            productos_pedidos: Lista de productos ordenados

        Returns:
            número de orden
        """
        self.contador_ordenes += 1
        numero_orden = self.contador_ordenes

        total = sum(producto.precio for producto in productos_pedidos)

        orden = {
            "numero": numero_orden,
            "cliente": cliente.nombre,
            "productos": [p.nombre for p in productos_pedidos],
            "total": total
        }

        self.ordenes.append(orden)
        cliente.agregar_orden(numero_orden)

        print(f"✓ Orden #{numero_orden} creada para {cliente.nombre}. Total: ${total:.2f}")
        return numero_orden

    def mostrar_menu(self):
        """
        Muestra todos los productos disponibles en el menú.
        """
        print("\n" + "="*70)
        print(f"{'MENÚ DEL RESTAURANTE':^70}")
        print(f"{self.nombre}".center(70))
        print("="*70)

        if not self.productos:
            print("No hay productos disponibles en el menú.")
        else:
            # Agrupar productos por categoría
            categorias = {}
            for producto in self.productos:
                if producto.categoria not in categorias:
                    categorias[producto.categoria] = []
                categorias[producto.categoria].append(producto)

            # Mostrar por categoría
            for categoria in categorias:
                print(f"\n--- {categoria.upper()} ---")
                for producto in categorias[categoria]:
                    print(f"  • {producto}")

        print("="*70)

    def mostrar_clientes(self):
        """
        Muestra la información de todos los clientes registrados.
        """
        print("\n" + "="*70)
        print(f"{'CLIENTES REGISTRADOS':^70}")
        print("="*70)

        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            for cliente in self.clientes:
                cliente.mostrar_detalles()

        print("="*70)

    def mostrar_ordenes(self):
        """
        Muestra el historial de todas las órdenes realizadas.
        """
        print("\n" + "="*70)
        print(f"{'HISTORIAL DE ÓRDENES':^70}")
        print("="*70)

        if not self.ordenes:
            print("No hay órdenes registradas.")
        else:
            for orden in self.ordenes:
                print(f"\nOrden #{orden['numero']}")
                print(f"  Cliente: {orden['cliente']}")
                print(f"  Productos: {', '.join(orden['productos'])}")
                print(f"  Total: ${orden['total']:.2f}")

        print("="*70)

    def mostrar_informacion_restaurante(self):
        """
        Muestra la información general del restaurante.
        """
        print("\n" + "="*70)
        print(f"{'INFORMACIÓN DEL RESTAURANTE':^70}")
        print("="*70)
        print(f"Nombre: {self.nombre}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")
        print(f"Productos en menú: {len(self.productos)}")
        print(f"Clientes registrados: {len(self.clientes)}")
        print(f"Órdenes realizadas: {len(self.ordenes)}")
        print("="*70)

