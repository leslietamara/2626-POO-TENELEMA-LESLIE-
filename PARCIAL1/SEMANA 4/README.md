# Sistema de Gestión de Restaurante

## Descripción del Proyecto

Este proyecto implementa un sistema de gestión de restaurante utilizando **Programación Orientada a Objetos (POO)** en Python. El sistema permite administrar productos (menú), clientes y órdenes de un restaurante.

---

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py          # Clase Producto
│   └── cliente.py           # Clase Cliente
├── servicios/
│   ├── __init__.py
│   └── restaurante.py       # Clase Restaurante
├── main.py                  # Punto de arranque del programa
└── README.md                # Este archivo
```

---

## Descripción de las Clases

### 1. **Clase Producto** (`modelos/producto.py`)

Representa un producto disponible en el restaurante.

**Atributos:**
- `nombre`: Nombre del producto
- `descripcion`: Descripción breve
- `precio`: Precio en moneda local
- `categoria`: Categoría (Entrada, Plato Principal, Postre, Bebida)

**Métodos principales:**
- `__init__()`: Constructor
- `__str__()`: Representación en texto
- `obtener_informacion()`: Retorna información como diccionario
- `mostrar_detalles()`: Muestra información formateada en consola

---

### 2. **Clase Cliente** (`modelos/cliente.py`)

Representa a un cliente del restaurante.

**Atributos:**
- `nombre`: Nombre completo del cliente
- `email`: Correo electrónico
- `telefono`: Número de teléfono
- `direccion`: Dirección del cliente (opcional)
- `ordenes`: Lista de órdenes realizadas

**Métodos principales:**
- `__init__()`: Constructor
- `__str__()`: Representación en texto
- `obtener_informacion()`: Retorna información como diccionario
- `agregar_orden()`: Agrega una orden al historial
- `mostrar_detalles()`: Muestra información formateada en consola

---

### 3. **Clase Restaurante** (`servicios/restaurante.py`)

Gestiona todas las operaciones principales del restaurante.

**Atributos:**
- `nombre`: Nombre del restaurante
- `direccion`: Dirección física
- `telefono`: Teléfono de contacto
- `productos`: Lista de productos en el menú
- `clientes`: Lista de clientes registrados
- `ordenes`: Historial de órdenes
- `contador_ordenes`: Control de numeración de órdenes

**Métodos principales:**
- `__init__()`: Constructor
- `agregar_producto()`: Agrega un producto al menú
- `registrar_cliente()`: Registra un cliente en el sistema
- `crear_orden()`: Crea una nueva orden
- `mostrar_menu()`: Muestra el menú organizado por categorías
- `mostrar_clientes()`: Lista todos los clientes registrados
- `mostrar_ordenes()`: Muestra el historial de órdenes
- `mostrar_informacion_restaurante()`: Muestra información general

---

## Características Implementadas

✅ **Constructor `__init__()`**: Todas las clases tienen constructor que inicializa sus atributos

✅ **Atributos Pertinentes**: Cada clase contiene atributos relevantes según el contexto del restaurante

✅ **Método `__str__()`**: Las clases Producto y Cliente implementan representación en texto

✅ **Métodos de Gestión**: Métodos para crear, agregar y mostrar información

✅ **Importaciones Correctas**: El archivo main.py importa correctamente las clases de los módulos

✅ **Creación de Objetos**: Se crean múltiples instancias de cada clase en main.py

✅ **Métodos Específicos**: Cada clase tiene métodos específicos para su funcionalidad

✅ **Comentarios**: El código incluye comentarios que explican las partes principales

✅ **Demostración Completa**: El programa main.py ejecuta la demostración del sistema

---

## Ejemplo de Uso

### Ejecutar el programa:

```bash
cd restaurante_app
python main.py
```

### Salida esperada:

El programa mostrará:

1. **Confirmación de productos agregados** al menú
2. **Confirmación de clientes registrados** en el sistema
3. **Confirmación de órdenes creadas** con sus totales
4. **Información del restaurante**: nombre, dirección, teléfono, conteos
5. **Menú completo**: productos organizados por categoría
6. **Lista de clientes registrados**: con información de contacto
7. **Historial de órdenes**: con detalles y totales
8. **Detalles de un producto específico**: ejemplo del método mostrar_detalles()

---

## Demostración del Sistema

El archivo `main.py` implementa una demostración completa que:

### [1] Crea 8 productos en el menú:
- 2 Entradas
- 2 Platos Principales
- 2 Postres
- 2 Bebidas

### [2] Registra 3 clientes:
- María García López
- Juan Rodríguez Pérez
- Ana Martínez López

### [3] Crea 3 órdenes:
- Orden #1: María (Entrada + Plato + Postre + Bebida = $71.50)
- Orden #2: Juan (Entrada + Plato + Postre = $37.75)
- Orden #3: Ana (Plato + Bebida = $25.00)

### [4] Muestra toda la información:
- Información general del restaurante
- Menú del restaurante
- Clientes registrados
- Historial de órdenes
- Detalles de un producto

---

## Conceptos de POO Utilizados

1. **Encapsulación**: Los datos y métodos están organizados en clases
2. **Abstracción**: Las clases abstraen conceptos del mundo real (Producto, Cliente, Restaurante)
3. **Modularidad**: El código está dividido en módulos y paquetes
4. **Reutilización**: Las clases pueden instanciarse múltiples veces
5. **Métodos especiales**: Uso de `__init__()` y `__str__()`
6. **Composición**: La clase Restaurante utiliza objetos Producto y Cliente

---

## Requisitos Cumplidos

| Requisito | Estado | Observaciones |
|-----------|--------|--------------|
| Estructura de carpetas | ✅ | restaurante_app/modelos/, servicios/, main.py |
| Clase Producto | ✅ | modelos/producto.py |
| Clase Cliente | ✅ | modelos/cliente.py |
| Clase Restaurante | ✅ | servicios/restaurante.py |
| Constructor __init__() | ✅ | Presente en las tres clases |
| Atributos pertinentes | ✅ | Apropiados al contexto del restaurante |
| Métodos de gestión | ✅ | Múltiples métodos en cada clase |
| Método __str__() | ✅ | Implementado en Producto y Cliente |
| Importaciones | ✅ | Correctas en main.py |
| Creación de objetos | ✅ | 8 productos, 3 clientes en main.py |
| Demostración funcional | ✅ | Completa y ordenada |
| Comentarios explicativos | ✅ | Presentes en todo el código |

---

## Notas Adicionales

- El programa es completamente funcional y ejecutable
- El código seguir principios de la POO
- La estructura permite fácil extensión futura
- Es posible agregar nuevas funcionalidades sin modificar la estructura base

---

**Autor**: Sistema de Gestión de Restaurante  
**Lenguaje**: Python 3  
**Paradigma**: Programación Orientada a Objetos (POO)

