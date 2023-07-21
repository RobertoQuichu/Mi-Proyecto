#Importacion de funciones.´
from tkinter import * 
from CTkMessagebox import CTkMessagebox
from PIL import Image
from views.ventana_de_incio import Aplicacion
import customtkinter, os, json


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
        self.iconbitmap("assets\ondas-sonoras.ico")

        #Centrar ventana.
        window_width = self.winfo_reqwidth()
        window_height = self.winfo_reqheight()
        position_right = int(self.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(self.winfo_screenheight() / 2 - window_height / 2)
        self.geometry(f'+{position_right}+{position_down}')

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

        """ Este metodo muestra la ventana principal, cuando la ventana para ingresar el usario se cierra."""

        #Procesamiento de datos.
        self.deiconify()