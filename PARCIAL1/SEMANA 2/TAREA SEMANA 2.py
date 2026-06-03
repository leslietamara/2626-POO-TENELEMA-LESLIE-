# Programa: Representación de un objeto real mediante una clase
# Ejemplo: Clase Estudiante

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = int(edad)
        self.grado = grado
        self.calificaciones = []

    def agregar_calificacion(self, nota):
        if not (0 <= nota <= 100):
            raise ValueError("La calificación debe estar entre 0 y 100")
        self.calificaciones.append(float(nota))

    def promedio(self):
        if not self.calificaciones:
            return None
        return sum(self.calificaciones) / len(self.calificaciones)

    def es_aprobado(self, minima=60):
        avg = self.promedio()
        if avg is None:
            return False
        return avg >= minima

    def mostrar_info(self):
        avg = self.promedio()
        avg_str = f"{avg:.2f}" if avg is not None else "N/A"
        return f"Estudiante: {self.nombre}, Edad: {self.edad}, Grado: {self.grado}, Promedio: {avg_str}"

    def __repr__(self):
        return f"Estudiante({self.nombre!r}, {self.edad}, {self.grado!r})"


if __name__ == "__main__":
    # Demo de uso
    alumno = Estudiante("Ana Pérez", 20, "Segundo")
    alumno.agregar_calificacion(85)
    alumno.agregar_calificacion(92)
    alumno.agregar_calificacion(78)
    print(alumno.mostrar_info())
    print("Promedio:", alumno.promedio())
    print("Aprobado:", "Sí" if alumno.es_aprobado(60) else "No")
