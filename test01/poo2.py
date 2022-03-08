class Pelicula ():
    ##Constructor
    def __init__(self,titulo,duracion,descripcion):
       ##Atributos
       self.__titulo = titulo
       self.__duracion = duracion
       self.__descripcion = descripcion
        ##Encapsulamiento de los atributos
        ## se hace agregando dos guines bajos
        ## tambien funciona con los metodos
        ## __attribute

    ##Getter
    def getTitulo(self):
        return self.__titulo
    ##setter
    def setTitulo(self,titulo):
        self.__titulo = titulo

     #Este metodo convierte el objeto en un string 
     # como en Java   
    def __str__(self) :
        return f"pelicula: Titulo:: {self.__titulo}, Duracion:: {self.__duracion}, Descripcion:: {self.__descripcion}"
        

cartelera = [
    Pelicula("Harry potter 1",180,"Pulicula basada en un libro de JK rolins"),
    Pelicula("Harry potter 2",180,"Pulicula basada en un libro de JK rolins"),
    Pelicula("Harry potter 3",180,"Pulicula basada en un libro de JK rolins"),
]

print(cartelera[0])
cartelera[0].setTitulo('Volver al futuro')
print(cartelera[0])
