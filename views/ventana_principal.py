#Importacion de funciones.´
from tkinter import * 
from PIL import Image
from views.indice_de_eventos import Indice_de_Eventos
import customtkinter

class Aplicacion (customtkinter.CTk) :

    """ Modelo de clase de la consola. """

    #Declaracion de metodos.
    def __init__ (self) :

        """ Metodo Constructor."""
        super().__init__()

        #Configuracion de la ventana.
        self.title("App Tour Music")
        self.geometry("480x360")
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(1 , weight = 1)
        self.iconbitmap("assets\ondas-sonoras.ico")
        self.config(bg = "#460808")

        #Centrar ventana.
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()
        window_width = self.winfo_reqwidth()
        window_height = self.winfo_reqheight()
        position_right = int(ancho_pantalla / 2 - window_width / 2)
        position_down = int(alto_pantalla / 2 - window_height / 2)
        self.geometry(f'+{position_right}+{position_down}')

        #Carga de imagenes.
        discoteca = customtkinter.CTkImage(light_image = Image.open("assets\discoteca.jpg"), size = (ancho_pantalla, alto_pantalla))
        etiqueta_imagen = customtkinter.CTkLabel(master = self, image= discoteca, text = "")
        etiqueta_imagen.pack()

        #Texto de bienvenida.
        welcome = customtkinter.CTkLabel(self, text = f"Bienvenido a App Music Tour", font = customtkinter.CTkFont(family="Arial", size=15, weight="bold"))
        welcome.place(relx = 0.5, rely = 0.1, anchor = CENTER)

        #Boton de indice de eventos.
        buton = customtkinter.CTkButton(self, text="Indice de eventos", command = self.mostrar_indice_de_eventos)
        buton.place(relx=0.1, rely=0.3, anchor="w")

    def mostrar_indice_de_eventos(self) :

        indice_eventos = Indice_de_Eventos()

