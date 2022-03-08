# Author: Narvaez Ruiz Alexis 

# Clase para generar los modelos necesarios para hacer las consultas 
# necesarias en a la base de datos.
import sys
sys.path.append(sys.path[0] + '\\..\\')
from patterns.singleton import *

# Funciones basicas del modelo
#   -> Agregar.
#   -> Buscar.
#   -> Eliminar.
#   -> Recuperar toda la lista 
class SuperModel_Class():
    # Constructor de la clase.
    #   nameTable -- Nombre de la tabla
    #   primaryKey -- Llave primaria de la de la tabla
    #   nameTable -- Nombre de la tabla
    #   valuesRow -- Valores para insertar en la tabla
    def __init__(self,nameTable,primaryKey,valuesRow):
        self.__nameTable = nameTable
        self.__primaryKey = primaryKey

        # Debe de ser un arreglo
        self.__values = valuesRow
        self.__queryInsertStr = self.__queryInsert()


        self.__instance = SingletonDB.getInstance()
    
    # ------------------------------------- Funciones de instancia -------------------------------------
    
    # Regresamos los valores en forma de tupla.
    def getValues(self):
        return tuple(self.__values)

    # Guarda un registro en la base de datos 
    def save(self):
        # Obtenemos el cursor
        cursor = self.__instance.getConnection().cursor()
        cursor.execute(self.__queryInsertStr,tuple(self.__values))
        self.__instance.getConnection().commit()
        self.__instance.getConnection().close()
    
    
    # Funcion que crea la instruccion de insercion de datos en la base de datos.
    def __queryInsert(self):
        cantidadSingnos = len(self.__values)
        strSignos = '?,' * cantidadSingnos
        signos = strSignos[ 0 : len(strSignos) - 1 ]

        return f"""INSERT INTO "{self.__nameTable}" VALUES ({signos})"""

    #Convierte el objeto en un string
    def __str__(self):
        return f""": {self.__values}"""
