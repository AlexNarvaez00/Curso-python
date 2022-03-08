# Generadores
# Crean un objeto "Iterable" que va extrallendo los valores 
# segun sea la llamada de la funcion (extrae valores de uno en uno)

# Anotacion mia -> Lo entiendo como una pila en Java



#Funcion tradiciconal
def numbersPairs(length) :
    num=0;
    listNumbers = []
    for index in range(length):
        listNumbers.append(num)
        num+=2
    return listNumbers 

print(numbersPairs(10))



# CON GENERADORES
def numbersPairsGen(length) :
    num=0;
    # listNumbers = []
    for index in range(length):
        # listNumbers.append(num)
        yield num
        num+=2
    # return listNumbers

listNumbersPairsGen = numbersPairsGen(10)
print('Primera extacción: '+ str( next(listNumbersPairsGen) ))
print('Segunda extacción: '+ str( next(listNumbersPairsGen) ))
print('Tercera extacción: '+ str( next(listNumbersPairsGen) ))
print('Cuarta extacción: '+ str( next(listNumbersPairsGen) ))
print('Quinta extacción: '+ str( next(listNumbersPairsGen) ))
print('Sexta extacción: '+ str( next(listNumbersPairsGen) ))
print('Septima extacción: '+ str( next(listNumbersPairsGen) ))
print('Octava extacción: '+ str( next(listNumbersPairsGen) ))
print('Novena extacción: '+ str( next(listNumbersPairsGen) ))
print('Decima extacción: '+ str( next(listNumbersPairsGen) ))
# En esta linea genera un error, por que ya no accede a la instruccion 
# yield en el for de arriba
# print('Onceava extacción: '+ str( next(listNumbersPairsGen) ))
