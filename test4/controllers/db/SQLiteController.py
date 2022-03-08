# Crea una conexion a una base de datos de tipos SQLite
import sqlite3
import sys
sys.path.append(sys.path[0] + '\\..\\..\\')
from config import *

class SQLiteContoller():

    # Contructor de la clase
    # name - Nombre de la conexion
    def __init__(self):
        self.__connection = sqlite3.connect(CONECCTION_NAME)

        # Obtenemos el cursor para poder hacer la consultas
        self.__cursorDB = self.__connection.cursor() 

    # Regresa el cursor que se utiliza para la conexion a la 
    # base de datos.
    def getCursor(self):
        return self.__cursorDB
    
    # Ejecuta la instruccion que se le envia como parametro
    def run(self,query):
        self.__cursorDB.execute(query)
        self.__connection.commit()
        self.__connection.close()

