# Decoradores,.
# Video 73, 74 ...
# https://youtu.be/DQXm6bIZgvk?list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&t=95


#Basicamente consiste en pasar una funcioin como parametro.

def funcion_exterior(function):
    # Funcion interior
    def funcion_interior():
        # Instruccion... 
        print('Ejecutando otras instruccion.... inicio')
        #Funcion a decorar.
        function()
        # Instruccion... 
        print('Ejecutando otras instruccion.... final')
    # Regresamos la funcion interna 
    return funcion_interior


@funcion_exterior
def calcArea():
    print('Calculo 1...')

calcArea()


# ----------------------------------------- funcion decoradora con parametros ...............................

def funct_exter(function):
    def funct_inter(*params):
        print("Instruciones...... 1")
        function(*params)
        print("Instruciones...... 2")
    return funct_inter

@funct_exter
def suma(number1,number2):
    print(number1+number2)


suma(30,20)



