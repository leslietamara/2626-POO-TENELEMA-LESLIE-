"""Script para demostración automática de SOLID en main.py"""

import subprocess
import sys

# Simular entrada de usuario:
# 6 (Aprender SOLID)
# 1 (Ver SRP)
# 5 (Volver)
# 1 (Ver OCP)
# 5 (Volver)
# 1 (Ver LSP)
# 5 (Volver)
# 7 (Salir)

entrada = "6\n1\n5\n2\n5\n3\n5\n4\n5\n7\n"

proceso = subprocess.Popen(
    [sys.executable, "main.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    cwd=r"C:\Users\TAMARA\PycharmProjects\2626-POO-TENELEMA-LESLIE-\PARCIAL1\SEMANA 8\restaurante_app"
)

stdout, stderr = proceso.communicate(input=entrada, timeout=10)

if stderr:
    print("STDERR:")
    print(stderr)
else:
    print("DEMOSTRACION DE MAIN.PY CON EDUCACIÓN SOBRE SOLID")
    print("=" * 80)
    print(stdout[:3000])  # Mostrar primeros 3000 caracteres
    print("\n... [salida truncada] ...\n")
    print(f"[Última parte de la salida]")
    print(stdout[-1000:])  # Mostrar últimos 1000 caracteres

