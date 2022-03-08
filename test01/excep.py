# Uso de las "Excepciones"


#Funcion para extraer el resultado de la formula general
#Ecuaciuones de segundo grado
import math 

def getX(a,b,c) :
    #Operacion que va dentro de la casita XD
    casita = (b*b) - (4*a*c)
    dividendo = -b - math.sqrt(casita)
    return ( dividendo/(2*a) )

try:
    #  ->  a=1,b=-5,c=6
    print("Solucion " + str( getX(1,-5,6) ) )
except ValueError : #Podrias no poner "ValueError"  pero al excepcion seria general
    print('No existe la raiz cuadrada de numeros negativos')
# Se pueden agregar multiples excepciones como en Java
 

 #finally: 
 # .... se ejecutara siempre

