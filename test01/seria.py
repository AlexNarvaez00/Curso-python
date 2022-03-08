# Serializacion de informacion
import pickle

persons = [
    {
        "key":"qwe1",
        "name":"User 1"
    },
    {
        "key":"qwe2",
        "name":"User 2"
    },
    {
        "key":"qwe3",
        "name":"User 3"
    },
    {
        "key":"qwe4",
        "name":"User 4"
    }
]
## -> Guardamos el archivo
file = open('names',"wb")
pickle.dump(persons,file)
file.close()

## -> Leemos el archivo
fileR = open('names',"rb")
personRead = pickle.load(fileR)
print(personRead)



