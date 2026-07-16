# RESUMEN DE LA TAREA: RESTAURANTE_APP CON EDUCACION SOBRE SOLID

## Completado Exitosamente

### ¿Qué se implementó?

Se creó un **sistema de gestión de restaurante** (`PARCIAL1/SEMANA 8/restaurante_app/`) que combina:

1. **Funcionalidad de negocio**: Registrar y listar productos, bebidas y clientes
2. **Educación interactiva**: Explicaciones didácticas sobre principios SOLID integradas en el software
3. **Arquitectura modular**: Separación clara entre modelos, servicios e interacción
4. **Principios SOLID aplicados**: SRP, OCP y LSP demostrados en cada aspecto del código

---

## Estructura del Proyecto

```
PARCIAL1/SEMANA 8/
├── README.md                    # Documentación completa (153 líneas)
├── demostracion.py             # Script que demuestra el sistema
├── demo_solid.py               # Demostración de SOLID
├── demo_completo.py            # Demostración completa
│
└── restaurante_app/
    ├── main.py                 # Menú interactivo (7 opciones)
    ├── explicaciones.py        # Módulo educativo SOLID (400+ líneas)
    ├── prueba_solid2.py        # Tests automatizados
    │
    ├── modelos/
    │   ├── __init__.py
    │   ├── producto.py         # Clase base: Producto
    │   ├── bebida.py           # Clase: Bebida(Producto)
    │   └── cliente.py          # Clase: Cliente
    │
    └── servicios/
        ├── __init__.py
        └── restaurante.py      # Servicio: administra colecciones
```

---

## Principios SOLID Implementados

### S — RESPONSABILIDAD ÚNICA (SRP)
- `Producto`: solo representa datos de un producto
- `Bebida`: solo representa datos de una bebida
- `Cliente`: solo representa datos de un cliente
- `Restaurante`: solo administra colecciones
- `main.py`: solo maneja interacción con usuario

**Resultado**: Cada archivo tiene UNA responsabilidad clara.

### O — ABIERTO/CERRADO (OCP)
- `Bebida` extiende `Producto` sin modificar su código
- `Restaurante` usa el **MISMO método** `registrar_producto()` para ambas clases
- Sistema listo para agregar nuevos tipos (Postre, BebidaEspecial, etc.) sin cambiar `Restaurante`

**Resultado**: Si quieres agregar un nuevo tipo, solo creas una clase que herede de `Producto`.

### L — SUSTITUCIÓN DE LISKOV (LSP)
- `Bebida` puede reemplazar a `Producto` en cualquier contexto
- Ambas implementan `mostrar_informacion()` de forma coherente
- `Restaurante.listar_productos()` funciona con ambas usando **polimorfismo**
- No hay condicionales `if isinstance()` en el código

**Resultado**: El código es predecible y sin sorpresas.

---

## Características del Sistema

### Menú Interactivo (7 opciones)
```
1. Registrar producto      → Solicita código, nombre, categoría, precio
2. Registrar bebida        → Solicita código, nombre, categoría, precio, tamaño, envase
3. Registrar cliente       → Solicita ID, nombre, correo
4. Listar productos        → Muestra todos con polimorfismo
5. Listar clientes         → Muestra todos registrados
6. Aprender sobre SOLID    → Menú educativo interactivo
7. Salir                   → Cierra el programa
```

### Educación Interactiva sobre SOLID
Optando por **opción 6**, el usuario accede a:
1. **Principio S** - Responsabilidad Única
2. **Principio O** - Abierto/Cerrado
3. **Principio L** - Sustitución de Liskov
4. **Resumen combinado** de los 3 principios
5. **Volver** al menú principal

Cada explicación incluye:
- Definición clara
- Ejemplos de código MAL vs BIEN
- Cómo se aplica en restaurante_app
- Ventajas y resultados

### Validaciones
- No permite códigos de productos duplicados
- No permite IDs de clientes duplicados
- Validación de precios (números positivos)

### Pruebas Automatizadas
`prueba_solid2.py` verifica:
- SRP: Las clases muestran sus datos correctamente
- OCP: Producto y Bebida usan el mismo método
- LSP: Ambas funcionan en la misma lista con polimorfismo
- Validaciones: Se rechazan duplicados

---

## Cómo Ejecutar

### Ejecutar el sistema interactivo:
```powershell
cd C:\Users\TAMARA\PycharmProjects\2626-POO-TENELEMA-LESLIE-\PARCIAL1\SEMANA 8\restaurante_app
python main.py
```

### Ejecutar pruebas:
```powershell
python prueba_solid2.py
```

### Ver demostración completa:
```powershell
cd ..
python demostracion.py
```

---

## Ejemplo de Flujo Real

1. Usuario ejecuta `python main.py`
2. Ve intro sobre SOLID
3. Selecciona opción 1: Registra "Pizza Margherita"
4. Selecciona opción 2: Registra "Refresco 500ml"
5. Selecciona opción 4: Ve ambos (Producto y Bebida) listados con sus datos
6. Selecciona opción 6: Accede a educación sobre SRP, OCP, LSP
7. Lee explicaciones contextualizadas con ejemplos
8. Vuelve al menú y continúa

---

## Archivos Entregables

✓ **main.py** - Punto de entrada, menú, interacción
✓ **explicaciones.py** - 400+ líneas de educación sobre SOLID
✓ **prueba_solid2.py** - Tests que verifican SRP, OCP, LSP
✓ **modelos/producto.py** - Clase base
✓ **modelos/bebida.py** - Herencia + polimorfismo
✓ **modelos/cliente.py** - Modelo simple
✓ **servicios/restaurante.py** - Lógica de negocio
✓ **README.md** - Documentación (153 líneas)
✓ **demostracion.py** - Script de demostración

---

## Commits en GitHub

1. **350168e** - Inicial: restaurante_app con explicaciones.py
2. **c0df454** - README mejorado con documentación completa
3. **0641dee** - Correcciones: imports y prueba_solid2.py
4. **3c74c94** - Agregado: demostracion.py

**Enlace del repositorio**: https://github.com/leslietamara/2626-POO-TENELEMA-LESLIE-

---

## Verificación

✓ Todas las pruebas pasan correctamente
✓ El programa se ejecuta sin errores
✓ Polimorfismo funciona (Bebida lista como Producto)
✓ Validaciones previenen duplicados
✓ Educación sobre SOLID es clara y contextualizada
✓ Arquitectura modular cumple SRP
✓ Sistema es abierto a extensión (OCP)
✓ Subclases son intercambiables (LSP)
✓ Código está en GitHub (repositorio público)

---

## Conclusión

El sistema **restaurante_app** demuestra de forma práctica cómo aplicar los principios SOLID (SRP, OCP, LSP) en un proyecto real. Cada principio se enseña de manera interactiva, no solo en forma teórica sino con ejemplos del mismo código que el usuario está usando. 

El proyecto es **extensible** (puedes agregar nuevos tipos de producto), **mantenible** (cada clase tiene una responsabilidad), y **robusto** (comportamiento predecible sin sorpresas).

✓ **TAREA COMPLETADA EXITOSAMENTE**

