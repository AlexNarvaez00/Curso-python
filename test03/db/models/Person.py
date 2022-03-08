from SuperModel import SuperModel_Class
class Person(SuperModel_Class) :
    # Constructor del formulario
    def __init__(self,name,id):
        super().__init__('Person','ID',[name,id])
      
    # Convierte el objeto en un String
    def __str__(self):
        return f"Persona {super().__str__()}"
