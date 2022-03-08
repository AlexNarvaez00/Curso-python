class Figure():
    def __init__(self,base,altura) : 
        self.__base = base
        self.__altura = altura
    def getBase(self):
        return self.__base
    def getAltura(self):
        return  self.__altura
    def getArea(self):
        return self.__base*self.__altura
    def __str__(self):
        return "Figura: ->"

class Cuadrado(Figure):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    def getArea(self):
        return self.getBase()*self.getAltura()
    def __str__(self):
        return f"{super().__str__()} Cuadrado: Base::{self.getBase()}, Altura::{self.getAltura()}"

class Triangulo(Figure):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    def getArea(self):
        return ( self.getBase()*self.getAltura() )/2
    def __str__(self) -> str:
        return f"{super().__str__()} Triangulo: Base::{self.getBase()}, Altura::{self.getAltura()}"


figuras = [
    Figure(10,10),
    Cuadrado(20,20),
    Triangulo(20,20)
]

print(figuras[0])
print(figuras[1])
print(figuras[2])
print("--------------------")
print(figuras[0].getArea())
print(figuras[1].getArea())
print(figuras[2].getArea())




