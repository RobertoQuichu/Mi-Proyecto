#Importacion de funciones.
import customtkinter, os, json
from tkinter import *
from PIL import Image
from CTkMessagebox import CTkMessagebox
from views.ventana_de_incio import Aplicacion
from views.ventana_principal import Inicio_de_app
from views.indice_de_eventos import Indice_de_Eventos

#Definicion de la clase principal.
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#Inicializador de la aplicacion.
if __name__ == '__main__' :

    app = Inicio_de_app()
    app.mainloop()