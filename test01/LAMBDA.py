# Expresiones lambda, en python

#Nombre=lambda parametro1,parametro2... : operacion  
suma = lambda parametro1,parametro2: parametro1+parametro2

resta = lambda parametro1,parametro2: parametro1-parametro2

multi = lambda parametro1,parametro2: parametro1*parametro2

div = lambda parametro1,parametro2: parametro1/parametro2

print( f"""Suma: {suma(10,10)}""" )
print( f"""Reta: {resta(10,10)}""" )
print( f"""Multiplicacion: {multi(10,10)}""" )
print( f"""Division: {div(10,10)}""" )

