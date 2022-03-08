# interfaces graficas de usuarios.print
# Para poder hacer las ventas utilizaremos 
# TKinder -> Que al menos funciona en Windows
from textwrap import fill
from tkinter import * 

root = Tk() ##Instanciamos una ventana
root.title('Pantalla principal')
#root.geometry("750x500") #ANCHO Y ALTO DELA VENTA


#Creamos un frame que ira dentro de la venta
panel = Frame() 
#La opcion de fill rellena toda la venta segun el Eje
panel.pack(
        fill="both",
        expand="True")
panel.config(
        width=750,
        height=500,
        background="red")

##Esta funcion debe de ir al siempre la final
root.mainloop() ##Este metodo es para mantener la venta en pantall 





#Video 44
