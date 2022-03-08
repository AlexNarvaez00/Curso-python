#Crear una calculadora usando python
from cgitb import text
from tkinter import * 
import functools
# --------------- Interfaz grafica
root = Tk() ##Instanciamos una ventana
root.title('Pantalla principal')
#root.geometry("750x500") #ANCHO Y ALTO DELA VENTA

#Creamos el frame
frame = Frame()
frame.pack(
        fill="both",
        expand="True")
#frame.config(width=750,height=500)

#---------------- Variables 
numeroPantall = StringVar()
operacion = ""
resultado = 0


#Creamos la caja de texto
screen = Entry(frame,width=40,textvariable=numeroPantall) 
screen.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    columnspan=4)

screen.config(
    justify="right")


## ------------------------------- Zona de funciones 
def click(number) :
    numeroPantall.set(numeroPantall.get()+str(number))

def operacion(opera) :
    global operaciones
    global resultado
    operaciones = opera
    resultado = float(numeroPantall.get())
    numeroPantall.set('')
    
    ##print(operaciones)
    ##print(resultado)

def setResultado():
    global resultado
    global operaciones
    resultadoTemp = resultado
    if operaciones == "*" :
        resultadoTemp = resultadoTemp * float(numeroPantall.get())
    if operaciones == "-" :
        resultadoTemp = resultadoTemp - float(numeroPantall.get())
    if operaciones == "+" :
        resultadoTemp = resultadoTemp + float(numeroPantall.get())
    if operaciones == "/" :
        resultadoTemp = resultadoTemp / float(numeroPantall.get())
    numeroPantall.set(resultadoTemp)
    resultado = 0


#Creamos un arreglo de botones
buttons = []
columnTemp = 0
for index in range(9):
    tempButton = Button(frame,text=f"{index}",width=10)
    
    tempButton.config(command=functools.partial(click,index))
    tempButton.grid(
        row = int(index / 3) + 1,
        column = columnTemp 
    )
    columnTemp+= 1
    if columnTemp > 2 :
        columnTemp = 0
    buttons.append(tempButton)

#Botones de las operaciones
operaciones = ["*","+","/","-"]
for text in operaciones:
    tempButton = Button(frame,text=text,width=10)
    tempButton.config(command=functools.partial(operacion,text))
    tempButton.grid(
        column=3,
        row = operaciones.index(text) +1
    )

#Boton de igual
igual = Button(frame,text="=",width=10)
igual.grid(
        column=0,
        row = 4,
        columnspan=3
    )
igual.config(command=setResultado)


##Esta funcion debe de ir al siempre al final
root.mainloop() ##Este metodo es para mantener la venta en pantall 


#Video 47