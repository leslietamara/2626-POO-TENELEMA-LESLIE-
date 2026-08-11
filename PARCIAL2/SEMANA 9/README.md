# Semana 9 - Persistencia con JSON

Esta carpeta replica el software de la semana 8, pero cambia la forma en que se guardan los datos: ahora los productos y clientes se almacenan en archivos JSON usando una estructura tipo diccionario.

## Estructura

```text
PARCIAL2/
└── SEMANA 9/
    ├── README.md
    └── restaurante_app/
        ├── __init__.py
        ├── main.py
        ├── data/
        │   ├── productos.json
        │   └── clientes.json
        ├── modelos/
        │   ├── __init__.py
        │   ├── bebida.py
        │   ├── cliente.py
        │   └── producto.py
        └── servicios/
            ├── __init__.py
            └── restaurante.py
```

## Estructura de los JSON

Los archivos usan un diccionario por clave:

```json
{
  "P001": {
    "codigo": "P001",
    "nombre": "Pizza Margarita",
    "categoria": "Plato fuerte",
    "precio": 14.5
  }
}
```

```json
{
  "C001": {
    "identificacion": "C001",
    "nombre": "Ana López",
    "correo": "ana@example.com"
  }
}
```

## Funcionalidades

- Registrar productos y bebidas
- Registrar clientes
- Listar productos y clientes
- Buscar por código o identificación
- Eliminar por código o identificación
- Guardar todo en archivos JSON

## Cómo ejecutar

```powershell
cd "C:\Users\TAMARA\PycharmProjects\2626-POO-TENELEMA-LESLIE-\PARCIAL2\SEMANA 9\restaurante_app"
python main.py
```
