##Herencia

class Articulo():
    def __init__(self,precio,cantidad):
        self.__precio = precio
        self.__canitdad = cantidad
    def getPrecio(self):
        return self.__precio
    def getCantidad(self):
        return self.__canitdad
    def setPrecio(self,precio):
        self.__precio = precio
    def setCantidad(self,cantidad):
        self.__cantidad = cantidad

    def __str__(self):
        return f"""Articulo: Precio::{self.__precio}, Cantidad::{self.__canitdad}"""

class Llanta(Articulo):
    def __init__(self, precio, cantidad,marca):
        super().__init__(precio, cantidad)
        self.__marca = marca

    def getMarca(self):
        return self.__marca
    def setMarca(self,marca):
        self.__marca = marca

    def __str__(self):
        return f"{super().__str__()} | Maca:: {self.__marca}"

articulo = Articulo(200,10)
llanta1 = Llanta(250,10,"Michelline")

print(articulo)
print(llanta1)
print(llanta1.getPrecio())


### VIDEO 31
