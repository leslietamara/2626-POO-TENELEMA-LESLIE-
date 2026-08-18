# Restaurante App - Semana 10

Estudiante: Leslie Tamara Tenelema

## Descripción

Este proyecto continúa la evolución de la aplicación de restaurante desarrollada en semanas anteriores. La mejora principal de esta entrega es la persistencia de los productos mediante un archivo JSON, permitiendo conservar la información aunque la aplicación se cierre y volver a cargarla al iniciar nuevamente.

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   └── productos.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
├── README.md
└── __init__.py
```

## Responsabilidades

- modelos/producto.py: define la clase Producto con validaciones, serialización a diccionario y reconstrucción desde JSON.
- modelos/usuario.py: representa la entidad Usuario del sistema. No se persiste en esta semana.
- servicios/restaurante.py: administra registros, búsquedas, actualizaciones, eliminaciones y listado de productos y usuarios.
- servicios/archivo_servicio.py: centraliza la lectura y escritura del archivo productos.json usando json.load() y json.dump() con manejo de errores.
- main.py: crea los servicios, carga los productos al iniciar, opera con el menú y solicita el guardado después de cambios.

## Archivo JSON

El archivo `datos/productos.json` almacena la colección de productos como una lista de diccionarios. Cada elemento conserva la información del producto en formato compatible con JSON.

Ejemplo:

```json
[
  {
    "codigo": "P001",
    "nombre": "Pizza Margarita",
    "categoria": "Plato fuerte",
    "precio": 14.5
  }
]
```

## Flujo de carga y guardado

1. main.py crea una instancia de ArchivoServicio.
2. El servicio intenta abrir `datos/productos.json`.
3. Si el archivo existe y contiene JSON válido, el programa reconstruye objetos Producto.
4. La colección se envía al servicio Restaurante para seguir trabajando con objetos del dominio.
5. Cuando se registra, actualiza o elimina un producto, el programa vuelve a guardar la nueva lista sobre el archivo JSON.

## Manejo de excepciones

La aplicación controla las situaciones esperadas de forma específica:

- FileNotFoundError: si el archivo no existe, la aplicación inicia con una colección vacía.
- json.JSONDecodeError: si el archivo existe pero su contenido no es JSON válido, se informa y se ignora la lectura.
- PermissionError: cuando no hay permisos para leer o escribir el archivo.
- KeyError: cuando un registro del JSON no contiene las claves esperadas.
- ValueError: para validar datos inválidos dentro de la clase Producto o en los datos ingresados por consola.

## Cómo ejecutar

```powershell
cd "C:\Users\TAMARA\PycharmProjects\2626-POO-TENELEMA-LESLIE-\PARCIAL2\SEMANA 10\restaurante_app"
python main.py
```

## Verificación de persistencia

Se comprobó el funcionamiento cerrando y reiniciando la aplicación. Tras registrar, actualizar y eliminar productos, la información quedó guardada en `datos/productos.json`; al ejecutar la app nuevamente, los productos persistidos aparecían en el listado y las modificaciones se conservaban correctamente.
