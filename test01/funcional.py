# Uso de las funciones FILTER y MAP 
# estas funciones sirven  para filtrar los elemento de un arreglo/tupla...
# Vídeo 67 -- https://youtu.be/mTJKU7IxL0U?list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS
# 
# 




# Forma 1

# Funcion que nos indica si un numero es PAR o IMPAR
def getPairs(number):
    return (number%2) == 0

# Arreglo de numeros
numbers = [10,123,47,56,63,72,44,34,59,78,50]
# Filtramos los numeros, nos regresa un arreeglo de numeros
numbersPairs = filter(getPairs,numbers)
print(list(numbersPairs))
# Iteramos el arreglo
#for number in numbersPairs:
#    print(number)

# ----------------------------------------------------------$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Forma 2.
# Filtramos los numeros mayores de 50 

# Arreglo de numeros
numbers = [33,44,55,66,77,88,90,100,200,12,20,30,33]
# Filtramos los numeros, nos regresa un arreeglo de numeros
numbersFiltered = filter(lambda number:number>50,numbers) 
print(list(numbersFiltered))


# ----------------------------- FILTRO DE OBJETOS -----------------------------
class Person():
    def __init__(self,key,name,age):
         self.key = key
         self.name = name
         self.age = age 
    def __str__(self):
        return f"""Persona: Name: {self.name}, Age: {self.age}, Key: {self.key}"""

persons = [
    Person('ASQ1','Kal',16),
    Person('ASQ2','Kara',25),
    Person('ASQ3','Rem',17),
    Person('ASQ4','Violet',28),
    Person('ASQ4','Ram',45),
    Person('ASQ4','Diana',30),
    Person('ASQ4','Klaudia',16),
    Person('ASQ4','Jean',14),
    Person('ASQ4','Anna',30)
]
# Filtramos a las personas mayores de edad
personFiltered = filter(lambda prsn:prsn.age > 18,persons)
for prs in personFiltered:
    print(prs)


# ------------------------------------- $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ -------------------------------------
# Uso de la funcion Map.
# Convertir Nombres en minuscula a mayusculas.

names = [
    "Nicky Godfray",
    "Darelle Hulkes",
    "Nita Sackler",
    "Jamill Ingleston",
    "Marlin Birdwhistle",
    "Suzi Ovendon",
    "Eric Oldridge",
    "Reese Fossitt",
    "Rickert Grigor",
    "Dottie Churchley",
    "Maureene Rugieri",
    "Melisse Stork",
    "Roth Ferri",
    "Eadmund Croydon",
    "Tamar Feldmesser",
    "Rochelle Vasyukhin",
    "Betteann Hardesty",
    "Mordecai Lugden",
    "Leticia Suscens",
    "Edgar Michal",
    "Sylvester Gatchell",
    "Bibby Joule",
    "Alfy Waycot",
    "Elspeth Guillou",
    "Wally Hubbock",
    "Casey Matiasek",
    "Cairistiona Batchellor",
    "Jarrid Dosdell",
    "Elisa St. Hill",
    "Gayler Kenright",
    "Darrin Erridge",
    "Alysa Vedeshkin",
    "Irwinn Salerg",
    "Lavena Riddiough",
    "Gerhard Skeete",
    "Gerrie Towndrow",
    "Fernandina Heck",
    "Dulsea Penylton",
    "Lester Bouchier",
    "Emelia Espinho",
    "Jeanna Bullivent",
    "Kahaleel Stokell",
    "Duffie Callan",
    "Truman Maggiore",
    "Milt Fancott",
    "Baxy Valente",
    "Leland Gaiford",
    "Taddeo Varlow",
    "Sibley Cawsby",
    "Aymer Indgs"
]

newName = map(lambda name:name.upper(),names)

print(list(newName))


