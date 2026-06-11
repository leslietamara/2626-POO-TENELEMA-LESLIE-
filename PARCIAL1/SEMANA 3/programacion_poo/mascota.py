#!/usr/bin/env python3
"""
mascota.py

Implementa la clase Mascota para la solución en POO.
"""

class Mascota:
    """Representa una mascota con atributos básicos y métodos de utilidad."""

    def __init__(self, nombre, especie, raza=None, edad=None, sexo=None,
                 peso_kg=None, color=None, propietario=None, contacto=None,
                 vacunas=None, observaciones=None):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.sexo = sexo
        self.peso_kg = peso_kg
        self.color = color
        self.propietario = propietario
        self.contacto = contacto
        self.vacunas = vacunas or []
        self.observaciones = observaciones

    def mostrar(self):
        """Muestra la información formateada de la mascota."""
        print('======================== INFORMACIÓN DE LA MASCOTA (POO) ========================')
        print(f"Nombre         : {self.nombre}")
        print(f"Especie        : {self.especie}")
        print(f"Raza           : {self.raza or '-'}")
        print(f"Edad (años)    : {self.edad if self.edad is not None else '-'}")
        print(f"Sexo           : {self.sexo or '-'}")
        print(f"Peso (kg)      : {self.peso_kg if self.peso_kg is not None else '-'}")
        print(f"Color/Descripción: {self.color or '-'}")
        print('------------------------- Información del propietario -----------------------')
        print(f"Propietario    : {self.propietario or '-'}")
        print(f"Contacto       : {self.contacto or '-'}")
        print('------------------------- Vacunas y observaciones -------------------------')
        print('Vacunas        : ' + (', '.join(self.vacunas) if self.vacunas else '-'))
        print(f"Observaciones  : {self.observaciones or '-'}")
        print('==========================================================================')

    def mostrar_informacion(self):
        """Método público requerido: muestra la información de la mascota.

        Implementa la interfaz pedida por la consigna (nombre, especie, edad)
        delegando en el método de salida existente.
        """
        self.mostrar()

    def hacer_sonido(self):
        """Método público requerido: imprime un sonido representativo según la especie.

        La implementación usa una tabla simple por especie y un mensaje por defecto.
        """
        especie_clave = (self.especie or '').strip().lower()
        sonidos = {
            'perro': 'Guau!',
            'gato': 'Miau!',
            'ave': 'Pío!',
            'pajaro': 'Pío!',
            'vaca': 'Muu!',
            'caballo': 'Hiii!',
            'conejo': '... (silbido)'
        }
        sonido = sonidos.get(especie_clave, 'Sonido desconocido')
        print(f"{self.nombre} ({self.especie or '—'}) hace: {sonido}")

    def to_dict(self):
        """Devuelve un diccionario con los datos de la mascota."""
        return {
            'nombre': self.nombre,
            'especie': self.especie,
            'raza': self.raza,
            'edad': self.edad,
            'sexo': self.sexo,
            'peso_kg': self.peso_kg,
            'color': self.color,
            'propietario': self.propietario,
            'contacto': self.contacto,
            'vacunas': list(self.vacunas),
            'observaciones': self.observaciones,
        }

