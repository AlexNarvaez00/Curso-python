# CLase "Persona"
from Model import Model
class Person(Model):
    #Constructor de la clase
    def __init__(self,name,lastrName,age):
        super().__init__('Person',[name,lastrName,age])
    

    # Sobreescritura
    def __str__(self):
        return f"""Person {super().__str__()}"""