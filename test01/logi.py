#Operadores logicos 
#AND OR

person = {
    "name":"Alex",
    "age":19,
    "key":17161195,
    "rol":1
}

if person['age'] > 0 and person['age'] > 18 : 
    print('Edad valida')

if (person['age'] > 0) & (person['age'] > 18) : 
    print('Edad valida 2')
