# 📚 Sistema Biblioteca - Constructores y Decoradores en Python

## 📖 Descripción

Este proyecto corresponde al ejemplo práctico desarrollado durante la **Semana 7** de la asignatura **Programación Orientada a Objetos (POO)**.

El sistema implementa una aplicación básica de consola para la gestión de libros y usuarios dentro de una biblioteca. Su principal objetivo es reforzar el uso de **constructores**, **decoradores**, **encapsulación mediante `@property` y `@setter`**, además de presentar el uso moderno de **`@dataclass`** como una alternativa para generar automáticamente constructores en Python.

La aplicación mantiene la arquitectura modular trabajada durante las semanas anteriores, separando el proyecto en **Modelos**, **Servicios** y el programa principal (`main.py`).

---

# 🎯 Objetivos de aprendizaje

Durante el desarrollo de este proyecto se aplican los siguientes conceptos:

- Implementar clases utilizando el constructor tradicional (`__init__`).
- Comprender cómo Python inicializa automáticamente los objetos.
- Aplicar el decorador `@dataclass` para simplificar la creación de clases orientadas a datos.
- Utilizar `@property` y `@setter` para controlar el acceso y modificación de atributos.
- Organizar un proyecto siguiendo una arquitectura por capas.
- Desarrollar una aplicación interactiva mediante un menú de consola.

---

# 📁 Estructura del proyecto

```text
biblioteca_app/
│
├── modelos/
│   ├── __init__.py
│   ├── libro.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   └── biblioteca.py
│
└── main.py
```

Cada carpeta cumple una responsabilidad específica:

- **modelos/** → Contiene las entidades principales del sistema.
- **servicios/** → Contiene la lógica que administra libros y usuarios.
- **main.py** → Controla la interacción con el usuario mediante un menú de consola.

---

# 🏗 Constructor tradicional (`__init__`)

La clase **Libro** utiliza el constructor tradicional para inicializar sus atributos.

```python
libro = Libro(
    "Python desde Cero",
    "Autor Ejemplo",
    "978000000001"
)
```

El constructor garantiza que cada objeto sea creado con la información necesaria antes de comenzar a utilizarlo.

---

# 🏷 Decorador `@dataclass`

La clase **Usuario** utiliza el decorador `@dataclass`.

Gracias a este decorador, Python genera automáticamente el constructor de la clase, reduciendo considerablemente la cantidad de código necesario.

```python
usuario = Usuario(
    "Juan Pérez",
    "juan@correo.com",
    1
)
```

Este enfoque resulta especialmente útil para clases cuyo propósito principal es almacenar información.

---

# 🔒 Encapsulación con `@property`

La clase **Libro** implementa propiedades para controlar el acceso a sus atributos.

```python
@property
def titulo(self):
    return self._titulo
```

El decorador `@property` permite acceder al atributo como si fuera una variable, aunque internamente se ejecuta un método.

Ejemplo:

```python
print(libro.titulo)
```

---

# ✏ Modificación de atributos con `@setter`

Los métodos `@setter` permiten validar o controlar los cambios realizados sobre un atributo.

```python
@titulo.setter
def titulo(self, nuevo_titulo):

    if not nuevo_titulo.strip():
        raise ValueError("El título no puede estar vacío.")

    self._titulo = nuevo_titulo
```

De esta manera se garantiza que los datos almacenados por el objeto sean consistentes.

---

# 📄 Método `mostrar_informacion()`

Cada entidad implementa un método llamado `mostrar_informacion()`.

Este método devuelve una representación legible del objeto para mostrarla al usuario.

Ejemplo:

```python
print(libro.mostrar_informacion())
```

Esto permite mantener organizada la lógica de presentación de cada entidad.

---

# ⚙ Arquitectura por capas

El proyecto mantiene una estructura modular sencilla.

## Modelos

Representan las entidades del sistema.

- Libro
- Usuario

## Servicios

Administran la lógica del sistema.

- Registrar libros.
- Registrar usuarios.
- Buscar información.
- Listar registros.

## Programa principal

Coordina la interacción con el usuario mediante un menú de opciones.

Esta separación facilita la organización y mantenimiento del código.

---

# 📋 Menú interactivo

El sistema incorpora un menú que permite ejecutar las principales operaciones de la aplicación.

```text
==============================
     SISTEMA DE BIBLIOTECA
==============================

1. Registrar libro
2. Listar libros
3. Buscar libro
--------------------------------
4. Registrar usuario
5. Listar usuarios
6. Buscar usuario
--------------------------------
7. Salir
```

Cada opción llama a una función específica, favoreciendo una mejor organización del programa.

---

# 💡 Buenas prácticas aplicadas

Durante el desarrollo del proyecto se implementaron las siguientes buenas prácticas:

- Organización del código mediante paquetes.
- Separación de responsabilidades entre modelos, servicios y programa principal.
- Uso de nombres descriptivos para clases, métodos y variables.
- Documentación mediante docstrings.
- Encapsulación utilizando `@property` y `@setter`.
- Uso de `@dataclass` cuando la clase representa principalmente datos.
- Métodos pequeños con una única responsabilidad.
- Reutilización de funciones para organizar el menú principal.

---

# 🆕 Conceptos aprendidos en esta práctica

Al finalizar este proyecto se fortalecen los siguientes conocimientos:

- Constructor tradicional (`__init__`).
- Decorador `@dataclass`.
- Decoradores `@property` y `@setter`.
- Inicialización correcta de objetos.
- Organización de aplicaciones mediante arquitectura por capas.
- Desarrollo de aplicaciones de consola utilizando funciones y menús interactivos.

---

# 📌 Conclusión

El constructor (`__init__`) continúa siendo una herramienta fundamental para inicializar objetos cuando se requiere mayor control sobre sus atributos.

Por otro lado, `@dataclass` representa una alternativa moderna que simplifica la creación de clases orientadas al almacenamiento de datos, reduciendo la cantidad de código necesario.

Asimismo, el uso de `@property` y `@setter` permite aplicar el principio de encapsulación, controlando el acceso y la modificación de la información de una manera más segura y organizada.

La combinación de estos elementos permite desarrollar aplicaciones orientadas a objetos más claras, mantenibles y alineadas con las buenas prácticas actuales de programación en Python.