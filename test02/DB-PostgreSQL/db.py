# Segunda prueba para conectar python con PostgreSQL
# Ejecutamos los siguiente comandos en la consola.
#  -> 
# pip install --upgrade pip 
# pip install psycopg
# pip install psycopg2
import psycopg

#Creamos la conexion a la base de datos.
conexion = psycopg.connect(
        dbname="laravelIG",
        user="postgres",
        password="narvaez",
        host="localhost",
        port="5433")
#Creamos el cursor 
cursorDB = conexion.cursor()
#Consulta
query  = """SELECT * FROM venta"""
cursorDB.execute(query)
#Recuperamos los elementos
listDB_venta = cursorDB.fetchall()
conexion.close()
for row in listDB_venta:
    print(row)
