# @Author Narvaez Ruiz Alexis 

from traceback import print_last


names = ["Alexis",
            "Narvaez",
            "Ruiz",
            "Andrea",
            "Amairany"]
names.append("juan") # Agrega el elemento al final
names.insert(1,"Anna") #Agrega el elmento en la posicion dada
# print(names.index('Anna')) #Rgresa la posicion donde se ecnuentra el
# el elmento.
# print("Alexis" in names) #Pregunta si el valor se encutra 
# dentro de la lista
names.pop() #Elimina el ultimo elemento de la lista
print(names)

carreras=["Sistemas","Ingles","Gestion"]


union= names+carreras #Une dos listas
print(union)

