#!/usr/bin/env python3
"""peso 6
color plomo con negro

main.py

Programa de ejemplo en POO que utiliza la clase Mascota definida en mascota.py.
"""

from mascota import Mascota


def solicitar_texto(prompt, obligatorio=True):
    while True:
        valor = input(prompt).strip()
        if valor or not obligatorio:
            return valor
        print('El campo es obligatorio. Intente de nuevo.')


def solicitar_entero(prompt, obligatorio=True, minimo=None):
    while True:
        valor = input(prompt).strip()
        if not valor and not obligatorio:
            return None
        try:
            n = int(valor)
            if minimo is not None and n < minimo:
                print(f'El valor debe ser >= {minimo}.')
                continue
            return n
        except ValueError:
            print('Ingrese un número entero válido.')


def solicitar_flotante(prompt, obligatorio=True, minimo=None):
    while True:
        valor = input(prompt).strip()
        if not valor and not obligatorio:
            return None
        try:
            f = float(valor)
            if minimo is not None and f < minimo:
                print(f'El valor debe ser >= {minimo}.')
                continue
            return f
        except ValueError:
            print('Ingrese un número válido (ej. 3.5).')


def crear_mascota():
    print('\n--- Crear nueva mascota (POO) ---')
    nombre = solicitar_texto('Nombre: ')
    especie = solicitar_texto('Especie: ')
    raza = solicitar_texto('Raza (opcional): ', obligatorio=False)
    edad = solicitar_entero('Edad (años, opcional): ', obligatorio=False, minimo=0)
    sexo = solicitar_texto('Sexo (M/F/O, opcional): ', obligatorio=False)
    peso = solicitar_flotante('Peso (kg, opcional): ', obligatorio=False, minimo=0)
    color = solicitar_texto('Color/Descripción (opcional): ', obligatorio=False)
    propietario = solicitar_texto('Propietario (opcional): ', obligatorio=False)
    contacto = solicitar_texto('Contacto (opcional): ', obligatorio=False)
    vacunas_txt = solicitar_texto('Vacunas (separadas por comas, opcional): ', obligatorio=False)
    vacunas = [v.strip() for v in vacunas_txt.split(',') if v.strip()] if vacunas_txt else []
    observaciones = solicitar_texto('Observaciones (opcional): ', obligatorio=False)

    m = Mascota(nombre=nombre, especie=especie, raza=raza, edad=edad, sexo=sexo,
                peso_kg=peso, color=color, propietario=propietario, contacto=contacto,
                vacunas=vacunas, observaciones=observaciones)
    print('Mascota creada correctamente.\n')
    return m


def main():
    mascotas = []
    # Demostración mínima: crear al menos dos objetos y ejecutar los métodos pedidos
    print('Demostración POO: crear 2 mascotas y ejecutar métodos')
    demo1 = Mascota(nombre='Fido', especie='Perro', edad=3)
    demo2 = Mascota(nombre='Misu', especie='Gato', edad=2)
    mascotas.extend([demo1, demo2])
    print('\n--- Demostración: salida de los dos objetos ---')
    for m in (demo1, demo2):
        m.mostrar_informacion()
        m.hacer_sonido()

    print('\nPrograma POO: gestión básica de mascotas')
    while True:
        print('\nOpciones:')
        print('[1] Crear mascota')
        print('[2] Listar mascotas (resumen)')
        print('[3] Mostrar mascota (detalle)')
        print('[4] Salir')
        opcion = solicitar_texto('Opción: ')

        if opcion == '1':
            m = crear_mascota()
            mascotas.append(m)
        elif opcion == '2':
            if not mascotas:
                print('No hay mascotas registradas.')
            else:
                print('\n--- Resumen de mascotas ---')
                for i, mm in enumerate(mascotas, start=1):
                    print(f'{i}. {mm.nombre} ({mm.especie})')
        elif opcion == '3':
            if not mascotas:
                print('No hay mascotas registradas.')
            else:
                idx = solicitar_entero('Ingrese el número de mascota a mostrar: ', minimo=1)
                if idx is None or idx < 1 or idx > len(mascotas):
                    print('Índice fuera de rango.')
                else:
                    mascotas[idx-1].mostrar()
        elif opcion == '4':
            print('Saliendo. ¡Hasta luego!')
            break
        else:
            print('Opción no válida, intente de nuevo.')


if __name__ == '__main__':
    main()

