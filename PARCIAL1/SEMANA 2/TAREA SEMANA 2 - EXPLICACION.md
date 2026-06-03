# Explicación detallada del código (Clase `Estudiante`)

Este documento explica paso a paso el archivo `TAREA SEMANA 2.py`, pensado para quien está empezando con Programación Orientada a Objetos (POO).

## 1. ¿Qué es la Programación Orientada a Objetos?
- Clase: plantilla o molde que describe un tipo de objeto (por ejemplo, `Estudiante`).
- Objeto (instancia): un elemento concreto creado a partir de la clase (por ejemplo, `alumno`).
- Atributos: características del objeto (nombre, edad, etc.).
- Métodos: funciones dentro de la clase que definen comportamientos (agregar calificación, calcular promedio).
- Encapsulamiento: agrupar datos y funciones relacionadas en la clase.

## 2. Estructura general del archivo
El archivo contiene:
- La definición de la clase `Estudiante` con sus atributos y métodos.
- Un bloque `if __name__ == "__main__":` que actúa como demo ejecutable.

## 3. Explicación línea por línea (bloques importantes)

### Definición de la clase
- `class Estudiante:`
  - Declara una nueva clase llamada `Estudiante`.

### Constructor (__init__)
- `def __init__(self, nombre, edad, grado):`
  - El constructor se ejecuta al crear una instancia. `self` representa la nueva instancia.
  - `self.nombre = nombre`: guarda el nombre en el objeto.
  - `self.edad = int(edad)`: convierte y guarda la edad como entero.
  - `self.grado = grado`: guarda el grado (por ejemplo, "Segundo").
  - `self.calificaciones = []`: inicializa una lista vacía para las notas.

¿Por qué `self`? Porque permite que cada objeto mantenga sus propios datos.

### Método `agregar_calificacion`
- `def agregar_calificacion(self, nota):`
  - Valida que la `nota` esté entre 0 y 100.
  - Si no está en ese rango, lanza `ValueError` para indicar un uso incorrecto.
  - Si es válida, añade la nota (convertida a `float`) a `self.calificaciones`.

Esto demuestra validación básica y modificación del estado interno del objeto.

### Método `promedio`
- `def promedio(self):`
  - Si la lista de calificaciones está vacía, devuelve `None` (no hay promedio).
  - Si hay notas, devuelve la suma de las notas dividida por la cantidad.

Nota: devolver `None` permite distinguir "sin datos" de "promedio 0".

### Método `es_aprobado`
- `def es_aprobado(self, minima=60):`
  - Calcula el promedio y compara con la nota mínima (`minima`, por defecto 60).
  - Si no hay promedio (`None`) devuelve `False`.
  - Devuelve `True` si el promedio es mayor o igual a `minima`, `False` en caso contrario.

Esto muestra cómo un método puede usar otros métodos de la misma clase.

### Método `mostrar_info`
- `def mostrar_info(self):`
  - Obtiene el promedio y lo formatea con 2 decimales si existe; si no, muestra `N/A`.
  - Devuelve una cadena con la información principal del estudiante.

Es útil para presentar datos de forma legible.

### Método especial `__repr__`
- `def __repr__(self):`
  - Provee una representación legible del objeto, útil para depuración.

### Bloque ejecutable (demo)
- `if __name__ == "__main__":`
  - Esto evita que el código de demostración se ejecute si se importa la clase desde otro archivo.
  - Dentro de este bloque:
    - Se crea una instancia: `alumno = Estudiante("Ana Pérez", 20, "Segundo")`.
    - Se agregan calificaciones: `85`, `92`, `78`.
    - Se imprime la información, el promedio y si está aprobado.

## 4. Cómo ejecutar el programa
Desde la terminal (en la carpeta del proyecto) ejecuta:

```bash
python "PARCIAL1/SEMANA 2/TAREA SEMANA 2.py"
```

Salida esperada (aprox.):

- Una línea con la info del estudiante, por ejemplo:
  `Estudiante: Ana Pérez, Edad: 20, Grado: Segundo, Promedio: 85.00`
- `Promedio: 85.0`
- `Aprobado: Sí`

(El formato exacto puede variar según el formateo de `mostrar_info()`.)

## 5. Consejos para practicar
- Cambia las notas y prueba distintos valores límite (0, 100, 59.9, 60).
- Crea más instancias para entender que cada objeto guarda sus propios datos.
- Añade métodos nuevos, por ejemplo `aplicar_recuperacion()` o `cantidad_de_notas()`.
- Intenta capturar la excepción `ValueError` al agregar una nota inválida.

## 6. Resumen breve de conceptos clave
- Clase: plantilla; `Estudiante` es la plantilla.
- Instancia/objeto: `alumno` es un objeto de la clase `Estudiante`.
- Atributos: variables dentro del objeto (`nombre`, `edad`, ...).
- Métodos: funciones que actúan sobre el objeto (`agregar_calificacion`, `promedio`, ...).

---
Si quieres, puedo:
- Añadir explicación línea por línea con números de línea.
- Traducir esto a un PDF o a un `README.md` más corto.
- Modificar el programa para leer calificaciones desde teclado o archivo.

Archivo creado: [PARCIAL1/SEMANA 2/TAREA SEMANA 2 - EXPLICACION.md](PARCIAL1/SEMANA 2/TAREA SEMANA 2 - EXPLICACION.md)
