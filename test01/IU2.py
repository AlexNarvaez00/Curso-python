# interfaces graficas de usuarios.print
# Para poder hacer las ventas utilizaremos 
# TKinder -> Que al menos funciona en Windows
from textwrap import fill
from tkinter import * 

root = Tk() ##Instanciamos una ventana
root.title('Pantalla principal')
root.geometry("750x500") #ANCHO Y ALTO DELA VENTA


#Creamos el frame
frame = Frame()
frame.pack(
        fill="both",
        expand="True")
frame.config(width=750,height=500)

## ----------------------------------------------------------
#Creamos una caja de texto para ingresar texto
inputText = Entry(frame)
#Indicamos en que posicion de la cuadricula queremos el elementos
inputText.grid(row=0,column=1)

#Creamos una etiqueta
etiqueta = Label(frame,text="Nombre de usuario:")
#Indicamos en que posicion de la cuadricula queremos el elementos
#sticky="e" Es para alinear el texto de l etiqueta  a la derecha 
etiqueta.grid(
        row=0,
        column=0,
        sticky="e",
        padx=15,
        pady=5)

## ----------------------------------------------------------
#Creamos una caja de texto para ingresar texto
inputText2 = Entry(frame)
#Indicamos en que posicion de la cuadricula queremos el elementos
inputText2.grid(row=1,column=1)
inputText2.config(show="*")

#Creamos una etiqueta
etiqueta = Label(frame,text="Contraseña de usuario:")
#Indicamos en que posicion de la cuadricula queremos el elementos
etiqueta.grid(
        row=1,
        column=0,
        sticky="e",
        padx=15,
        pady=5)


##Esta funcion debe de ir al siempre la final
root.mainloop() ##Este metodo es para mantener la venta en pantall 





#Video 45