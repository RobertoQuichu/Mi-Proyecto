#Importacion de funciones.
from tkinter import *
from models.eventos import Eventos 
from models.ubicaciones import Ubicacion
import customtkinter
import json

class Indice_de_Eventos (customtkinter.CTkToplevel) :

    """ """

    #Declaracion de Metodos.
    def __init__(self) :

        """ Metodo constructor de la clase Indice_de_Eventos"""

        super().__init__()
        self.title("Indice de eventos")
        self.geometry("360x240")
        self.iconbitmap("assets\ondas-sonoras.ico")
        self.eventos = Eventos.cargar_eventos("data/indice_de_eventos.json")
        self.ubicaciones = Ubicacion.cargar_ubicaciones("data/ubicaciones.json")
        



