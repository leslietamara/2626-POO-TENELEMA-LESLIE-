# EVIDENCIA DE EJECUCIÓN - SEMANA 6

**Proyecto**: Sistema de Gestión de Restaurante  
**Fecha de Ejecución**: 2026-06-23  
**Programa**: `restaurante_app/main.py`

---

## Ejecución Exitosa ✅

El programa se ejecutó sin errores. A continuación se muestra la salida completa:

```
======================================================================
INICIALIZANDO SISTEMA DE GESTIÓN DE RESTAURANTE
======================================================================


[1] AGREGANDO PRODUCTOS AL MENÚ...

✓ Producto 'Tabla de Quesos y Embutidos' agregado al menú.
✓ Producto 'Camarones al Ajillo' agregado al menú.
✓ Producto 'Filete de Salmón a la Mantequilla' agregado al menú.
✓ Producto 'Pechuga de Pollo Rellena' agregado al menú.
✓ Producto 'Tiramisú Casero' agregado al menú.
✓ Producto 'Flan de Huevo' agregado al menú.
✓ Producto 'Vino Tinto Reserva' agregado al menú.
✓ Producto 'Agua Mineral' agregado al menú.

[2] REGISTRANDO CLIENTES...

✓ Cliente 'María García López' registrado en el sistema.
✓ Cliente 'Juan Rodríguez Pérez' registrado en el sistema.
✓ Cliente 'Ana Martínez López' registrado en el sistema.

[3] CREANDO ÓRDENES...

✓ Orden #1 creada para María García López. Total: $71.50
✓ Orden #2 creada para Juan Rodríguez Pérez. Total: $37.75
✓ Orden #3 creada para Ana Martínez López. Total: $25.00

[4] MOSTRANDO INFORMACIÓN DEL SISTEMA...


======================================================================
                     INFORMACIÓN DEL RESTAURANTE                      
======================================================================
Nombre: La Buena Mesa
Dirección: Calle Principal 123, Centro
Teléfono: +34 912345678
Productos en menú: 8
Clientes registrados: 3
Órdenes realizadas: 3
======================================================================

======================================================================
                         MENÚ DEL RESTAURANTE                         
                            La Buena Mesa                             
======================================================================

--- ENTRADA ---
  • Tabla de Quesos y Embutidos ($15.50) - Selección variada de quesos y jamones ibéricos
  • Camarones al Ajillo ($12.00) - Camarones frescos al ajillo y limón

--- PLATO PRINCIPAL ---
  • Filete de Salmón a la Mantequilla ($22.50) - Salmón fresco con salsa de mantequilla y limón
  • Pechuga de Pollo Rellena ($18.75) - Pollo relleno de jamón y queso, acompañado de ensalada

--- POSTRE ---
  • Tiramisú Casero ($8.50) - Tradicional tiramisú italiano preparado diariamente
  • Flan de Huevo ($7.00) - Flan cremoso con caramelo

--- BEBIDA ---
  • Vino Tinto Reserva ($25.00) - Vino de la región, cosecha 2018
  • Agua Mineral ($2.50) - Agua mineral sin gas

======================================================================

======================================================================
                         CLIENTES REGISTRADOS                         
======================================================================

  Cliente: María García López
  Email: maria.garcia@email.com
  Teléfono: +34 612345678
  Dirección: Av. España 45, Madrid
  Órdenes realizadas: 1

  Cliente: Juan Rodríguez Pérez
  Email: juan.rodriguez@email.com
  Teléfono: +34 623456789
  Dirección: Calle Mayor 12, Barcelona
  Órdenes realizadas: 1

  Cliente: Ana Martínez López
  Email: ana.martinez@email.com
  Teléfono: +34 634567890
  Dirección: Plaza Central 7, Valencia
  Órdenes realizadas: 1

======================================================================

======================================================================
                         HISTORIAL DE ÓRDENES                         
======================================================================

Orden #1
  Cliente: María García López
  Productos: Tabla de Quesos y Embutidos, Filete de Salmón a la Mantequilla, Tiramisú Casero, Vino Tinto Reserva
  Total: $71.50

Orden #2
  Cliente: Juan Rodríguez Pérez
  Productos: Camarones al Ajillo, Pechuga de Pollo Rellena, Flan de Huevo
  Total: $37.75

Orden #3
  Cliente: Ana Martínez López
  Productos: Filete de Salmón a la Mantequilla, Agua Mineral
  Total: $25.00

======================================================================

======================================================================
DETALLES DE UN PRODUCTO ESPECÍFICO
======================================================================

  Producto: Filete de Salmón a la Mantequilla
  Descripción: Salmón fresco con salsa de mantequilla y limón
  Precio: $22.50
  Categoría: Plato Principal

======================================================================

======================================================================
SISTEMA EJECUTADO CORRECTAMENTE
======================================================================
```

---

## ✅ Verificación de Resultados

### 1. Productos Agregados Correctamente
- ✅ **Cantidad esperada**: 8 productos
- ✅ **Cantidad real**: 8 productos confirma con "Productos en menú: 8"
- ✅ **Categorías**: Entrada, Plato Principal, Postre, Bebida
- ✅ **Precios**: Todos los precios mostrados en formato decimal (float)
- ✅ **Descripciones**: Todas las descripciones detalladas

### 2. Clientes Registrados Correctamente
- ✅ **Cantidad esperada**: 3 clientes
- ✅ **Cantidad real**: 3 clientes confirma con "Clientes registrados: 3"
- ✅ **Información completa**: Nombre, email, teléfono, dirección
- ✅ **Historial de órdenes**: Cada cliente muestra sus órdenes

### 3. Órdenes Creadas y Gestionadas
- ✅ **Cantidad esperada**: 3 órdenes
- ✅ **Cantidad real**: 3 órdenes confirma con "Órdenes realizadas: 3"
- ✅ **Cálculo de totales correcto**:
  - Orden #1: $15.50 + $22.50 + $8.50 + $25.00 = $71.50 ✅
  - Orden #2: $12.00 + $18.75 + $7.00 = $37.75 ✅
  - Orden #3: $22.50 + $2.50 = $25.00 ✅
- ✅ **Productos en cada orden**: Listados correctamente

### 4. Métodos de Presentación Funcionando
- ✅ `restaurante.mostrar_informacion_restaurante()` - Funciona correctamente
- ✅ `restaurante.mostrar_menu()` - Agrupa por categorías correctamente
- ✅ `restaurante.mostrar_clientes()` - Lista clientes con detalles
- ✅ `restaurante.mostrar_ordenes()` - Muestra historial completo
- ✅ `producto.mostrar_detalles()` - Muestra detalles de producto específico

### 5. En Estado General del Sistema
- ✅ **Estado de ejecución**: SIN ERRORES
- ✅ **Importaciones**: Todas funcionales
- ✅ **Objetos creados**: 12 objetos totales (8 Productos + 3 Clientes + 1 Restaurante)
- ✅ **Listas gestionadas**: Todos los datos se almacenan y recuperan correctamente
- ✅ **Salida formateada**: Presentación clara y profesional

---

## 📋 Checklist de Ejecución

| Elemento | Estado | Observación |
|----------|--------|-------------|
| Inicio del programa | ✅ | Ejecución sin errores |
| Importaciones | ✅ | Todas las clases importadas correctamente |
| Instancia Restaurante | ✅ | Creada correctamente |
| 8 Productos creados | ✅ | Con nombres, descripciones y precios |
| 3 Clientes creados | ✅ | Con datos de contacto completos |
| Productos agregados a lista | ✅ | 8/8 productos en `restaurante.productos` |
| Clientes registrados en lista | ✅ | 3/3 clientes en `restaurante.clientes` |
| 3 Órdenes creadas | ✅ | Con cálculos de totales correctos |
| Órdenes en lista | ✅ | 3/3 órdenes en `restaurante.ordenes` |
| Historial de cliente | ✅ | Cada cliente tiene sus órdenes |
| Método __str__() Producto | ✅ | Funciona en mostrar_menu() |
| Método __str__() Cliente | ✅ | Funciona en mostrar_clientes() |
| Método obtener_informacion() | ✅ | Retorna diccionarios correctamente |
| Método mostrar_detalles() | ✅ | Formatea información correctamente |
| Presentación final | ✅ | Clara y profesional |
| Mensaje de finalización | ✅ | "SISTEMA EJECUTADO CORRECTAMENTE" |

---

## 🔍 Análisis de Tipos de Datos

### Tipos str (cadenas)
- ✅ `nombre`: "La Buena Mesa", "Tabla de Quesos", "María García López", etc.
- ✅ `descripcion`: "Selección variada de quesos y jamones ibéricos", etc.
- ✅ `categoria`: "Entrada", "Plato Principal", "Postre", "Bebida"
- ✅ `email`: "maria.garcia@email.com", etc.
- ✅ `telefono`: "+34 612345678", etc.
- ✅ `direccion`: "Av. España 45, Madrid", etc.

### Tipos float (decimales)
- ✅ `precio`: 15.50, 12.00, 22.50, 18.75, 8.50, 7.00, 25.00, 2.50
- ✅ `total`: 71.50, 37.75, 25.00 (calculados correctamente)

### Tipos int (enteros)
- ✅ `numero_orden`: 1, 2, 3
- ✅ `contador_ordenes`: 0, 1, 2, 3
- ✅ `len()` de listas: 8, 3, 3, 1

### Tipos list (listas)
- ✅ `productos`: [Producto, Producto, ...] (8 elementos)
- ✅ `clientes`: [Cliente, Cliente, Cliente] (3 elementos)
- ✅ `ordenes`: [dict, dict, dict] (3 elementos)
- ✅ `ordenes` (Cliente): [1, 2, 3] (IDs de órdenes)

### Tipos dict (diccionarios)
- ✅ `orden`: {"numero": 1, "cliente": "...", "productos": [...], "total": 71.50}
- ✅ `obtener_informacion()`: {"nombre": "...", "email": "...", "telefono": "...", ...}

---

## 🎯 Conclusión de Ejecución

✅ **EL PROGRAMA FUNCIONA CORRECTAMENTE**

Todos los requisitos de ejecución han sido satisfechos:
1. ✅ El programa se ejecuta sin errores
2. ✅ Los objetos se crean correctamente
3. ✅ Las listas administran los datos correctamente
4. ✅ Los métodos funcionan según lo esperado
5. ✅ La presentación es clara y profesional
6. ✅ Los cálculos (totales de órdenes) son correctos
7. ✅ Todos los tipos de datos se utilizan apropiadamente
8. ✅ El flujo del programa es lógico y coherente

---

**Ejecución Verificada**: 2026-06-23  
**Estatus**: ✅ **APROBADO**

