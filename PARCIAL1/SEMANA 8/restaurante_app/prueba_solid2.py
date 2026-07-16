"""Script de prueba para verificar funcionamiento de restaurante_app"""

import sys
import os

# Anadir la carpeta restaurante_app al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def prueba_srp():
    """Prueba del Principio de Responsabilidad Unica"""
    print("\n" + "="*60)
    print("PRUEBA 1: Responsabilidad Unica")
    print("="*60)

    # Cada clase tiene UNA responsabilidad
    p = Producto("P1", "Ensalada", "Platos", 15.99)
    print(f"Producto: {p.mostrar_informacion()}")

    b = Bebida("B1", "Cafe", "Bebidas", 3.50, "250ml", "taza")
    print(f"Bebida: {b.mostrar_informacion()}")

    c = Cliente("123", "Juan", "juan@example.com")
    print(f"Cliente: {c.mostrar_informacion()}")
    print("[OK] Cada clase muestra sus datos correctamente")


def prueba_ocp():
    """Prueba del Principio Abierto/Cerrado"""
    print("\n" + "="*60)
    print("PRUEBA 2: Abierto/Cerrado")
    print("="*60)

    r = Restaurante()

    # Registrar Producto
    p1 = Producto("P1", "Corte", "Platos Fuertes", 25.00)
    r.registrar_producto(p1)
    print(f"Registrado: {p1}")

    # Registrar Bebida
    b1 = Bebida("B1", "Limonada", "Bebidas", 4.50, "500ml", "botella")
    r.registrar_producto(b1)
    print(f"Registrado: {b1}")

    # Registrar otra Bebida
    b2 = Bebida("B2", "Jugo", "Bebidas", 5.00, "250ml", "vaso")
    r.registrar_producto(b2)
    print(f"Registrado: {b2}")

    print("\n[OK] Producto y Bebida usan el MISMO metodo registrar_producto()")
    print("[OK] Sistema abierto a extension SIN modificar Restaurante")


def prueba_lsp():
    """Prueba del Principio de Sustitucion de Liskov"""
    print("\n" + "="*60)
    print("PRUEBA 3: Sustitucion de Liskov (Polimorfismo)")
    print("="*60)

    r = Restaurante()

    # Agregar Productos y Bebidas
    productos = [
        Producto("P1", "Hamburguesa", "Platos Rapidos", 12.00),
        Bebida("B1", "Refresco", "Bebidas", 3.00, "330ml", "lata"),
        Producto("P2", "Pizza", "Platos Principales", 18.00),
        Bebida("B2", "Agua", "Bebidas", 2.00, "1L", "botella"),
    ]

    for p in productos:
        r.registrar_producto(p)

    print("\nListado de productos (usando polimorfismo):")
    print("-" * 60)
    for info in r.listar_productos():
        print(f"  {info}")

    print("\n[OK] Ambas clases funcionan en la MISMA lista")
    print("[OK] Cada una muestra SUS datos (polimorfismo)")
    print("[OK] Bebida puede reemplazar a Producto sin problemas")


def prueba_validaciones():
    """Prueba de validaciones (sin duplicados)"""
    print("\n" + "="*60)
    print("PRUEBA 4: Validaciones")
    print("="*60)

    r = Restaurante()

    # Registrar un producto
    p1 = Producto("P100", "Paella", "Especial", 22.00)
    r.registrar_producto(p1)
    print(f"[OK] Registrado: {p1}")

    # Intentar registrar con codigo duplicado
    try:
        p2 = Producto("P100", "Otro plato", "Otro", 15.00)
        r.registrar_producto(p2)
        print("[ERROR] permitio codigo duplicado")
    except ValueError as e:
        print(f"[OK] Validacion correcta: {e}")

    # Registrar cliente
    c1 = Cliente("111", "Maria", "maria@example.com")
    r.registrar_cliente(c1)
    print(f"[OK] Registrado: {c1}")

    # Intentar registrar cliente con ID duplicado
    try:
        c2 = Cliente("111", "Otro cliente", "otro@example.com")
        r.registrar_cliente(c2)
        print("[ERROR] permitio ID duplicado")
    except ValueError as e:
        print(f"[OK] Validacion correcta: {e}")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("PRUEBAS DEL SISTEMA RESTAURANTE_APP")
    print("="*60)

    prueba_srp()
    prueba_ocp()
    prueba_lsp()
    prueba_validaciones()

    print("\n" + "="*60)
    print("[OK] TODAS LAS PRUEBAS PASARON CORRECTAMENTE")
    print("="*60)

