# Uso de la instruccion de "Yield form"
# 
#  -> se puede usar en los bucles anidados
#  

# La elipsis en Python se escribe con un asterisco
# def myFunction(*args)


def getNames(*names):
    for element in names : #Ciclo padre
        #for subElement in element: #Segundo siclo 
            #yield subElement
        yield from element

genObject = getNames('Alexis','Cladia','Martin')

print('Primera extracción '+next(genObject))
print('Segunda extracción '+next(genObject))
print('Tercera extracción '+next(genObject))


