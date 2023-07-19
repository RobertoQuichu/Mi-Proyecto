#Importacion de funciones.
import customtkinter
from tkinter import *
from PIL import Image
import os  

#Definicion de la clase principal.
customtkinter.set_appearance_mode("System")
class Aplicacion :

    """ Modelo de clase de la consola. """

    #Declaracion de metodos.
    def __init__ (self, ventana) :

        """ Metodo Constructor."""
        self.ventana = ventana

        #Configuracion de la ventana.
        self.ventana.title("App Tour Music")
        self.ventana.geometry("720x480")
        self.ventana.grid_rowconfigure(0, weight = 1)
        self.ventana.grid_columnconfigure(1 , weight = 1)
        self.ventana.iconbitmap("icon\ondas-sonoras.ico")
        self.ventana.config(bg = "#460808")
    
        #Obtencion de las dimenciones de la pantalla.
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()

        #Carga de imagenes.
        discoteca = customtkinter.CTkImage(light_image = Image.open("imagen\discoteca.jpg"), size = (ancho_pantalla, alto_pantalla))
        etiqueta_imagen = customtkinter.CTkLabel(master = self.ventana, image= discoteca, text = "")
        etiqueta_imagen.pack()

        #Creacion de un boton.
        buton = customtkinter.CTkButton(self.ventana, text = "Inicial busqueda")
        buton.place(relx=0.1, rely=0.5, anchor="w")

if __name__ == '__main__' :

    ventana_principal = customtkinter.CTk()
    app = Aplicacion(ventana_principal)
    ventana_principal.mainloop()