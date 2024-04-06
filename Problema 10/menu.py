from ejercicio3 import Circulo
from ejercicio4 import Rectangulo

def calcular_area_circulo():
    try:
        radio = float(input("Ingrese el radio del círculo: "))
        circulo = Circulo(radio)
        area = circulo.calcular_area()
        print(f"El área del círculo con radio {radio} es: {area}")
    except ValueError as ve:
        print(f"Error: {ve}")

def calcular_area_rectangulo():
    try:
        largo = float(input("Ingrese el largo del rectángulo: "))
        ancho = float(input("Ingrese el ancho del rectángulo: "))
        rectangulo = Rectangulo(largo, ancho)
        area = rectangulo.calcular_area()
        print(f"El área del rectángulo con largo {largo} y ancho {ancho} es: {area}")
    except ValueError as ve:
        print(f"Error: {ve}")

def calcular_area_cuadrado():
    try:
        lado = float(input("Ingrese el lado del cuadrado: "))
        cuadrado = Rectangulo(lado, lado)  # Un cuadrado es solo un caso especial de un rectángulo con lados iguales
        area = cuadrado.calcular_area()
        print(f"El área del cuadrado con lado {lado} es: {area}")
    except ValueError as ve:
        print(f"Error: {ve}")

def menu():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            calcular_area_circulo()
        elif opcion == '2':
            calcular_area_rectangulo()
        elif opcion == '3':
            calcular_area_cuadrado()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()


