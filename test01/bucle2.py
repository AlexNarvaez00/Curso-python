#Narvaez Ruiz Alexis

#Bucles2 
persons = [
    {
        "key":"qwe1",
        "name":"User1",
        "numbers":[1,4,5,8,2]
    },
    {
        "key":"qwe2",
        "name":"User2",
        "numbers":[1,2,7,0,3]
    },
    {
        "key":"qwe3",
        "name":"User3",
        "numbers":[1,1,1,1,1]
    },
    {
        "key":"qwe4",
        "name":"User4",
        "numbers":[1,2,3,4,5]
    },
    {
        "key":"qwe5",
        "name":"User5",
        "numbers":[1,4,4,4,4]
    },
]
index = 0;
for element in persons:
    if (index % 2) == 0 :
        print(element)
    else:
        print('No permitido')
    index+=1


###Imprimir string caracter a caracter
name = "Alexis"
for char in name:
    print(char)
print("----------------")


# rage(i,k,j)
# i -> inicio
# k -> Final 
#j -> Incremento
for index in range(10,20,3):
    print(f"Posición número {index}")
