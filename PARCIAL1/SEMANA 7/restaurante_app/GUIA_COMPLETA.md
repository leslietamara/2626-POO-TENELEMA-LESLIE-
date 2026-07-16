# GUÍA DE USO DEL SISTEMA DE RESTAURANTE

## Cómo Ejecutar el Sistema

### Desde la terminal:
```bash
cd restaurante_app
python main.py
```

### El programa mostrará el menú:
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
Seleccione una opción:
```

---

## Ejemplos de Interacción

### Ejemplo 1: Registrar un Producto

```
Seleccione una opción: 1
--- Registrar Nuevo Producto ---
Nombre del producto: Pizza Margarita
Categoría (ej: Bebidas, Alimentos, Postres): Alimentos
Precio del producto: 25.50
✓ Producto 'Pizza Margarita' registrado exitosamente.
```

### Ejemplo 2: Listar Productos

```
Seleccione una opción: 2
--- Listado de Productos ---

Total de productos: 1

1. [ALIMENTOS] Pizza Margarita - $25.50 - Disponible
```

### Ejemplo 3: Buscar un Producto

```
Seleccione una opción: 3
--- Buscar Producto ---
1. Buscar por nombre
2. Buscar por categoría
Seleccione opción: 1
Ingrese nombre del producto: Pizza Margarita
✓ Producto encontrado:
  [ALIMENTOS] Pizza Margarita - $25.50 - Disponible
```

### Ejemplo 4: Registrar un Cliente

```
Seleccione una opción: 4
--- Registrar Nuevo Cliente ---
ID del cliente: C001
Nombre del cliente: Juan Pérez
Correo del cliente: juan.perez@email.com
✓ Cliente 'Juan Pérez' registrado exitosamente.
```

### Ejemplo 5: Listar Clientes

```
Seleccione una opción: 5
--- Listado de Clientes ---

Total de clientes: 1

1. [ID: C001] Juan Pérez - juan.perez@email.com
```

### Ejemplo 6: Buscar un Cliente

```
Seleccione una opción: 6
--- Buscar Cliente ---
1. Buscar por ID
2. Buscar por nombre
Seleccione opción: 1
Ingrese ID del cliente: C001
✓ Cliente encontrado:
  [ID: C001] Juan Pérez - juan.perez@email.com
```

---

## Validaciones Implementadas

### En la Clase Producto:

1. **Nombre no vacío**: 
   - Error si está vacío o solo contiene espacios

2. **Categoría no vacía**: 
   - Error si está vacía o solo contiene espacios

3. **Precio válido**: 
   - Error si es negativo o cero
   - Error si no es un número válido

### En la Clase Cliente:

1. **ID único**: 
   - Error si ya existe un cliente con el mismo ID

2. **Campos no vacíos**: 
   - Validación en el menú antes de crear el objeto

### Ejemplos de Validaciones:

#### Crear producto con nombre vacío:
```
Nombre del producto: 
Categoría: Alimentos
Precio: 10.00
✗ Error al registrar producto: El nombre del producto no puede estar vacío
```

#### Crear producto con precio negativo:
```
Nombre del producto: Pizza
Categoría: Alimentos
Precio: -10
✗ Error al registrar producto: El precio debe ser mayor que cero
```

#### Registrar cliente con ID duplicado:
```
ID del cliente: C001  (ya existe)
Nombre del cliente: Otro Cliente
Correo: otro@email.com
✗ Error al registrar cliente: Ya existe un cliente con el ID C001
```

---

## Estructura del Código

### archivo: modelos/producto.py
```python
class Producto:
    def __init__(self, nombre, categoria, precio, disponible=True):
        # Constructor que valida datos mediante setters
        
    @property
    def nombre(self):
        # Acceso controlado
        
    @nombre.setter
    def nombre(self, valor):
        # Validación: no vacío
        
    # Similar para categoria y precio
    
    def mostrar_informacion(self):
        # Retorna string con disponibilidad formateada
```

### archivo: modelos/cliente.py
```python
from dataclasses import dataclass

@dataclass
class Cliente:
    id_cliente: str
    nombre: str
    correo: str
    
    def mostrar_informacion(self):
        # Retorna información del cliente
```

### archivo: servicios/restaurante.py
```python
class Restaurante:
    def __init__(self, nombre):
        self.productos = []
        self.clientes = []
        
    # Métodos para productos:
    # - registrar_producto()
    # - listar_productos()
    # - buscar_producto_por_nombre()
    # - buscar_productos_por_categoria()
    
    # Métodos para clientes:
    # - registrar_cliente()
    # - listar_clientes()
    # - buscar_cliente_por_id()
    # - buscar_cliente_por_nombre()
```

### archivo: main.py
```python
def main():
    restaurante = Restaurante("Restaurant Express")
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            listar_productos(restaurante)
        # ... más opciones
        elif opcion == "7":
            break
```

---

## Pruebas Automatizadas

Se incluye un archivo `prueba.py` que prueba automáticamente todas las funciones:

```bash
python prueba.py
```

Este script verifica:
- ✓ Creación de productos válidos
- ✓ Validación de productos inválidos
- ✓ Listado de productos
- ✓ Búsqueda por nombre y categoría
- ✓ Modificación de atributos
- ✓ Creación de clientes con @dataclass
- ✓ Validación de IDs únicos
- ✓ Listado y búsqueda de clientes

---

## Conceptos POO Implementados

### 1. Constructor Tradicional (`__init__`)
- Inicializa atributos privados
- Valida datos mediante setters
- Garantiza objetos en estado válido

### 2. Decorador `@property`
- Acceso controlado a atributos
- Encapsulación de datos

### 3. Decorador `@setter`
- Modificación con validación
- Previene estados inválidos

### 4. Decorador `@dataclass`
- Genera automáticamente `__init__`
- Reduce código boilerplate
- Perfecto para objetos de datos simples

### 5. Arquitectura Modular
- Separación de responsabilidades
- Carpeta `modelos` para clases de datos
- Carpeta `servicios` para lógica de negocio
- Archivo `main.py` para interfaz de usuario

### 6. Encapsulación
- Atributos privados (con `_`)
- Acceso controlado mediante properties
- Validación centralizada

---

## Notas Importantes

1. **No se requiere conexión a base de datos**: Los datos se almacenan en memoria mientras se ejecuta el programa

2. **Los datos se pierden al salir**: El programa no persiste datos en archivos

3. **Validación robusta**: Todos los setters incluyen validaciones

4. **Menú intuitivo**: El programa solicita datos de forma clara y amigable

5. **Mensajes de error útiles**: Se especifica qué validación falló

6. **Búsqueda flexible**: Se puede buscar productos por nombre o categoría, clientes por ID o nombre

---

## Restricciones Respetadas

✅ No es una copia literal del proyecto docente  
✅ No usa interfaces gráficas  
✅ No usa bases de datos  
✅ Estructura modular correcta  
✅ Nombres descriptivos  
✅ Validaciones implementadas  
✅ Comentarios explicativos  
✅ Objetos creados dinámicamente desde `input()`  
✅ Usa `@property`, `@setter` y `@dataclass`  
✅ Menú interactivo funcional  

---

## Próximos Pasos (Opcionales)

El sistema podría extenderse con:
- Persistencia en archivo JSON/CSV
- Búsqueda más avanzada
- Edición de datos registrados
- Eliminación de productos/clientes
- Integración con base de datos
- Interfaz gráfica
- API REST

Pero respeta las restricciones de la tarea original.

