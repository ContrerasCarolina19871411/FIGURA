from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass


class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3


# Ejemplo de uso
triangulo = Triangulo(10, 5, 7, 8, 9)
area = triangulo.calcular_area()
perimetro = triangulo.calcular_perimetro()
print("Área del triángulo:", area)
print("Perímetro del triángulo:", perimetro)

