from Model import *
from Person import *


person1 = Person(None)
person1.setValueColumn('keyStr','AQSWDEFRGT')
person1.setValueColumn('name','Alexis')
person1.setValueColumn('age',20)
print(person1.__str__())
#person1.save()

modelList = Model.list(Person,'Persona')
print(modelList[0])