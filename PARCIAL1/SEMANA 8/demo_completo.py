"""
Script de demostración interactiva: Muestra el flujo completo del restaurante_app
"""

import subprocess
import sys

def mostrar_separador():
    print("\n" + "=" * 80)

def demostrar_pruebas():
    """Ejecuta las pruebas automáticas y muestra los resultados."""

    mostrar_separador()
    print("DEMOSTRACION 1: EJECUTANDO PRUEBAS AUTOMATIZADAS")
    mostrar_separador()

    proceso = subprocess.run(
        [sys.executable, "prueba_solid.py"],
        cwd=r"C:\Users\TAMARA\PycharmProjects\2626-POO-TENELEMA-LESLIE-\PARCIAL1\SEMANA 8\restaurante_app",
        capture_output=True,
        text=True,
        timeout=15
    )

    print(proceso.stdout)
    if proceso.stderr:
        print("ERRORES:", proceso.stderr)


def demostrar_menu():
    """Simula una sesión interactiva del menú."""

    mostrar_separador()
    print("DEMOSTRACION 2: SIMULACION DE SESION INTERACTIVA")
    mostrar_separador()

    # Simulamos las entradas:
    # 1 (registrar producto), 2 (registrar bebida), 4 (listar), 7 (salir)
    entrada_simulada = "1\ntest_prod\nPizza Margherita\nPlatos Principales\n25.50\n2\ntest_beb\nRefresco\nBebidas\n5.00\n500ml\nbotella\n4\n5\n7\n"

    print("\nSimulando interaccion de usuario:")
    print("1. Registrar producto: Pizza Margherita")
    print("2. Registrar bebida: Refresco 500ml en botella")
    print("3. Listar productos")
    print("4. Salir")
    print("\n" + "-" * 80 + "\n")

    proceso = subprocess.Popen(
        [sys.executable, "main.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=r"C:\Users\TAMARA\PycharmProjects\2626-POO-TENELEMA-LESLIE-\PARCIAL1\SEMANA 8\restaurante_app"
    )

    try:
        stdout, stderr = proceso.communicate(input=entrada_simulada, timeout=10)

        if stderr:
            print("ERRORES EN STDERR:")
            print(stderr)

        # Mostrar la salida (primeras y ultimas lineas)
        lineas = stdout.split('\n')
        print("SALIDA DEL PROGRAMA (fragmentos clave):")
        print("\n".join(lineas[:15]))  # Primeras 15 líneas
        print("\n... [salida intermedia] ...\n")
        print("\n".join(lineas[-10:]))  # Últimas 10 líneas

    except subprocess.TimeoutExpired:
        proceso.kill()
        print("TIMEOUT: El programa tardó demasiado en responder")


def resumen_funcionalidades():
    """Muestra un resumen de las funcionalidades."""

    mostrar_separador()
    print("FUNCIONALIDADES IMPLEMENTADAS")
    mostrar_separador()

    print("""
SISTEMA RESTAURANTE_APP v1.0 - CON EDUCACION SOLID INTEGRADA

CARACTERISTICAS:
================

1. GESTION DE PRODUCTOS Y BEBIDAS
   - Registrar productos (código, nombre, categoría, precio)
   - Registrar bebidas (incluye tamaño y envase)
   - Listar productos con polimorfismo (cada tipo muestra sus datos)
   - Validación: No permite códigos duplicados

2. GESTION DE CLIENTES
   - Registrar clientes (ID, nombre, correo)
   - Listar clientes registrados
   - Validación: No permite IDs duplicados

3. EDUCACION INTERACTIVA SOBRE SOLID
   - Opción 6 en el menú principal
   - Explicación de SRP (Responsabilidad Única)
   - Explicación de OCP (Abierto/Cerrado)
   - Explicación de LSP (Sustitución de Liskov)
   - Resumen combinado de los 3 principios
   - Todas las explicaciones contextualizadas en restaurante_app

4. ARQUITECTURA MODULAR
   - modelos/: Clases de datos (Producto, Bebida, Cliente)
   - servicios/: Lógica de negocio (Restaurante)
   - main.py: Interacción con usuario
   - explicaciones.py: Módulo educativo

5. PRINCIPIOS SOLID APLICADOS
   ✓ SRP: Cada clase tiene UNA responsabilidad
   ✓ OCP: Bebida extiende Producto sin modificar Restaurante
   ✓ LSP: Bebida es intercambiable con Producto (polimorfismo)
   ✓ Validaciones de integridad (sin duplicados)
   ✓ Uso correcto de herencia (Bebida < Producto)
   ✓ Anotaciones de tipos en todas las funciones

ARCHIVOS DEL PROYECTO:
======================
PARCIAL1/SEMANA 8/
├── README.md                          # Documentación completa
├── demo_solid.py                       # Script de demostración
├── restaurante_app/
│   ├── main.py                         # Punto de entrada + menú
│   ├── explicaciones.py                # Módulo educativo SOLID
│   ├── prueba_solid.py                 # Tests automatizados
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py                 # Clase base
│   │   ├── bebida.py                   # Hereda de Producto
│   │   └── cliente.py
│   └── servicios/
│       ├── __init__.py
│       └── restaurante.py              # Servicio (lógica)

COMO EJECUTAR:
==============
1. Individual (productos y clientes):
   $ python main.py

2. Pruebas (verificar SRP, OCP, LSP):
   $ python prueba_solid.py

3. Esta demostración:
   $ python demo_completo.py

PROXIMOS PASOS (Extensiones opcionales):
========================================
- Agregar clase Postre que herede de Producto
- Agregar persistencia en archivos JSON
- Agregar interfaz gráfica con tkinter
- Agregar base de datos (SQLite)
- Implementar patrones de diseño adicionales (Factory, Singleton, etc.)
""")


if __name__ == "__main__":
    print("\n")
    print("*" * 80)
    print("*" + " " * 78 + "*")
    print("*" + "  DEMOSTRACION COMPLETA: RESTAURANTE_APP CON EDUCACION SOLID  ".center(78) + "*")
    print("*" + " " * 78 + "*")
    print("*" * 80)

    try:
        demostrar_pruebas()
        demostrar_menu()
        resumen_funcionalidades()

        mostrar_separador()
        print("DEMOSTRACION COMPLETADA EXITOSAMENTE")
        mostrar_separador()

    except Exception as e:
        print(f"\nERROR durante la demostración: {e}")
        import traceback
        traceback.print_exc()

