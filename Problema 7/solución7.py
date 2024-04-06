import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Cuadrante I"
        elif self.x < 0 and self.y > 0:
            return "Cuadrante II"
        elif self.x < 0 and self.y < 0:
            return "Cuadrante III"
        elif self.x > 0 and self.y < 0:
            return "Cuadrante IV"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre el eje X"
        else:
            return "En el origen"

    def vector(self, otro_punto):
        return Punto(otro_punto.x - self.x, otro_punto.y - self.y)

    def distancia(self, otro_punto):
        distancia = math.sqrt((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2)
        print(f"La distancia entre {self} y {otro_punto} es: {distancia}")

class Rectangulo:
    def __init__(self, punto1=Punto(), punto2=Punto()):
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        return abs(self.punto2.x - self.punto1.x)

    def altura(self):
        return abs(self.punto2.y - self.punto1.y)

    def area(self):
        return self.base() * self.altura()

# Ejemplo de uso:
punto1 = Punto(3, 5)
punto2 = Punto(-2, 7)
punto3 = Punto(-3, -2)
punto4 = Punto(2, -4)

print("Punto 1:", punto1)
print("Cuadrante:", punto1.cuadrante())
print()

print("Punto 2:", punto2)
print("Cuadrante:", punto2.cuadrante())
print()

print("Punto 3:", punto3)
print("Cuadrante:", punto3.cuadrante())
print()

print("Punto 4:", punto4)
print("Cuadrante:", punto4.cuadrante())
print()

print("Vector entre punto 1 y punto 2:", punto1.vector(punto2))
print("Vector entre punto 2 y punto 1:", punto2.vector(punto1))
print()

punto1.distancia(punto2)
punto2.distancia(punto3)
print()

rectangulo = Rectangulo(punto1, punto3)
print("Base del rectángulo:", rectangulo.base())
print("Altura del rectángulo:", rectangulo.altura())
print("Área del rectángulo:", rectangulo.area())
