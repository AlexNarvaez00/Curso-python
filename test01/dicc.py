#Diccionarios
#Clave:valor
#La clave puede ser de cualquier tipo, pero de 
#ser unica

#El valor puede ser de cualquier tipo
table = {
    'qw1':"Alexis",
    'qw2':"Zayda",
    'qw3':"Jordan",
    'qw4':"Claudia",
    'qw5':"Jenni"
}
print(table['qw1'])

##Agregar mas elmentos
table['qw6'] = "Denisse"
print(table)

#Elimina un elmento del diccionario
del table['qw1']
print(table)

#Claves
print(table.keys())
#Valores
print(table.values())
#Longitud
print(len(table))

