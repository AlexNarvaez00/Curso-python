# interfaces graficas de usuarios.print
# Para poder hacer las ventas utilizaremos 
# TKinder -> Que al menos funciona en Windows
from textwrap import fill
from tkinter import * 
import sys
sys.path.append(sys.path[0] + '\\..\\')
from controllers.PersonController import *




root = Tk() ##Instanciamos una ventana
root.title('Crud tabla persona')
root.geometry("750x500") #ANCHO Y ALTO DELA VENTA

#Creamos un frame que ira dentro de la venta
panel = Frame()
panel.pack(
        fill="both",
        expand="True")
panel.config(width=750,height=500)

# ---------------------------------------------------------
#Creamos una etiqueta
etiquetaKey = Label(panel,text="Llave primaria:")
#Indicamos en que posicion de la cuadricula queremos el elementos
#sticky="e" Es para alinear el texto de l etiqueta  a la derecha 
etiquetaKey.grid(
        row=1,
        column=0,
        sticky="e",
        padx=15,
        pady=5)

#Creamos una caja de texto para ingresar texto
inputTextKey = Entry(panel)
inputTextKey.grid(row=1,column=1)

# ---------------------------------------------------------
#Creamos una etiqueta
etiquetaName = Label(panel,text="Nombre:")
#Indicamos en que posicion de la cuadricula queremos el elementos
#sticky="e" Es para alinear el texto de l etiqueta  a la derecha 
etiquetaName.grid(
        row=2,
        column=0,
        sticky="e",
        padx=15,
        pady=5)

#Creamos una caja de texto para ingresar texto
inputTextName = Entry(panel)
inputTextName.grid(row=2,column=1)


# --------------------------------------------------------------------------------
## edad.
#Creamos una etiqueta
etiquetaAge = Label(panel,text="Edad:")
#Indicamos en que posicion de la cuadricula queremos el elementos
#sticky="e" Es para alinear el texto de l etiqueta  a la derecha 
etiquetaAge.grid(
        row=3,
        column=0,
        sticky="e",
        padx=15,
        pady=5)

#Creamos una caja de texto para ingresar texto
inputTextAge = Entry(panel)
inputTextAge.grid(row=3,column=1)

# ------------------------------------------------------
# Definimos el boton
boton = Button(panel,text="Guardar",command=lambda:insert(
        inputTextKey.get(),
        inputTextName.get(),
        inputTextAge.get()))
boton.grid(
        row=4,
        column=1,
        padx=15,
        pady=5)


# Definimos la lista donde se mostraran los elementos.
listView = Listbox(panel)



##Esta funcion debe de ir al siempre la final
root.mainloop() ##Este metodo es para mantener la venta en pantall 
