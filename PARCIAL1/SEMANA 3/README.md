# SEMANA 3: Introducción a la Programación Orientada a Objetos (POO)

## Objetivos de la Semana

En esta semana, se explora el contraste entre dos paradigmas de programación:

1. **Programación Orientada a Objetos (POO)** - Enfoque moderno y escalable
2. **Programación Tradicional** - Enfoque funcional basado en variables y funciones

Se implementa un sistema de **gestión de mascotas** utilizando ambos enfoques para comparar sus ventajas y diferencias.

---

## Conceptos Clave

### ¿Qué es la Programación Orientada a Objetos (POO)?

La POO es un paradigma de programación que organiza el código alrededor de **objetos** que contienen:

- **Atributos (propiedades)**: Datos que describe el objeto
- **Métodos**: Acciones/funciones que el objeto puede realizar

**Ventajas:**
- ✅ Código más organizado y reutilizable
- ✅ Facilita el mantenimiento y escalabilidad
- ✅ Modelado más cercano a la realidad
- ✅ Mejor encapsulación de datos

### Programación Tradicional

Utiliza principalmente:
- Variables para almacenar datos
- Funciones para procesar esos datos
- Estructuras de datos simples (diccionarios, listas, tuplas)

**Características:**
- Código más directo y simple para programas pequeños
- Menor curva de aprendizaje
- Menos abstracción

---

## Estructura del Proyecto

```
SEMANA 3/
├── programacion_poo/
│   ├── main.py          # Programa principal (interfaz y menú)
│   └── mascota.py       # Definición de la clase Mascota
├── programacion_tradicional/
│   └── tradicional.py   # Programa completo sin clases
└── README.md            # Este archivo
```

---

## Descripción de Archivos

### 📁 Carpeta `programacion_poo/`

#### `mascota.py` - Definición de la Clase

Define la clase `Mascota` con los siguientes elementos:

**Atributos:**
```python
- nombre         # Nombre de la mascota (requerido)
- especie        # Tipo de animal (requerido)
- raza           # Raza de la mascota
- edad           # Edad en años
- sexo           # Sexo (M/F/O)
- peso_kg        # Peso en kilogramos
- color          # Color o descripción física
- propietario    # Nombre del propietario
- contacto       # Teléfono o contacto del propietario
- vacunas        # Lista de vacunas aplicadas
- observaciones  # Notas adicionales
```

**Métodos:**
- `__init__()` - Constructor que inicializa todos los atributos
- `mostrar()` - Muestra la información de forma formateada
- `mostrar_informacion()` - Interfaz pública para mostrar info
- `hacer_sonido()` - Emite un sonido según la especie (Guau, Miau, etc.)
- `to_dict()` - Convierte el objeto a diccionario

#### `main.py` - Programa Principal

Implementa la interfaz de usuario interactiva con las siguientes funciones:

**Funciones auxiliares:**
- `solicitar_texto()` - Valida entrada de texto
- `solicitar_entero()` - Valida entrada numérica entera
- `solicitar_flotante()` - Valida entrada numérica decimal

**Funciones principales:**
- `crear_mascota()` - Crea una nueva mascota pidiendo datos al usuario
- `main()` - Menú principal con opciones:
  - [1] Crear mascota
  - [2] Listar mascotas (resumen)
  - [3] Mostrar mascota (detalle)
  - [4] Salir

**Demostración:**
Al iniciar, el programa crea automáticamente 2 mascotas de demostración:
- Fido (Perro, 3 años)
- Misu (Gato, 2 años)

### 📁 Carpeta `programacion_tradicional/`

#### `tradicional.py` - Solución sin POO

Implementa el mismo sistema de gestión de mascotas **sin usar clases**:

**Estructuras de datos:**
- Diccionarios para almacenar información de mascotas
- Listas para almacenar múltiples mascotas

**Funciones:**
- `solicitar_texto()` - Validación de entrada
- `solicitar_entero()` - Validación de números enteros
- `solicitar_flotante()` - Validación de números decimales
- `registrar_mascota()` - Crea un diccionario con datos de la mascota
- `mostrar_mascota()` - Muestra la información del diccionario
- `main()` - Menú con opciones para registrar y visualizar mascotas

---

## Comparación: POO vs Programación Tradicional

| Aspecto | POO | Tradicional |
|---------|-----|------------|
| **Organizacion** | Encapsulada en clases | Funciones y diccionarios |
| **Reutilización** | Fácil (herencia, polimorfismo) | Más difícil |
| **Mantenimiento** | Mejor para proyectos grandes | Mejor para proyectos pequeños |
| **Legibilidad** | Código descriptivo | Menos estructura |
| **Memoria** | Más recursos | Más ligero |
| **Escalabilidad** | Excelente | Limitada |

---

## Características Demostradas

### 1. Creación de Objetos
```python
# POO
mascota1 = Mascota(nombre='Fido', especie='Perro', edad=3)

# Tradicional
mascota1 = {'nombre': 'Fido', 'especie': 'Perro', 'edad': 3}
```

### 2. Métodos vs Funciones
```python
# POO - El método pertenece al objeto
mascota1.hacer_sonido()

# Tradicional - La función recibe el diccionario como parámetro
hacer_sonido(mascota1)
```

### 3. Validación de Entrada
Ambos enfoques implementan validación robusta con:
- Campos obligatorios y opcionales
- Validación de tipos de datos
- Valores mínimos permitidos

### 4. Interfaz de Usuario
- Menú interactivo en consola
- Opciones para crear, listar y visualizar mascotas
- Manejo de errores y validaciones

---

## Cómo Ejecutar

### Opción 1: Ejecutar la versión POO

```bash
cd "C:\Users\TAMARA\UEA\2626-POO-TENELEMA-LESLIE-\PARCIAL1\SEMANA 3\programacion_poo"
python main.py
```

### Opción 2: Ejecutar la versión Tradicional

```bash
cd "C:\Users\TAMARA\UEA\2626-POO-TENELEMA-LESLIE-\PARCIAL1\SEMANA 3\programacion_tradicional"
python tradicional.py
```

---

## Ejemplo de Uso

### Sesión Inicial (Demostración POO)

```
Demostración POO: crear 2 mascotas y ejecutar métodos

--- Demostración: salida de los dos objetos ---
======================== INFORMACIÓN DE LA MASCOTA (POO) ========================
Nombre         : Fido
Especie        : Perro
...
==========================================================================

Fido (Perro) hace: Guau!

Programa POO: gestión básica de mascotas

Opciones:
[1] Crear mascota
[2] Listar mascotas (resumen)
[3] Mostrar mascota (detalle)
[4] Salir
Opción: 
```

---

## Aprendizajes Clave

1. **Clases y Objetos**: Una clase es un plano, un objeto es una instancia
2. **Encapsulación**: Los datos y métodos están juntos en el objeto
3. **Reutilización**: Crear múltiples objetos Mascota a partir de una sola clase
4. **Mantenibilidad**: Los cambios se hacen una sola vez en la clase
5. **Comparación**: La POO es más poderosa para sistemas complejos

---

## Recursos Adicionales

### Conceptos de POO a Profundizar

- **Herencia**: Una clase puede heredar de otra
- **Polimorfismo**: Métodos con el mismo nombre, diferente comportamiento
- **Abstracción**: Ocultar complejidad innecesaria
- **Getters/Setters**: Métodos para acceder y modificar atributos

### Próximas Sesiones

Se espera que en semanas posteriores se exploren estos conceptos avanzados y se creen sistemas más complejos aplicando principios SOLID.

---

## Nota del Autor

Este proyecto demuestra cómo el mismo problema (gestión de mascotas) se resuelve de dos formas diferentes. La elección del paradigma depende de:

- Tamaño y complejidad del proyecto
- Necesidad de escalabilidad
- Equipo de desarrollo
- Mantenimiento futuro

**Para proyectos educativos y profesionales, se recomienda la POO.**

---

**Última actualización:** Semana 3 - Junio 2026

