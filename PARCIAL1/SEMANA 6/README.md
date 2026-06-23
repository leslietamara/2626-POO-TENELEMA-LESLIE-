# Sistema de Gestión de Restaurante - SEMANA 6

## Descripción del Proyecto

Este proyecto implementa un **Sistema de Gestión de Restaurante** utilizando **Programación Orientada a Objetos (POO)** en Python. El sistema permite administrar productos (menú), clientes y órdenes de un restaurante de manera organizada y eficiente.

---

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py              # Paquete de inicialización de modelos
│   ├── producto.py              # Clase Producto
│   └── cliente.py               # Clase Cliente
├── servicios/
│   ├── __init__.py              # Paquete de inicialización de servicios
│   └── restaurante.py           # Clase Restaurante
├── main.py                      # Punto de arranque del programa
└── README.md                    # Este archivo (documentación)
```

---

## Requisitos Cumplidos

### 1. Estructura del Proyecto ✅
- ✅ Estructura de carpetas organizadas en `modelos/`, `servicios/` y `main.py`
- ✅ Separación clara de responsabilidades
- ✅ Nombres descriptivos para carpetas y archivos

### 2. Implementación de Clases ✅

#### **Clase Producto** (`modelos/producto.py`)
- **Responsabilidad**: Representa un producto del restaurante
- **Atributos**:
  - `nombre: str` - Nombre del producto
  - `descripcion: str` - Descripción breve del producto
  - `precio: float` - Precio del producto en moneda local
  - `categoria: str` - Categoría (Entrada, Plato Principal, Postre, Bebida)
- **Métodos principales**:
  - `__init__()` - Constructor con anotaciones de tipo
  - `__str__()` - Representación en texto del producto
  - `obtener_informacion()` - Retorna información como diccionario
  - `mostrar_detalles()` - Muestra información formateada en consola

#### **Clase Cliente** (`modelos/cliente.py`)
- **Responsabilidad**: Representa a un cliente del restaurante
- **Atributos**:
  - `nombre: str` - Nombre completo del cliente
  - `email: str` - Correo electrónico del cliente
  - `telefono: str` - Número de teléfono del cliente
  - `direccion: str` - Dirección del cliente (opcional)
  - `ordenes: list` - Lista de órdenes realizadas por el cliente
- **Métodos principales**:
  - `__init__()` - Constructor con anotaciones de tipo
  - `__str__()` - Representación en texto del cliente
  - `obtener_informacion()` - Retorna información como diccionario
  - `agregar_orden()` - Agrega una orden al historial del cliente
  - `mostrar_detalles()` - Muestra información formateada en consola

#### **Clase Restaurante** (`servicios/restaurante.py`)
- **Responsabilidad**: Gestiona todas las operaciones del restaurante
- **Atributos**:
  - `nombre: str` - Nombre del restaurante
  - `direccion: str` - Dirección física del restaurante
  - `telefono: str` - Teléfono de contacto del restaurante
  - `productos: list` - Lista de productos disponibles en el menú
  - `clientes: list` - Lista de clientes registrados
  - `ordenes: list` - Historial de órdenes realizadas
  - `contador_ordenes: int` - Contador para generar IDs de órdenes
- **Métodos principales**:
  - `__init__()` - Constructor con anotaciones de tipo
  - `agregar_producto()` - Agrega un producto al menú
  - `registrar_cliente()` - Registra un cliente en el sistema
  - `crear_orden()` - Crea una nueva orden para un cliente
  - `mostrar_menu()` - Muestra el menú organizado por categorías
  - `mostrar_clientes()` - Lista todos los clientes registrados
  - `mostrar_ordenes()` - Muestra el historial de órdenes
  - `mostrar_informacion_restaurante()` - Muestra información general

### 3. Convenciones de Nombres ✅
- ✅ **PascalCase** para clases: `Producto`, `Cliente`, `Restaurante`
- ✅ **snake_case** para variables, atributos, métodos y archivos: `nombre_cliente`, `obtener_informacion()`, `cliente.py`
- ✅ Identificadores descriptivos y significativos en todo el código

### 4. Tipos de Datos Utilizados ✅
- ✅ **str** (cadenas): nombres, descripciones, categorías, emails
- ✅ **float** (decimales): precios de productos y totales de órdenes
- ✅ **int** (enteros): IDs de órdenes, contador de órdenes
- ✅ **list** (listas): colecciones de productos, clientes, órdenes
- ✅ **dict** (diccionarios): información de órdenes y detalles

### 5. Anotaciones de Tipo ✅
- ✅ Anotaciones en constructores: `def __init__(self, nombre: str, ...)`
- ✅ Anotaciones en atributos: `self.nombre: str = nombre`
- ✅ Anotaciones en retornos: `-> None`, `-> str`, `-> dict`, `-> int`

### 6. Método Especial __str__() ✅
- ✅ Implementado en `Producto`: Retorna descripción formateada con nombre y precio
- ✅ Implementado en `Cliente`: Retorna nombre y email en formato legible

### 7. Importaciones Correctas ✅
- ✅ `main.py` importa correctamente desde `modelos.producto` y `modelos.cliente`
- ✅ `main.py` importa correctamente desde `servicios.restaurante`
- ✅ Uso de importaciones relativas apropiadas

### 8. Creación de Objetos en main.py ✅
- ✅ Se crean **8 productos** (Entradas, Platos Principales, Postres, Bebidas)
- ✅ Se crean **3 clientes** (María García López, Juan Rodríguez Pérez, Ana Martínez López)
- ✅ Se crean **3 órdenes** con diferentes combinaciones de productos

### 9. Gestión de Objetos ✅
- ✅ Los productos se agregan a la lista `restaurante.productos`
- ✅ Los clientes se registran en la lista `restaurante.clientes`
- ✅ Las órdenes se almacenan en la lista `restaurante.ordenes`
- ✅ Cada cliente mantiene su historial de órdenes

### 10. Presentación de Información ✅
- ✅ Información del restaurante mostrada de forma organizada
- ✅ Menú agrupado por categorías
- ✅ Lista de clientes con detalles completos
- ✅ Historial de órdenes con totales
- ✅ Detalles de productos específicos

### 11. Comentarios Explicativos ✅
- ✅ Comentarios al inicio de archivos indicando su responsabilidad
- ✅ Docstrings en clases y métodos
- ✅ Comentarios en secciones principales del código
- ✅ Explicación de variables complejas

---

## Características Implementadas

✅ **Constructor `__init__()`**: Todas las clases tienen constructor que inicializa sus atributos  
✅ **Atributos Pertinentes**: Cada clase contiene atributos relevantes al contexto del restaurante  
✅ **Método `__str__()`**: Implementado en Producto y Cliente para representación en texto  
✅ **Métodos de Gestión**: Métodos para crear, agregar, mostrar y gestionar información  
✅ **Importaciones Correctas**: El archivo main.py importa correctamente las clases  
✅ **Creación de Objetos**: Se crean múltiples instancias de cada modelo  
✅ **Gestión de Listas**: Uso de listas para almacenar y gestionar objetos  
✅ **Anotaciones de Tipo**: Type hints en métodos y atributos  
✅ **Convenciones PEP 8**: Aplicadas en todo el código  
✅ **Demostración Completa**: El programa ejecuta todas las operaciones correctamente  

---

## Cómo Ejecutar el Programa

### Opción 1: Desde la carpeta del proyecto
```bash
cd restaurante_app
python main.py
```

### Opción 2: Desde la ruta completa (Windows)
```powershell
cd "C:\Users\TAMARA\UEA\2626-POO-TENELEMA-LESLIE-\PARCIAL1\SEMANA 6\restaurante_app"
python main.py
```

---

## Salida Esperada

El programa mostrará:

1. **Confirmación de productos agregados** al menú (8 productos)
2. **Confirmación de clientes registrados** en el sistema (3 clientes)
3. **Confirmación de órdenes creadas** con sus totales (3 órdenes)
4. **Información general del restaurante**:
   - Nombre, dirección, teléfono
   - Conteo de productos, clientes y órdenes
5. **Menú completo** organizado por categorías
6. **Lista de clientes registrados** con información de contacto y órdenes
7. **Historial de órdenes** con detalles y totales
8. **Detalles de un producto específico**

---

## Demostración del Sistema

### [1] Productos Agregados (8 total)
- 2 Entradas: Tabla de Quesos, Camarones al Ajillo
- 2 Platos Principales: Salmón a la Mantequilla, Pechuga de Pollo Rellena
- 2 Postres: Tiramisú Casero, Flan de Huevo
- 2 Bebidas: Vino Tinto Reserva, Agua Mineral

### [2] Clientes Registrados (3 total)
- María García López - maria.garcia@email.com
- Juan Rodríguez Pérez - juan.rodriguez@email.com
- Ana Martínez López - ana.martinez@email.com

### [3] Órdenes Creadas (3 total)
- **Orden #1** - María: Entrada + Plato + Postre + Bebida = $71.50
- **Orden #2** - Juan: Entrada + Plato + Postre = $37.75
- **Orden #3** - Ana: Plato + Bebida = $25.00

---

## Conceptos de POO Utilizados

1. **Encapsulación**: Datos y métodos organizados en clases
2. **Abstracción**: Las clases abstraen conceptos del mundo real
3. **Modularidad**: Código dividido en módulos y paquetes
4. **Reutilización**: Las clases pueden instanciarse múltiples veces
5. **Métodos Especiales**: Uso de `__init__()` y `__str__()`
6. **Composición**: La clase Restaurante utiliza objetos Producto y Cliente
7. **Type Hints**: Anotaciones de tipo para mayor claridad

---

## Restricciones Respetadas

- ✅ Código original (no copiado del ejemplo docente)
- ✅ Código comprendido y bien estructurado
- ✅ Sin interfaces gráficas ni menús interactivos
- ✅ Nombres descriptivos (sin x, dato, objeto, clase1, etc.)
- ✅ Cumplimiento completo de requisitos técnicos

---

## Notas Finales

- El programa es completamente funcional y ejecutable
- El código sigue principios sólidos de POO
- La estructura permite fácil extensión futura
- Es posible agregar nuevas funcionalidades sin modificar la estructura base
- Todos los requisitos mínimos han sido cumplidos exitosamente

---

**Autor**: Tenelema Leslie  
**Lenguaje**: Python 3  
**Paradigma**: Programación Orientada a Objetos (POO)  
**Semana**: 6  
**Fecha**: 2026-06-23

