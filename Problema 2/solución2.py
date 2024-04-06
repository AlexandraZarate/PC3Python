def solicitar_calificaciones():
    while True:
        calificaciones_str = input("Ingrese las calificaciones separadas por comas (del 0 al 20, incluyendo números decimales): ")
        calificaciones_lista = calificaciones_str.split(',')
        calificaciones_enteros = []

        try:
            for calificacion_str in calificaciones_lista:
                calificacion = float(calificacion_str.strip())
                if not (0 <= calificacion <= 20):
                    raise ValueError("Las calificaciones deben estar en el rango de 0 a 20.")
                calificaciones_enteros.append(round(calificacion))
            return calificaciones_enteros
        except ValueError as ve:
            print(f"Error: {ve}. Por favor ingrese calificaciones válidas.")

def main():
    calificaciones = solicitar_calificaciones()
    print("Calificaciones ingresadas:", calificaciones)

if __name__ == "__main__":
    main()