"""
Modulo educativo: Explicacion didactica de principios SOLID
aplicados al sistema de restaurante.
"""
def mostrar_intro_solid() -> None:
    """Muestra una introduccion a SOLID al inicio del programa."""
    print("\n" + "=" * 60)
    print("BIENVENIDO AL SISTEMA DE RESTAURANTE")
    print("=" * 60)
    print("\nEste programa fue diseñado aplicando principios SOLID,")
    print("un conjunto de reglas que hacen el codigo mas mantenible")
    print("y extensible. ¡Aprenderas como funcionan!")
    print("\n" + "=" * 60 + "\n")
def explicar_srp() -> None:
    """Explica el Principio de Responsabilidad Unica (SRP)."""
    print("\n" + "=" * 60)
    print("PRINCIPIO S -- Responsabilidad Unica (SRP)")
    print("=" * 60)
    print("""
DEFINICION: Una clase debe tener una unica razon para cambiar.
EN NUESTRO RESTAURANTE:
  * Producto y Bebida -> solo representan datos
  * Cliente -> solo representa un cliente
  * Restaurante -> solo administra colecciones y validaciones
  * main.py -> solo maneja la interaccion por consola
Resultado: Si quieres cambiar como se guardan datos,
solo editas Restaurante. Cada archivo es responsable de una cosa!
""")
def explicar_ocp() -> None:
    """Explica el Principio Abierto/Cerrado (OCP)."""
    print("\n" + "=" * 60)
    print("PRINCIPIO O -- Abierto/Cerrado (OCP)")
    print("=" * 60)
    print("""
DEFINICION: Una clase debe estar ABIERTA para extension pero CERRADA para modificacion.
EN NUESTRO RESTAURANTE:
  * Bebida hereda de Producto SIN modificar Producto
  * Restaurante registra Producto y Bebida en UNA lista
  * Si quieres agregar nuevos tipos:
    - Creas una nueva clase que herede de Producto
    - Restaurante NO cambia!
Resultado: El sistema es extensible sin riesgo de romper codigo.
""")
def explicar_lsp() -> None:
    """Explica el Principio de Sustitucion de Liskov (LSP)."""
    print("\n" + "=" * 60)
    print("PRINCIPIO L -- Sustitucion de Liskov (LSP)")
    print("=" * 60)
    print("""
DEFINICION: Un objeto de una clase derivada debe poder reemplazar a un
objeto de la clase base sin que el programa se rompa.
EN NUESTRO RESTAURANTE:
  * Bebida hereda de Producto
  * Ambas implementan mostrar_informacion()
  * Restaurante solo llama mostrar_informacion() en cada objeto
  * Bebida puede reemplazar a Producto sin problemas!
Resultado: El codigo es predecible y las subclases son intercambiables.
""")
def mostrar_menu_solid() -> None:
    """Muestra un menu interactivo para explorar principios SOLID."""
    while True:
        print("\n" + "=" * 60)
        print("APRENDER SOBRE PRINCIPIOS SOLID EN RESTAURANTE")
        print("=" * 60)
        print("1. Principio S - Responsabilidad Unica (SRP)")
        print("2. Principio O - Abierto/Cerrado (OCP)")
        print("3. Principio L - Sustitucion de Liskov (LSP)")
        print("4. Ver resumen combinado")
        print("5. Volver al menu principal")
        opcion = input("\nSeleccione una opcion: ").strip()
        if opcion == "1":
            explicar_srp()
        elif opcion == "2":
            explicar_ocp()
        elif opcion == "3":
            explicar_lsp()
        elif opcion == "4":
            mostrar_resumen_solid()
        elif opcion == "5":
            return
        else:
            print("Opcion no valida. Intente de nuevo.")
        input("\nPresione Enter para continuar...")
def mostrar_resumen_solid() -> None:
    """Muestra un resumen de los 3 principios SOLID aplicados."""
    print("\n" + "=" * 60)
    print("RESUMEN: 3 PRINCIPIOS SOLID EN RESTAURANTE_APP")
    print("=" * 60)
    print("""
RESPONSABILIDAD UNICA (SRP):
  * Producto: solo guarda datos de un producto
  * Bebida: solo guarda datos de una bebida
  * Cliente: solo guarda datos de un cliente
  * Restaurante: solo administra colecciones
  * main.py: solo maneja interaccion con usuario
  Resultado: Codigo modular y facil de mantener
ABIERTO/CERRADO (OCP):
  * Bebida hereda de Producto SIN modificar Producto
  * Restaurante registra ambos en UNA lista
  * Si quieres agregar nuevos tipos, solo creas nuevas clases
  * Restaurante nunca cambia!
  Resultado: Extensible sin riesgo de romper codigo
SUSTITUCION DE LISKOV (LSP):
  * Bebida puede reemplazar a Producto en cualquier lugar
  * Ambas usan el metodo comun: mostrar_informacion()
  * Restaurante.listar_productos() funciona con ambas
  Resultado: Codigo predecible y sin sorpresas
CONCLUSION: SOLID permite que el restaurante_app sea:
  [OK] Facil de entender (cada clase = UN proposito claro)
  [OK] Facil de mantener (cambios localizados)
  [OK] Facil de extender (nuevos tipos sin modificar existentes)
  [OK] Robusto (comportamiento predecible)
""")
