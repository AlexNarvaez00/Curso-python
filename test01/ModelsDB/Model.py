#Modelo para crear objetos haciendo peticiones a una base de datos.

class Model():

    # Constructor de la clase
    def __init__(self,nameTable,values):
        self.__nameTable = nameTable
        # Valores del registro
        # debe de ser un arreglo
        self.__values = values
        
        self.__queryInsertStr = self.__queryInsert()
    
    # ------------------------- Funciones de instancia -------------------------

    # Guarda el elemento en la base de datos.
    # si el elemento ya existe, lo actualiza
    def save(self):
        pass 
    
    # Borra el elemento en la base de datos.
    def delete(self):
        pass

    # Funcion que crea la instruccion de insercion de datos en la base de datos.
    def __queryInsert(self):
        cantidadSingnos = len(self.__values)
        strSignos = '?,' * cantidadSingnos
        signos = strSignos[ 0 : len(strSignos) - 1 ]
        return f"""INSERT INTO "{self.__nameTable}" VALUES ({signos})"""
    
    # Regresa la instruccion de "INSERT..." de SQL
    def getInsert(self):
        return self.__queryInsert()

    # Establece el valor de en la posicion dada para 
    # guardarla en la base de datos  
    def setValue(self,pos,value):
        if (pos < len(self.__values)):
            self.__values[pos] = value
        else:
            self.__values.append(value) 

    def __str__(self):
        return f""": {self.__values}"""





    # Establece el valor de un atributo
    # Params
    # @var str attribute  -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x Componer
    #  ----------> SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'Person'
    #   Nombre del atributo a insertar en la tabla,
    #   si el atributo no existe lo agrega, pero puede
    #   generar un error
    def set(self,attribute,value):
        index = self.__values.index(value)
        if ( index >= 0):
            self.__values[index] = value 
        else:
            self.__values.append(value)
    # ---------------------- Getter y Setters ----------------------
    def getNameTable(self):
        return self.__nameTable

