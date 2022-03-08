# Clase "Modelo", esta clase lo que trata de "imitar" el modelo que se implementa en PHP
# (laravel).

import sys
sys.path.append(sys.path[0] + '\\..\\')

from controllers.db.SQLiteController import * 

class Model():

    # Constructor de la clase.
    # constructor simple
    def __init__(self):
        self.__init__(None)

    # Constructor de la clase.
    # constructor que inicializa la llave primaria
    def __init__(self,primaryKey):
        self.__init__(primaryKey,None)

    # Constructor de la clase.
    # constructor que inicializa la llave primaria, el nombre de la tabla
    def __init__(self,tableName,primaryKey,values):      
        # Nombre de la tabla,
        # es un nombre inmutable
        self.__tableName = tableName

        # Nombre de la llave primaria.
        self.__primaryKey = primaryKey

        # Diccionario para gardar el nombre de 
        # las columnas y el valor.
        self.__columns = {}

        # Objeto que abre la conexion a la base de datos
        self.__objeSQL = SQLiteContoller()

        # Valores de la tupla.
        self.__values = values


    # Funciones de instancia. -------------------------------------------------------------------

    def getTuple(self):
        return self.__values

    # Funcion para establecer a llave primaria de la tabla.
    def setPrimaryKey(self,column):
        self.__primaryKey = column

    # Establece el valor para la columna dada
    def setValueColumn(self,column,value):
        self.__columns[column] = value

    # Guarda el registro en la tabla
    def save(self):
        namesColummns = list(self.__columns.keys())
        values = list(self.__columns.values())

        namesColummnsStr = str(namesColummns).replace('[','').replace(']','')
        valuesStr = str(values).replace('[','').replace(']','')
        
        query = f"""INSERT INTO '{self.__tableName}' ({namesColummnsStr}) VALUES ({valuesStr})"""
        
        self.__objeSQL.run(query)

    # Elimina el registro de la tabla
    def delete(self):
        query = f"""DELETE FROM '{self.__tableName}' WHERE {self.__primaryKey}={self.__columns[self.__primaryKey]}"""
        self.__objeSQL.run(query)

    # Funcion que transforma el objeto en un string
    def __str__(self):
        values = ""
        if (self.__values == None):
            values = f"""Columnas: {list(self.__columns.keys())}"""
        else:
            values = f"""Valores: {self.__values}"""                
        return f""": Nombre: {self.__tableName}, Llave primaria: {self.__primaryKey}, Columnas: {values}"""

    ## --------------- Funciones estaticas ---------------------------------------------------------
    @staticmethod
    def list(nameClass,tableName):
        listElements = []
        query = f""" SELECT * FROM '{tableName}' """
        SQLObject = SQLiteContoller()
        SQLObject.getCursor().execute(query)
        rowsTable = SQLObject.getCursor().fetchall()
        print(rowsTable)
        for tupleInformation in rowsTable:
            modelObject = nameClass(tupleInformation)
            listElements.append(modelObject)
            print(tupleInformation)
        return listElements
