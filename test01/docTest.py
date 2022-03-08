# Documentacion para  realizar pruebas
# video 76,77,78
# https://youtu.be/64v9X7K-iuc?list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS

def calcArea(base,altura):
    """Calcula el area de un triangulo

        >>> calcArea(3,6)
        9.0
    """
    return base*altura/2

#Importamos el siguiente modulo para poder relizar las pruebas.
import doctest
doctest.testmod()


#NOTA RAPIDO 
# Al  ejecutar el test si no no regresa nada significa que el test fue exitoso 
# en caso contrario con mostrara el error que se genero