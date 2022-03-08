#Conectar python con postgresl
# Debemos de instalar el siguiente paquete por consola
#   pip install psycopg 

#import psycopg
#conexion = psycopg2.connect(databas)



## -------------- Conexion con SQLite
import sqlite3

# Creamos la conexion a la base de datos
conextion = sqlite3.connect('first')

#Creamos un cursor (Para hacer la consultas)
cursorDB = conextion.cursor() 
#Creamos una tabla nueva
#cursorDB.execute(
#    """
#        CREATE TABLE person(
#            keyPerson varchar(15) PRIMARY KEY,  
#            name varchar(15),
#            number int
#        ) 
#    """
#)

##Inserta un solo valor
#cursorDB.execute(
#    """
#        INSERT INTO person VALUES('QWERTY_1','Alexis',10)
#    """
#)

#Insertamos valores en la tabla
rows = [
    ("QWERTY_2","Name 2",12),
    ("QWERTY_3","Name 3",13),
    ("QWERTY_4","Name 4",14),
    ("QWERTY_5","Name 5",15),
    ("QWERTY_6","Name 6",16),
    ("QWERTY_7","Name 7",17),
    ("QWERTY_8","Name 8",18),
    ("QWERTY_9","Name 9",19),
    ("QWERTY_10","Name 10",20),
    ("QWERTY_11","Name 11",21),
    ("QWERTY_14","Name 11",22),
    ("QWERTY_15","Name 11",23),
    ("QWERTY_16","Name 11",24),
    ("QWERTY_17","Name 11",25),
    ("QWERTY_18","Name 11",26),
    ("QWERTY_19","Name 11",27),
    ("QWERTY_20","Name 11",28),
    ("QWERTY_21","Name 11",29)
]

##Insertamos multiples valores.
#cursorDB.executemany("INSERT INTO person VALUES(?,?,?)",rows)

## seleccionamos las filas
cursorDB.execute("SELECT * FROM person")
rowsDB = cursorDB.fetchall()
for row_DB in rowsDB :
    print( row_DB[0] )  

#Confirmamos el cambio en la tabla
conextion.commit()

#Cerramos la conexion a ala base de datos.
conextion.close()


##Video 57 
