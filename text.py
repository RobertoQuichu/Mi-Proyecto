from tkinter import *

def obtener_texto () :
    texto = cuadro_texto.get("1.0", END)
    etiqueta.config(text = texto)

#Creacion de la ventana
ventana = Tk()

#Creamos un widget
cuadro_texto = Text(ventana, height=5, width=30)
cuadro_texto.insert(END, "escribe algo aqui...")
cuadro_texto.pack()
boton = Button(ventana, text="Obtener texto", command=obtener_texto)
boton.pack()
etiqueta = Label(ventana, text="", wraplength=200)
etiqueta.pack()
ventana.mainloop()