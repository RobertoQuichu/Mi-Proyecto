#Importacion de funciones.
from tkinter import *
import customtkinter

#Declaracion de clases.
class Busqueda_Filtraciones(customtkinter.CTkToplevel) :

    """ """

    #Declaracion de metodos.
    def __init__ (self, ventana) :
        
        """Metodo Constructor."""
        super().__init__(ventana)
        self.title("Busque y Filtraciones.")
        self.geometry("360x300")
        

        #Creacion de un Frame para colocar los widgets.
        frame = customtkinter.CTkFrame(self)
        frame.grid(row=0, column=0, sticky="nsew", padx = 10, pady = 10) 

        #Configurar las filas y columnas de la ventana principal para que el frame ocupe todo el espacio disponible.
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #Configurar las filas y columnas del frame para que el contenido se expanda en todas las direcciones.
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        #Etiqueda de busqueda.
        self.etiqueta_busqueda = customtkinter.CTkLabel(frame, text = "Seleccione el tipo de busqueda que desea ")
        