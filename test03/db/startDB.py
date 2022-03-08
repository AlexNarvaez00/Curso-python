# Este script crea la base de datos por primera vez
# solo se debe de ejecutar una vez, para crear las tablas,
# en la base de datos.

# Author:  Narvaez Ruiz Alexis

from models.Person import Person
from patterns.singleton import *  
from config import *
from Class2 import Names2

tmpe = Person(('Alexis'))
print(tmpe)






