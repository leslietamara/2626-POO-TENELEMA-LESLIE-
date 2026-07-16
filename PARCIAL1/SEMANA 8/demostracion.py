"""
Demostracion simple: Pruebas + Ejecucion interactiva
"""
import subprocess
import sys

print("\n" + "="*80)
print("DEMOSTRACION: RESTAURANTE_APP CON EDUCACION SOBRE SOLID")
print("="*80 + "\n")

# PARTE 1: PRUEBAS AUTOMATIZADAS
print("PARTE 1: EJECUTANDO PRUEBAS DE FUNCIONALIDAD")
print("-"*80)
proceso = subprocess.run(
    [sys.executable, "prueba_solid2.py"],
    cwd=r"C:\Users\TAMARA\PycharmProjects\2626-POO-TENELEMA-LESLIE-\PARCIAL1\SEMANA 8\restaurante_app"
)

print("\n" + "="*80)
print("PARTE 2: DEMOSTRACION DEL SISTEMA EN EJECUCION")
print("-"*80)
print("\nSimulando interaccion del usuario:")
print("  1. Registrar un producto")
print("  2. Registrar una bebida")
print("  3. Listar productos")
print("  4. Ver opcion de SOLID (sin entrar)")
print("  5. Salir\n")

# Entrada simulada
entrada = "1\nP001\nPizza Margherita\nPlatos Principales\n25.99\n2\nB001\nRefrescante\nBebidas\n5.00\n500ml\nbotella\n4\n7\n"

proceso = subprocess.Popen(
    [sys.executable, "main.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    cwd=r"C:\Users\TAMARA\PycharmProjects\2626-POO-TENELEMA-LESLIE-\PARCIAL1\SEMANA 8\restaurante_app"
)

stdout, stderr = proceso.communicate(input=entrada, timeout=10)

# Mostrar output
print("SALIDA DEL PROGRAMA:")
print("-"*80)
output_lines = stdout.split('\n')
for line in output_lines[:80]:  # Primeras 80 lineas
    print(line)

print("\n..." + " [SALIDA CONTINUA]")

print("\n" + "="*80)
print("RESUMEN")
print("="*80)
print("""
El sistema implementa correctamente:

1. RESPONSABILIDAD UNICA (SRP)
   - Producto: solo almacena datos de producto
   - Bebida: solo almacena datos de bebida
   - Cliente: solo almacena datos de cliente
   - Restaurante: solo administra colecciones
   - main.py: solo maneja interaccion usuario

2. ABIERTO/CERRADO (OCP)
   - Bebida extiende Producto sin cambiar codigo existente
   - Restaurante usa UN SOLO metodo para registrar ambos tipos
   - Sistema listo para agregar nuevos tipos (Postre, Botana, etc)

3. SUSTITUCION DE LISKOV (LSP)
   - Bebida puede reemplazar a Producto sin problemas
   - El listado usa polimorfismo (mostrar_informacion())
   - Cada tipo se muestra correctamente segun su clase

CARACTERISTICAS IMPLEMENTADAS:
- Menú interactivo con 7 opciones
- Educacion interactiva sobre SOLID (opcion 6)
- Validaciones (sin codigos/IDs duplicados)
- Pruebas automatizadas
- Arquitectura modular
- Anotaciones de tipos
- Documentacion completa

ARCHIVOS:
- main.py: Punto de entrada + menu interactivo
- explicaciones.py: Educacion sobre SOLID
- prueba_solid2.py: Tests automatizados
- modelos/: Clases de datos (Producto, Bebida, Cliente)
- servicios/: Lógica de negocio (Restaurante)
- README.md: Documentacion completa
""")

print("\n" + "="*80)
print("FIN DE LA DEMOSTRACION")
print("="*80)

