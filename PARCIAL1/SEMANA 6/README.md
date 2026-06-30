# Sistema de Restaurante App

**Nombre del estudiante:** Leslie Tamara Tenelema

## Descripción del Sistema
Este proyecto es una aplicación modular desarrollada en Python que simula la administración del menú de un restaurante, aplicando los principios de la Programación Orientada a Objetos (POO). 

## Estructura del Proyecto
El proyecto está estructurado de la siguiente forma:
- `restaurante_app/modelos/`: Contiene las clases de las entidades del sistema (`producto.py`, `platillo.py`, `bebida.py`).
- `restaurante_app/servicios/`: Contiene la clase de lógica y administración (`restaurante.py`).
- `restaurante_app/main.py`: Archivo principal que arranca el programa.

## Principios POO Aplicados
- **Herencia:** Se aplicó una relación de herencia donde `Platillo` y `Bebida` son clases hijas de la clase padre `Producto`. Comparten atributos como nombre, precio y disponibilidad, mientras añaden atributos propios (calorías y volumen en ml, respectivamente).
- **Encapsulación:** El atributo `__precio` de la clase `Producto` está encapsulado, impidiendo su acceso directo y requiriendo del uso de los métodos `obtener_precio()` y `cambiar_precio()` (que incluye validación de que no sea 0 o negativo) para ser manipulado.
- **Polimorfismo:** El polimorfismo se evidencia mediante el método `mostrar_informacion()`. Se sobrescribe en cada clase hija para retornar detalles específicos. En el método `mostrar_menu()` de la clase `Restaurante`, se itera una lista de productos y se invoca `mostrar_informacion()` en cada uno de los objetos, respondiendo cada cual de la forma adecuada dependiendo de si es `Platillo` o `Bebida`.

## Reflexión sobre la importancia de la POO
Aplicar los principios de la Programación Orientada a Objetos en proyectos Python permite crear código más limpio, escalable y mantenible. La herencia evita la duplicidad de código, la encapsulación protege los datos críticos del sistema de modificaciones indebidas, y el polimorfismo aporta gran flexibilidad al manejar distintos tipos de objetos a través de una interfaz común, haciendo que los sistemas modulares sean robustos y fáciles de extender.
