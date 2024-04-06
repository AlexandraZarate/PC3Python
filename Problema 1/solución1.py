def solicitar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: Introduzca un dato válido.")

def solicitar_fraccion():
    while True:
        try:
            x = solicitar_entero("Introduzca el numerador (X) de la fracción: ")
            y = solicitar_entero("Introduzca el denominador (Y) de la fracción: ")
            if y == 0:
                raise ValueError("Y no puede ser 0.")
            if x > y:
                raise ValueError("X debe ser menor o igual a Y.")
            return x, y
        except ValueError as ve:
            print(f"Error: {ve}")

def calcular_porcentaje(x, y):
    porcentaje = (x / y) * 100
    if porcentaje < 1:
        return 'E'
    elif porcentaje > 99:
        return 'F'
    else:
        return round(porcentaje)

def main():
    while True:
        try:
            x, y = solicitar_fraccion()
            porcentaje = calcular_porcentaje(x, y)
            if porcentaje == 'E':
                print("E")
            elif porcentaje == 'F':
                print("F")
            else:
                print(f"{porcentaje}%")
            break  # Salir del bucle si no hay error
        except ValueError as ve:
            print(f"Error: {ve}")

if __name__ == "__main__":
    main()
