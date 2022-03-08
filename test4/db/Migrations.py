# Archivo que contendra una clase con un metodo para generar las tablas 
# para la base de datos.
import sys
sys.path.append(sys.path[0] + '\\..\\')
from controllers.db.SQLiteController import *

class Migrations():
    def __init__(self):
        self.__sql = SQLiteContoller()
        
    def createTables(self):
        tables = {
            'persona': f"""
                        CREATE TABLE 'persona'(
                            keyStr VARCHAR(30) PRIMARY KEY,
                            name TEXT,
                            age INT
                        )""",
            
        }
        return tables 

    # Envia la instrucciones SQL a ser ejecutadas    
    def sendTables(self):
        tablesQuery = self.createTables()
        for item in tablesQuery.items():
            self.__sql.run(item[1])
            print(f"""Tabla: ->{item[0]}, creada exitosamente""")
