# Uso de expresiones regulares.
# video  69,70,71
# Pagina qu epuede ser muy util 
# https://www.w3schools.com/python/python_regex.asp

import re

# Sintaxis basico
#Expresion regular.... Las plabras deben de inicar con una mayuscula y tener
# por lo menos 3 letras 

expresion = '^[A-Z][a-z]{2,15}$'
texto = "Ian"

print(re.match(expresion,texto))


request = re.search(expresion,texto)
if(request is not None):
    print(request.start())
    print(request.end())
    print(request.span())
    print(request.string)
else: 
    print('No se encontraron coincidencias o algo salio mal ')






