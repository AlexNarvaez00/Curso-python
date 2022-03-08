#Condicionales
person = {
    'name':"Karla",
    'edad':18,
    'key':"qwerty"
}
#Else if juntos
# 

if person['edad'] > 18 :
    print(person['name']+" es mayor de edad")
elif person['edad'] == 18 : 
    print(person['name']+" tiene 18 años")
else :
    print(person['name']+" NO es mayor de edad")
