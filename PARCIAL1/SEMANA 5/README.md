# Sistema de Gestión de Restaurante - SEMANA 5

## 📖 Descripción del Proyecto

Este proyecto implementa un **Sistema de Gestión de Restaurante** utilizando **Programación Orientada a Objetos (POO)** en Python. El sistema permite administrar productos (menú), clientes y órdenes de un restaurante de manera organizada.

---

## 📁 Estructura del Proyecto

```
restaurante_app/
├── __init__.py                  # Inicialización del paquete
├── main.py                      # Punto de arranque del programa
├── modelos/
│   ├── __init__.py              # Inicialización del paquete modelos
│   ├── producto.py              # Clase Producto
│   └── cliente.py               # Clase Cliente
└── servicios/
    ├── __init__.py              # Inicialización del paquete servicios
    └── restaurante.py           # Clase Restaurante
```

---

## 🎯 Componentes Principales

### 1. **Clase Producto** (`modelos/producto.py`)
Representa un producto disponible en el restaurante.

**Atributos:**
- `nombre`: Nombre del producto
- `descripcion`: Descripción breve del producto
- `precio`: Precio en moneda local
- `categoria`: Categoría (Entrada, Plato Principal, Postre, Bebida)

**Métodos:**
- `__init__()`: Constructor
- `__str__()`: Representación en texto
- `obtener_informacion()`: Retorna información como diccionario
- `mostrar_detalles()`: Muestra información formateada

---

### 2. **Clase Cliente** (`modelos/cliente.py`)
Representa a un cliente del restaurante.

**Atributos:**
- `nombre`: Nombre completo del cliente
- `email`: Correo electrónico
- `telefono`: Número de teléfono
- `direccion`: Dirección del cliente
- `ordenes`: Lista de órdenes realizadas

**Métodos:**
- `__init__()`: Constructor
- `__str__()`: Representación en texto
- `obtener_informacion()`: Retorna información como diccionario
- `agregar_orden()`: Agrega una orden al historial
- `mostrar_detalles()`: Muestra información formateada

---

### 3. **Clase Restaurante** (`servicios/restaurante.py`)
Gestiona todas las operaciones principales del restaurante.

**Atributos:**
- `nombre`: Nombre del restaurante
- `direccion`: Dirección física
- `telefono`: Teléfono de contacto
- `productos`: Lista de productos en el menú
- `clientes`: Lista de clientes registrados
- `ordenes`: Historial de órdenes realizadas
- `contador_ordenes`: Control de numeración de órdenes

**Métodos:**
- `__init__()`: Constructor
- `agregar_producto()`: Agrega un producto al menú
- `registrar_cliente()`: Registra un cliente en el sistema
- `crear_orden()`: Crea una nueva orden
- `mostrar_menu()`: Muestra el menú organizado por categorías
- `mostrar_clientes()`: Lista todos los clientes registrados
- `mostrar_ordenes()`: Muestra el historial de órdenes
- `mostrar_informacion_restaurante()`: Muestra información general

---

## 🚀 Cómo Ejecutar

### Requisitos previos:
- Python 3.7+ instalado
- Terminal/CMD disponible

### Pasos:

1. **Navega a la carpeta del proyecto**
```bash
cd restaurante_app
```

2. **Ejecuta el programa**
```bash
python main.py
```

3. **Observa la salida**
El programa mostrará:
- Confirmación de productos agregados (8 productos)
- Confirmación de clientes registrados (3 clientes)
- Confirmación de órdenes creadas (3 órdenes)
- Información del restaurante
- Menú completo organizado por categorías
- Lista de clientes con detalles
- Historial de órdenes con totales
- Detalles de un producto específico

---

## 📊 Demostración del Sistema

### Productos Agregados (8 total)
- **Entradas**: 2 productos
  - Tabla de Quesos y Embutidos ($15.50)
  - Camarones al Ajillo ($12.00)
- **Platos Principales**: 2 productos
  - Filete de Salmón a la Mantequilla ($22.50)
  - Pechuga de Pollo Rellena ($18.75)
- **Postres**: 2 productos
  - Tiramisú Casero ($8.50)
  - Flan de Huevo ($7.00)
- **Bebidas**: 2 productos
  - Vino Tinto Reserva ($25.00)
  - Agua Mineral ($2.50)

### Clientes Registrados (3 total)
1. María García López - maria.garcia@email.com
2. Juan Rodríguez Pérez - juan.rodriguez@email.com
3. Ana Martínez López - ana.martinez@email.com

### Órdenes Creadas (3 total)
- **Orden #1** - María: $71.50
- **Orden #2** - Juan: $37.75
- **Orden #3** - Ana: $25.00

---

## 🎓 Conceptos de POO Utilizados

1. **Encapsulación**: Datos y métodos organizados en clases
2. **Abstracción**: Las clases abstraen conceptos del mundo real
3. **Modularidad**: Código dividido en módulos y paquetes
4. **Reutilización**: Las clases pueden instanciarse múltiples veces
5. **Métodos especiales**: Uso de `__init__()` y `__str__()`

---

## 💡 Características Implementadas

✅ Constructor `__init__()` en todas las clases  
✅ Atributos pertinentes con tipos de datos adecuados  
✅ Método `__str__()` para representación en texto  
✅ Métodos de gestión (agregar, registrar, mostrar)  
✅ Importaciones correctas entre módulos  
✅ Creación de múltiples objetos  
✅ Gestión de listas para almacenar datos  
✅ Presentación formateada de información  
✅ Comentarios explicativos en el código  

---

## 📝 Notas Adicionales

- El programa es completamente funcional y ejecutable
- El código sigue principios de POO
- La estructura permite fácil extensión futura
- Es posible modificar los datos (productos, clientes, órdenes) para personalizar el sistema

---

## 🔄 Cómo Extender el Proyecto

Puedes agregar nuevas funcionalidades:
- Buscar productos por categoría
- Filtrar órdenes por cliente
- Calcular estadísticas (orden promedio, cliente frecuente, etc.)
- Guardar datos en archivos
- Eliminar o modificar productos y clientes

---

**Autor**: Sistema de Gestión de Restaurante  
**Lenguaje**: Python 3  
**Paradigma**: Programación Orientada a Objetos (POO)  
**Semana**: 5

