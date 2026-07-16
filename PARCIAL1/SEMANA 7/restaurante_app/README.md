# Sistema de Restaurante - Programación Orientada a Objetos

**Autor:** Tamara  
**Fecha:** Semana 7 - Parcial 1  
**Materia:** Programación Orientada a Objetos en Python

---

## Descripción del Sistema

El **Sistema de Restaurante** es una aplicación de consola desarrollada en Python que permite la gestión básica de un restaurante. El sistema implementa un menú interactivo que permite registrar, listar y buscar tanto productos como clientes del restaurante.

### Objetivo Principal

Demostrar la aplicación de conceptos fundamentales de la Programación Orientada a Objetos (POO), incluyendo:
- Constructores tradicionales y personalizados
- Decoradores `@property` y `@setter`
- Decorador `@dataclass`
- Arquitectura modular por capas
- Creación dinámica de objetos a partir de entrada del usuario

---

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
├── main.py
└── README.md
```

### Responsabilidad de Cada Componente

#### **modelos/producto.py**
Define la clase `Producto` con:
- **Constructor tradicional `__init__`**: Inicializa los atributos del producto
- **Atributos privados**: `_nombre`, `_categoria`, `_precio`, `_disponible`
- **Decoradores `@property`**: Permiten acceso controlado a los atributos
- **Decoradores `@setter`**: Permiten modificación con validaciones

**Validaciones implementadas:**
- Nombre no puede estar vacío
- Categoría no puede estar vacía
- Precio debe ser mayor que cero
- Precio debe ser un número válido

#### **modelos/cliente.py**
Define la clase `Cliente` usando el decorador `@dataclass`:
- **Atributos**: `id_cliente`, `nombre`, `correo`
- **Método `mostrar_informacion()`**: Presenta los datos de forma legible
- Simplifica la creación de objects sin necesidad de escribir `__init__` manual

#### **servicios/restaurante.py**
Define la clase `Restaurante` como servicio centralizado:
- Administra dos listas: `productos` y `clientes`
- **Métodos para productos**:
  - `registrar_producto()`
  - `listar_productos()`
  - `buscar_producto_por_nombre()`
  - `buscar_productos_por_categoria()`
  - `cantidad_productos()`
- **Métodos para clientes**:
  - `registrar_cliente()`
  - `listar_clientes()`
  - `buscar_cliente_por_id()`
  - `buscar_cliente_por_nombre()`
  - `cantidad_clientes()`

#### **main.py**
Punto de arranque del programa:
- Implementa el menú interactivo
- Solicita datos al usuario mediante `input()`
- Crea objetos a partir de los datos ingresados
- Llama a los métodos del servicio `Restaurante`
- Mantiene el bucle principal hasta que el usuario selecciona "Salir"

---

## Uso del Constructor en la Clase Producto

```python
class Producto:
    def __init__(self, nombre, categoria, precio, disponible=True):
        self._nombre = None
        self._categoria = None
        self._precio = None
        self._disponible = disponible
        
        # Usar los setters para validación
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
```

El constructor:
1. Inicializa atributos privados
2. Utiliza los `setters` para validar los datos ingresados
3. Lanza excepciones si los datos no son válidos
4. Asegura que los objetos se crean en un estado consistente

**Ejemplo de uso:**
```python
# Crear producto desde datos del usuario
producto = Producto("Pizza Margherita", "Alimentos", "15.99")
# Si los datos no son válidos, el constructor lanza una excepción
```

---

## Uso de @property y @setter

Los decoradores `@property` y `@setter` permiten:
- **Acceso controlado** a los atributos privados
- **Validación** antes de aceptar nuevos valores
- **Encapsulación** de la lógica de negocio

**Ejemplo:**
```python
@property
def precio(self):
    """Obtiene el precio del producto."""
    return self._precio

@precio.setter
def precio(self, valor):
    """Establece el precio con validación."""
    try:
        precio_float = float(valor)
        if precio_float <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        self._precio = precio_float
    except ValueError as e:
        raise ValueError("El precio debe ser un número válido mayor que cero")
```

**Beneficios:**
- Los datos inválidos se rechazan en el momento de la asignación
- El código cliente no necesita hacer validaciones manuales
- Se facilita el mantenimiento futuro del código

---

## Uso de @dataclass en la Clase Cliente

El decorador `@dataclass` simplifica la creación de clases que almacenan datos:

```python
from dataclasses import dataclass

@dataclass
class Cliente:
    id_cliente: str
    nombre: str
    correo: str
```

**Ventajas:**
- Genera automáticamente el método `__init__`
- Genera automáticamente los métodos `__repr__` y `__eq__`
- Reduce significativamente el código boilerplate
- Mantiene la estructura limpia y legible

**Comparación:**
- **Sin @dataclass**: Requiere escribir constructor, setters, getters
- **Con @dataclass**: Solo declarar atributos con tipos

---

## Menú Interactivo

El programa presenta el siguiente menú:

```
==================================================
            SISTEMA DE RESTAURANTE
==================================================
1. Registrar producto
2. Listar productos
3. Buscar producto
--------------------------------------------------
4. Registrar cliente
5. Listar clientes
6. Buscar cliente
--------------------------------------------------
7. Salir
==================================================
```

### Opciones Disponibles:

1. **Registrar producto**: Solicita nombre, categoría y precio, luego crea un objeto `Producto` y lo almacena en el `Restaurante`
2. **Listar productos**: Muestra todos los productos registrados con su información completa
3. **Buscar producto**: Permite buscar por nombre o categoría
4. **Registrar cliente**: Solicita ID, nombre y correo, luego crea un objeto `Cliente` y lo almacena
5. **Listar clientes**: Muestra todos los clientes registrados
6. **Buscar cliente**: Permite buscar por ID o nombre
7. **Salir**: Termina la ejecución del programa

---

## Flujo de Creación de Objetos

El sistema implementa el siguiente flujo:

```
┌─────────────────┐
│  input()        │ ← Solicitud de datos al usuario
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│  Constructor del Modelo │ ← Creación del objeto con validación
└────────┬────────────────┘
         │
         ▼
┌──────────────────────┐
│  Objeto Creado       │ ← Producto o Cliente
└────────┬─────────────┘
         │
         ▼
┌──────────────────────────────┐
│  Registro en Restaurante     │ ← Almacenamiento en lista
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────┐
│  Listado o Búsqueda      │ ← Consulta de información
└──────────────────────────┘
```

Este flujo demuestra que:
- Los datos ingresados se transforman en objetos mediante constructores
- Los objetos se validan al momento de su creación
- Los objetos se almacenan centralizadamente en el servicio
- La información se puede consultar de múltiples formas

---

## Cómo Ejecutar el Sistema

1. **Navegar a la carpeta del proyecto:**
   ```bash
   cd restaurante_app
   ```

2. **Ejecutar el programa principal:**
   ```bash
   python main.py
   ```

3. **Interactuar con el menú:**
   - Seleccionar opciones ingresando números del 1 al 7
   - Seguir las instrucciones en pantalla
   - El programa continuará hasta que seleccione la opción 7

---

## Ejemplos de Uso

### Registrar un Producto
```
Seleccione una opción: 1
--- Registrar Nuevo Producto ---
Nombre del producto: Pizza Margherita
Categoría (ej: Bebidas, Alimentos, Postres): Alimentos
Precio del producto: 15.99
✓ Producto 'Pizza Margherita' registrado exitosamente.
```

### Buscar un Producto
```
Seleccione una opción: 3
--- Buscar Producto ---
1. Buscar por nombre
2. Buscar por categoría
Seleccione opción: 1
Ingrese nombre del producto: Pizza Margherita
✓ Producto encontrado:
  [ALIMENTOS] Pizza Margherita - $15.99 - Disponible
```

### Registrar un Cliente
```
Seleccione una opción: 4
--- Registrar Nuevo Cliente ---
ID del cliente: CLI001
Nombre del cliente: Juan Pérez
Correo del cliente: juan@example.com
✓ Cliente 'Juan Pérez' registrado exitosamente.
```

---

## Importancia de Crear Objetos a partir de Datos del Usuario

### 1. **Validación en Tiempo de Construcción**
Los datos se validan al crear el objeto, evitando estados inválidos:
```python
# Si el usuario ingresa un precio negativo:
producto = Producto("Pizza", "Alimentos", "-5")
# Lanza: ValueError: El precio debe ser mayor que cero
```

### 2. **Capas de Abstracción**
Separar la creación de datos (models) del almacenamiento (servicios) permite:
- Reutilizar lógica de validación
- Cambiar la forma de persistencia sin afectar los modelos
- Facilitar pruebas unitarias

### 3. **Mantenibilidad**
Si la validación cambia, se modifica en un solo lugar (el constructor/setter):
```python
# Cambiar: "precio mínimo de 1000"
@precio.setter
def precio(self, valor):
    precio_float = float(valor)
    if precio_float < 1000:  # Cambio centralizado
        raise ValueError("El precio mínimo es 1000")
    self._precio = precio_float
```

### 4. **Seguridad y Consistencia**
Los objetos garantizan que los datos están en un estado válido:
- Evita datos inconsistentes en la aplicación
- Facilita la implementación de reglas de negocio
- Previene errores difíciles de detectar

---

## Decisiones de Diseño

1. **Producto con constructor tradicional**: Permite mayor control y validación explícita
2. **Cliente con @dataclass**: Simplifica la gestión de datos sin validación compleja
3. **Restaurante como servicio centralizado**: Facilita la administración de múltiples objetos
4. **Búsqueda tanto por nombre como por categoría (productos)**: Proporciona flexibilidad al usuario
5. **Validación de ID único para clientes**: Evita duplicados en la base de datos

---

## Requisitos Cumplidos

✅ Estructura modular correcta (modelos, servicios, main)  
✅ Clase Producto con constructor `__init__` tradicional  
✅ Decoradores `@property` y `@setter` con validaciones  
✅ Validación de nombre, categoría y precio  
✅ Método `mostrar_informacion()` en Producto  
✅ Clase Cliente implementada con `@dataclass`  
✅ Clase Restaurante como servicio  
✅ Métodos para registrar, listar y buscar productos  
✅ Métodos para registrar, listar y buscar clientes  
✅ Menú interactivo ejecutable desde consola  
✅ Creación dinámica de objetos desde `input()`  
✅ Importaciones correctas entre módulos  
✅ Comentarios explicativos en el código  
✅ Sistema completamente funcional  

---

## Conclusión

Este sistema demuestra la aplicación práctica de conceptos fundamentales de POO en Python. La arquitectura modular permite que el código sea mantenible, escalable y fácil de entender. La separación entre modelos y servicios facilita cambios futuros y la reutilización de código.

La importancia de crear objetos a partir de datos del usuario radica en que garantiza la integridad de los datos desde su creación, facilita la implementación de reglas de negocio y mejora significativamente la mantenibilidad y seguridad de la aplicación.

