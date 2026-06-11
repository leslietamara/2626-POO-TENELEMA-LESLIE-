 #!/usr/bin/env python3
"""
tradicional.py

Programa de programación tradicional que registra y muestra información de una mascota
utilizando únicamente variables y funciones (sin clases ni objetos).

Estructura:
 - registrar_mascota(): solicita datos por teclado y devuelve un diccionario con la info
 - mostrar_mascota(m): muestra de forma organizada la información de la mascota

Autor: Generado automáticamente
"""

def solicitar_texto(prompt, obligatorio=True):
    """Solicita una cadena al usuario. Si es obligatorio, vuelve a preguntar si está vacía."""
    while True:
        valor = input(prompt).strip()
        if valor or not obligatorio:
            return valor
        print("El campo es obligatorio. Por favor ingrese un valor.")


def solicitar_entero(prompt, obligatorio=True, minimo=None):
    """Solicita un entero al usuario con validación básica."""
    while True:
        valor = input(prompt).strip()
        if not valor and not obligatorio:
            return None
        try:
            n = int(valor)
            if minimo is not None and n < minimo:
                print(f"El valor debe ser >= {minimo}.")
                continue
            return n
        except ValueError:
            print("Por favor ingrese un número entero válido.")


def solicitar_flotante(prompt, obligatorio=True, minimo=None):
    """Solicita un número flotante al usuario con validación básica."""
    while True:
        valor = input(prompt).strip()
        if not valor and not obligatorio:
            return None
        try:
            f = float(valor)
            if minimo is not None and f < minimo:
                print(f"El valor debe ser >= {minimo}.")
                continue
            return f
        except ValueError:
            print("Por favor ingrese un número válido (por ejemplo: 3.5).")


def registrar_mascota():
    """Solicita por teclado los datos de la mascota y devuelve un diccionario con la información."""
    print('\n--- Registro de mascota ---')
    mascota = {}
    mascota['nombre'] = solicitar_texto('Nombre de la mascota: ')
    mascota['especie'] = solicitar_texto('Especie (ej. Perro, Gato, Ave): ')
    mascota['raza'] = solicitar_texto('Raza (si no aplica, dejar vacío): ', obligatorio=False)
    mascota['edad'] = solicitar_entero('Edad (años): ', obligatorio=False, minimo=0)
    mascota['sexo'] = solicitar_texto('Sexo (M/F/O): ', obligatorio=False)
    mascota['peso_kg'] = solicitar_flotante('Peso (kg): ', obligatorio=False, minimo=0)
    mascota['color'] = solicitar_texto('Color/Descripción física: ', obligatorio=False)
    propietario = solicitar_texto('Nombre del propietario: ', obligatorio=False)
    contacto = solicitar_texto('Teléfono / contacto: ', obligatorio=False)
    mascota['propietario'] = propietario
    mascota['contacto'] = contacto

    vacunas = solicitar_texto('Vacunas (lista separada por comas, o dejar vacío): ', obligatorio=False)
    if vacunas:
        mascota['vacunas'] = [v.strip() for v in vacunas.split(',') if v.strip()]
    else:
        mascota['vacunas'] = []

    mascota['observaciones'] = solicitar_texto('Observaciones adicionales: ', obligatorio=False)

    print('\nRegistro completado.\n')
    return mascota


def mostrar_mascota(m):
    """Muestra de forma organizada la información de la mascota.

    Recibe un diccionario con los campos definidos en registrar_mascota.
    """
    if not m:
        print('No hay información de la mascota para mostrar.')
        return

    print('======================== INFORMACIÓN DE LA MASCOTA ========================')
    print(f"Nombre         : {m.get('nombre','-')}")
    print(f"Especie        : {m.get('especie','-')}")
    print(f"Raza           : {m.get('raza','-')}")
    edad = m.get('edad')
    print(f"Edad (años)    : {edad if edad is not None else '-'}")
    print(f"Sexo           : {m.get('sexo','-')}")
    peso = m.get('peso_kg')
    print(f"Peso (kg)      : {peso if peso is not None else '-'}")
    print(f"Color/Descripción: {m.get('color','-')}")
    print('------------------------- Información del propietario -----------------------')
    print(f"Propietario    : {m.get('propietario','-')}")
    print(f"Contacto       : {m.get('contacto','-')}")
    print('------------------------- Vacunas y observaciones -------------------------')
    vacunas = m.get('vacunas', [])
    if vacunas:
        print('Vacunas        : ' + ', '.join(vacunas))
    else:
        print('Vacunas        : -')
    obs = m.get('observaciones')
    print(f"Observaciones  : {obs if obs else '-'}")
    print('==========================================================================')


def main():
    """Función principal: maneja el flujo simple de registro y muestra."""
    print('Programa de registro de mascotas (sin clases, usando funciones).')
    while True:
        opcion = solicitar_texto('\nElija una opción: [1] Registrar mascota  [2] Salir\nOpción: ')
        if opcion == '1':
            mascota = registrar_mascota()
            mostrar_mascota(mascota)
        elif opcion == '2':
            print('Saliendo. ¡Hasta luego!')
            break
        else:
            print('Opción no válida. Ingrese 1 o 2.')


if __name__ == '__main__':
    main()


