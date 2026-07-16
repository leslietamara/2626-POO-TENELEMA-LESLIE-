# Tarea Semana 8 - Restaurante App

Nombre del estudiante: [Tu Nombre Completo]

Descripción:
Versión mejorada del sistema `restaurante_app` para practicar principios SOLID (SRP, OCP, LSP). El sistema permite registrar y listar productos, bebidas y clientes desde un menú por consola.

Estructura del proyecto:

restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py

Responsabilidad de cada clase:
- `Producto` (modelos/producto.py): datos y método `mostrar_informacion()`.
- `Bebida` (modelos/bebida.py): hereda de `Producto` e incorpora atributos propios (tamaño, envase). Sobrescribe `mostrar_informacion()`.
- `Cliente` (modelos/cliente.py): representa información de un cliente y `mostrar_informacion()`.
- `Restaurante` (servicios/restaurante.py): administra colecciones, registra y lista productos y clientes.

Principios aplicados:
- SRP: cada clase tiene una única responsabilidad (modelo vs servicio vs presentación).
- OCP: `Bebida` amplía `Producto` sin modificar la lógica del servicio `Restaurante`.
- LSP: `Bebida` puede usarse donde se espera un `Producto` — el servicio usa el método común `mostrar_informacion()`.

Ejecución:
Abrir una terminal en la carpeta `PARCIAL1/SEMANA 8/restaurante_app` y ejecutar:

```powershell
python main.py
```

Reflexión breve:
Diseñar con responsabilidades claras facilita el mantenimiento y la extensión del sistema. Separar la interacción (main), los modelos y los servicios permite añadir nuevos tipos de producto sin cambiar el código de administración.

