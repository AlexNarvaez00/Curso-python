# Archivo para crear el patron de diseño singleton.
# Puede mejorar
# Observaciones
# -> Se debe de tener uan variable provada-estatica para crear el objeto.
# -> Debe de ir en la caprte de patterns
import psycopg
from config  import * 
class SingletonDB() :
    # Constructor de la clase
    def __init__(self,name,port,host,user,password):
        self.__connection = psycopg.connect(
            dbname=name,
            user=user,
            port=port,
            host=host,
            password=password)
        self.__nameConexion = f"{name}"
    
    # Regresa un objeto de conexion a la base de datos
    @staticmethod
    def getInstance():
        SingletonDBVar = SingletonDB(nameDataBase,portDataBase,hostNameDataBase,userDataBase,passwordDataBase) 
        return SingletonDBVar

    def getConnection(self):
        return self.__connection


    # Cierra la conexion
    def close(self):
        self.__connection.close()  

    # Convierte el objeto en un string    
    def __str__(self):
        return f"{self.__nameConexion}: {self.__connection}"

