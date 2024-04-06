class Rectangulo:
    def __init__(self, largo, ancho):
        if largo <= 0 or ancho <= 0:
            raise ValueError("Tanto el largo como el ancho deben ser mayores que 0.")
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho


def solicitar_dimension(mensaje):
    try:
        valor = float(input(mensaje))
        if valor <= 0:
            print("Error: El valor debe ser mayor que 0.")
            return solicitar_dimension(mensaje)  # Llamada recursiva si el valor es negativo o igual a 0
        return valor
    except ValueError:
        print("Error: Ingrese un número válido.")
        return solicitar_dimension(mensaje)  # Llamada recursiva si se ingresa un valor no numérico


def main():
    try:
        # Solicitar largo del rectángulo
        largo = solicitar_dimension("Ingrese el largo del rectángulo: ")

        # Solicitar ancho del rectángulo
        ancho = solicitar_dimension("Ingrese el ancho del rectángulo: ")

        # Crear objeto Rectangulo
        rectangulo = Rectangulo(largo, ancho)

        # Calcular área del rectángulo
        area = rectangulo.calcular_area()

        # Mostrar el resultado
        print(f"El área del rectángulo con largo {largo} y ancho {ancho} es: {area}")

    except ValueError as ve:
        print(f"Error: {ve}")


if __name__ == "__main__":
    main()