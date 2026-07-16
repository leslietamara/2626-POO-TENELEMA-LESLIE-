# Tarea Semana 8 - Restaurante App

**Nombre del estudiante:** [Tu Nombre Completo]

## Descripción General

Versión mejorada del sistema `restaurante_app` para practicar y **aprender de forma interactiva** los principios SOLID (SRP, OCP, LSP). 

El sistema permite:
- **Registrar y listar productos, bebidas y clientes** mediante un menú por consola
- **Aprender principios SOLID de manera didáctica** con explicaciones contextualizadas en el código del restaurante
- **Explorar cómo cada principio se aplica** en clases reales del proyecto

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
├── main.py
├── explicaciones.py
└── prueba_solid.py
```

## Responsabilidad de cada clase

- **`Producto`** (modelos/producto.py): Representa datos comunes de un producto y define `mostrar_informacion()`.
- **`Bebida`** (modelos/bebida.py): Hereda de `Producto` e incorpora atributos propios (tamaño, envase). Sobrescribe `mostrar_informacion()`.
- **`Cliente`** (modelos/cliente.py): Representa información de un cliente. Implementa `mostrar_informacion()`.
- **`Restaurante`** (servicios/restaurante.py): Servicio que administra colecciones, registra y lista productos y clientes. Valida duplicados.
- **`explicaciones.py`**: Módulo educativo con explicaciones interactivas sobre SRP, OCP y LSP.

## Principios SOLID Aplicados

### S — Responsabilidad Única (SRP)
- Cada clase tiene **UNA única responsabilidad**:
  - `Producto` y `Bebida` → solo representan datos
  - `Cliente` → solo representa un cliente
  - `Restaurante` → solo administra colecciones y validaciones
  - `main.py` → solo maneja interacción por consola
  
**Ventaja:** Si necesitas cambiar cómo se guardan datos, solo editas `Restaurante`. Si quieres cambiar la interfaz, solo editas `main.py`.

### O — Abierto/Cerrado (OCP)
- `Bebida` **extiende** `Producto` sin modificar su código
- `Restaurante` usa el **mismo método** `registrar_producto()` para ambas clases
- Si quieres agregar nuevos tipos (Postre, Bebida Especial, etc.), solo creas una clase que herede de `Producto`
- **`Restaurante` nunca necesita cambios**

**Ventaja:** El sistema es extensible sin riesgo de romper código existente.

### L — Sustitución de Liskov (LSP)
- `Bebida` **puede reemplazar a** `Producto` en cualquier contexto
- Ambas implementan `mostrar_informacion()` de forma coherente
- `Restaurante.listar_productos()` funciona con ambas sin condicionales
- **Sin sorpresas:** cada subclase respeta el contrato de la clase base

**Ventaja:** Código predecible y comportamiento consistente.

## Cómo Ejecutar

### Opción 1: Ejecutar desde la carpeta restaurante_app

```powershell
cd 'C:\Users\TAMARA\PycharmProjects\2626-POO-TENELEMA-LESLIE-\PARCIAL1\SEMANA 8\restaurante_app'
python main.py
```

### Opción 2: Ejecutar desde la raíz del proyecto

```powershell
cd 'C:\Users\TAMARA\PycharmProjects\2626-POO-TENELEMA-LESLIE-'
python .\PARCIAL1\SEMANA 8\restaurante_app\main.py
```

## Menú Interactivo

Al ejecutar `main.py`, aparecerá este menú:

```
========================================
        SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Registrar bebida
3. Registrar cliente
----------------------------------------
4. Listar productos
5. Listar clientes
----------------------------------------
6. Aprender sobre SOLID
----------------------------------------
7. Salir
```

### Opción 6: Aprender sobre SOLID

Selecciona la opción **6** para acceder a un menú educativo interactivo:

```
1. Principio S - Responsabilidad Unica (SRP)
2. Principio O - Abierto/Cerrado (OCP)
3. Principio L - Sustitucion de Liskov (LSP)
4. Ver los 3 principios juntos (resumen)
5. Volver al menu principal
```

Cada opción mostrará:
- **Definición** clara y accesible del principio
- **Ejemplos de código MAL vs BIEN** con comparaciones
- **Cómo se aplica específicamente en restaurante_app**
- **Ventajas y resultados** de aplicar el principio

## Pruebas Automatizadas

Para ejecutar las pruebas que verifican los principios SOLID:

```powershell
cd 'C:\Users\TAMARA\PycharmProjects\2626-POO-TENELEMA-LESLIE-\PARCIAL1\SEMANA 8\restaurante_app'
python prueba_solid.py
```

**Pruebas incluidas:**
- Responsabilidad Única: cada clase muestra sus datos correctamente
- Abierto/Cerrado: Producto y Bebida usan el mismo método de registro
- Sustitución de Liskov: polimorfismo en el listado de productos
- Validaciones: no permite códigos ni IDs duplicados

## Ejemplo de Flujo

1. **Usuario ejecuta `python main.py`**
   → Se muestra intro a SOLID
   → Menú principal

2. **Usuario selecciona opción 1 (Registrar producto)**
   → Solicita: Código, Nombre, Categoría, Precio
   → Crea objeto `Producto`
   → `Restaurante` lo registra
   → Mensaje de confirmación

3. **Usuario selecciona opción 2 (Registrar bebida)**
   → Solicita: Código, Nombre, Categoría, Precio, Tamaño, Envase
   → Crea objeto `Bebida` (hereda de `Producto`)
   → `Restaurante` lo registra en la MISMA lista
   → Mensaje de confirmación

4. **Usuario selecciona opción 4 (Listar productos)**
   → `Restaurante` itera por la lista
   → Llama `mostrar_informacion()` en cada objeto
   → Cada tipo muestra sus datos específicos (polimorfismo)

5. **Usuario selecciona opción 6 (Aprender sobre SOLID)**
   → Menú educativo interactivo
   → Explicaciones con ejemplos contextualizados
   → Vuelve al menú principal

## Reflexión sobre SOLID

Diseñar con **responsabilidades claras** facilita:
- **Mantenimiento:** cambios localizados sin afectar otros módulos
- **Extensibilidad:** agregar nuevos tipos sin modificar código existente
- **Robustez:** comportamiento predecible y sin sorpresas
- **Legibilidad:** cada clase tiene un propósito único y evidente

Separar la **interacción** (main.py), los **modelos** (datos) y los **servicios** (lógica) permite que el código crezca de forma ordenada y sostenible.

---

**Conclusión:** Este proyecto demuestra que SOLID no es solo teoría, sino una práctica esencial para escribir código mantenible, extensible y robusto.

