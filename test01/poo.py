from asyncio.windows_events import NULL


class Person():
     #Atributos de la clase.
     name = NULL
     key = NULL
     calificaciones = []

     def getPromedio(self):
         sumador = 0;
         for index in self.calificaciones : 
             sumador+=index
         return sumador/len(self.calificaciones)



persona = Person() #Instaciamos la clase
print(persona)
persona.calificaciones = [10,10,9,9]
print(persona.getPromedio())

### Video 27 