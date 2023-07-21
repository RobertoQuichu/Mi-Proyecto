from tkinter import *

def suma() :
    num1 = numero1.get()
    num2 = numero2.get()
    suma = num1 + num2
    etiqueta.config(text = "suma: {}".format(suma))

ventana = Tk()
ventana.geometry("200x200")
numero1 = IntVar()
numero2 = IntVar()
entry1 = Entry(ventana, textvariable=numero1)
entry2 = Entry(ventana, textvariable=numero2)
entry1.grid(column=0, row=0, padx = 10, pady=10)
entry2.grid(row=1, column=0, padx  =10, pady=10)
boton = Button(ventana, text="sumar", command=suma)
boton.grid(row=2, column=0, padx=10, pady=10)
etiqueta = Label(ventana, text='')
etiqueta.grid(row=3, column=0)
ventana.mainloop()