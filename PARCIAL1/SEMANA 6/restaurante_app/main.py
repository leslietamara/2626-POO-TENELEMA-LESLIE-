from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def main():
    # 1. Instanciar la clase de servicio
    mi_restaurante = Restaurante("La Cuchara de Palo")

    # 2. Crear objetos de tipo Platillo
    platillo_1 = Platillo("Ceviche Mixto", 12.50, calorias=450)
    platillo_2 = Platillo("Lomo Saltado", 15.00, calorias=700, disponibilidad=False)

    # 3. Crear objetos de tipo Bebida
    bebida_1 = Bebida("Jugo de Naranja", 3.00, volumen_ml=500)
    bebida_2 = Bebida("Cerveza Artesanal", 5.50, volumen_ml=330)

    # 4. Demostrar encapsulación modificando un precio mediante el método
    print("=== DEMOSTRACIÓN DE ENCAPSULACIÓN ===")
    print(f"Precio original de '{platillo_1.nombre}': ${platillo_1.obtener_precio():.2f}")
    
    print("\n-> Modificando precio a $13.00 (Valor válido)...")
    platillo_1.cambiar_precio(13.00)
    print(f"Nuevo precio de '{platillo_1.nombre}': ${platillo_1.obtener_precio():.2f}")
    
    print("\n-> Intentando modificar precio a -$2.00 (Valor inválido)...")
    # Intento de precio negativo (debe mostrar error)
    bebida_1.cambiar_precio(-2.00)
    print(f"El precio de '{bebida_1.nombre}' se mantiene en: ${bebida_1.obtener_precio():.2f}")
    print("=====================================\n")

    # 5. Agregar objetos a la lista del restaurante
    mi_restaurante.agregar_producto(platillo_1)
    mi_restaurante.agregar_producto(platillo_2)
    mi_restaurante.agregar_producto(bebida_1)
    mi_restaurante.agregar_producto(bebida_2)

    # 6. Mostrar el menú (evidenciando polimorfismo)
    print("=== DEMOSTRACIÓN DE POLIMORFISMO ===")
    mi_restaurante.mostrar_menu()

if __name__ == "__main__":
    main()
