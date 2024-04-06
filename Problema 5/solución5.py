class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Información del estudiante:")
        print(f"Nombre: {self.nombre}")
        print(f"Número de registro: {self.numero_registro}")

    def set_edad(self):
        while True:
            try:
                edad = int(input("Ingrese la edad del estudiante: "))
                if edad < 13 or edad > 15:
                    raise ValueError("No hay estudiantes con esta edad")
                else:
                    self.edad = edad
                    break
            except ValueError as ve:
                print(f"Error: {ve}")

    def set_notas(self):
        while True:
            try:
                notas = input("Ingrese las notas del estudiante separadas por comas: ")
                notas = notas.split(",")
                notas = [int(nota) for nota in notas]
                for nota in notas:
                    if nota < 5 or nota > 20:
                        raise ValueError("Introduzca notas válidas")
                self.notas = notas
                break
            except ValueError as ve:
                print(f"Error: {ve}")

    def mostrar_resultado(self):
        print("Resultado:")
        print(f"Nombre del alumno: {self.nombre}")
        print(f"Número de registro: {self.numero_registro}")
        print(f"Edad del alumno: {self.edad}")
        print(f"Notas del alumno: {self.notas}")


def main():
    while True:
        try:
            nombre = input("Ingrese el nombre del alumno: ")
            if not nombre.isalpha():
                raise ValueError("Tipo de dato no válido")
            numero_registro = int(input("Ingrese el número de registro del alumno: "))
            if numero_registro < 0:
                raise ValueError("No es posible un número de registro negativo")

            alumno = Alumno(nombre, numero_registro)
            alumno.display()
            alumno.set_edad()
            alumno.set_notas()
            alumno.mostrar_resultado()
            break  # Salir del bucle si no hay error
        except ValueError as ve:
            print(f"Error: {ve}")


if __name__ == "__main__":
    main()
