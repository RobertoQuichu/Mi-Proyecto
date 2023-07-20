#Importacion de funciones.
import customtkinter
from tkinter import *
from PIL import Image
from CTkMessagebox import CTkMessagebox
import os  
import json

#Definicion de la clase principal.
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class Inicio_de_app (customtkinter.CTk) :

    """ 
    Esta clase inicia la ventana principal en la cual el usuario ingresara su nombre
    con el cual el programa se referira a el
    
    """

    #Declaracion de metodos.
    def __init__(self) :
        
        """ Metodo constructor. """

        #Procesamiento de datos.
        super().__init__()
        self.title("App Music Tour")
        self.geometry("360x200")
        self.iconbitmap("icon\ondas-sonoras.ico")

        #Creacion de etiqueta.
        self.etiqueta_nombre = customtkinter.CTkLabel(self, text = "Ingrese su nombre: ", font = customtkinter.CTkFont(family = "Arial", size = 12))
        self.etiqueta_nombre.pack(pady = 10)

        #Creacion del campo para el ingreso del nombre.
        self.entrada_nombre = customtkinter.CTkEntry(self)
        self.entrada_nombre.pack(pady = 10) 

        #Creacion de botones de inicio y de cierre.
        self.boton_inicio = customtkinter.CTkButton(self, text = "Iniciar Aplicacion", command = self.iniciar_app)
        self.boton_inicio.pack(pady = 10)
        self.boton_cierre = customtkinter.CTkButton(self, text = "Cerrar Aplicacion", command = self.destroy)
        self.boton_cierre.pack(pady = 5)

    def iniciar_app (self) :

        """ Este metodo da inicio a las comandos principales de la aplicacion."""

        #Procesamiento de datos.
        nombre = self.entrada_nombre.get()
        if nombre :
            self.withdraw() #Oculta la ventana actual.
            self.app = Aplicacion(nombre)
            self.app.protocol("WW_DELETE_WINDOW", self.mostrar_ventana_inicial)
        else :
            CTkMessagebox(title = "Campo Vacio", message = "Por favor ingrese su nombre.")

    def mostrar_ventana_inicial (self):

        """ Este metodo muestra la ventana de inicio cuando la ventana de la aplicación se cierra"""

        #Procesamiento de datos.
        self.deiconify()

class Aplicacion (customtkinter.CTkToplevel):

    """ Modelo de clase de la consola. """

    #Declaracion de metodos.
    def __init__ (self, nombre) :

        """ Metodo Constructor."""
        super().__init__()

        #Configuracion de la ventana.
        self.title("App Tour Music")
        self.geometry("480x360")
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(1 , weight = 1)
        self.iconbitmap("icon\ondas-sonoras.ico")
        self.config(bg = "#460808")
    
        #Obtencion de las dimenciones de la pantalla.
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()

        #Carga de imagenes.
        discoteca = customtkinter.CTkImage(light_image = Image.open("imagen\discoteca.jpg"), size = (ancho_pantalla, alto_pantalla))
        etiqueta_imagen = customtkinter.CTkLabel(master = self, image= discoteca, text = "")
        etiqueta_imagen.pack()

        #Texto de bienvenida.
        welcome = customtkinter.CTkLabel(self, text = f"Bienvenido {nombre}", font = customtkinter.CTkFont(family="Arial", size=22, weight="bold"))
        welcome.place(relx = 0.2, rely = 0.1, anchor = CENTER)

        #Creacion del Boton.
        buton = customtkinter.CTkButton(self, text = "Inicial busqueda")
        buton.place(relx=0.1, rely=0.3, anchor="w")

if __name__ == '__main__' :

    app = Inicio_de_app()
    app.mainloop()