import math

class Circulo:
    def __init__(self):
        self.radio = None

    def solicitar_radio(self):
        while True:
            try:
                radio = float(input("Ingrese el radio del círculo: "))
                if radio == 0:
                    raise ValueError("El radio no puede ser 0")
                elif radio < 0:
                    raise ValueError("El radio no puede ser negativo")
                else:
                    self.radio = radio
                    break
            except ValueError as ve:
                print(f"Error: {ve}")

    def calcular_area(self):
        if self.radio is None:
            self.solicitar_radio()
        return math.pi * self.radio ** 2


def main():
    circulo = Circulo()
    area = circulo.calcular_area()
    print(f"El área del círculo es: {area}")


if __name__ == "__main__":
    main()

