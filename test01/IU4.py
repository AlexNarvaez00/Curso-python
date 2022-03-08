from tkinter import *


root = Tk()

## ----------------- Variable global
numberOption = IntVar()
valeCheck = [
    StringVar(),
    StringVar(),
    StringVar()
]

## ----------------- Eventos
def botonClick():
    print(numberOption.get())

def clickCheck():
    global valeCheck
    print(valeCheck[0].get())

## ----------------- Radio buttons
array = ["Hombre","Mujer"] 
for radio in array:
    radioButton = Radiobutton(
        root,
        text=radio,
        value=array.index(radio),
        variable=numberOption,
        command=botonClick )
    radioButton.pack()

## -------------------- Check buttons
arrayMultiple = ["Animales","Juegos","cine"]
for check in arrayMultiple:
    checkButton = Checkbutton(root,text=check)
    checkButton.pack()
    checkButton.config(
        command=clickCheck,
        variable=valeCheck[arrayMultiple.index(check)],
        offvalue=0,
        onvalue=check)






root.mainloop()


#video 50,51,52 