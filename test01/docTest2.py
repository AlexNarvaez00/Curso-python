# Documentacion para hacer pruebas.

import math


def calcSqrts(numbers):
    """
        Calcula la raiz cuadrada de los numerodos dados
        , regresando un numero arreglo

        >>> calcSqrts([16,25,100,36])
        [4.0, 5.0, 10.0, 6.0]
    """ 
    #return list(map(lambda number:math.sqrt(number),numbers))
    return [math.sqrt(n) for n in numbers]

# print(calcSqrts([16,25,100,36]))
import doctest
doctest.testmod()