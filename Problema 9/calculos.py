import operaciones

if __name__ == "__main__":
    # Ejemplos de uso
    print("Suma:", operaciones.suma(5, 3))
    print("Resta:", operaciones.resta(10, 4))
    print("Producto:", operaciones.producto(6, 7))
    print("División:", operaciones.division(8, 2))
    
    # Ejemplos de manejo de errores
    print("Suma con error:", operaciones.suma(5, "3"))
    print("División por cero:", operaciones.division(8, 0))
