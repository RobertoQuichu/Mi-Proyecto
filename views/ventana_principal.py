#Importacion de funciones.´
from tkinter import * 
from PIL import Image
from views.indice_de_eventos import Indice_de_Eventos
from views.busqueda_y_filtraciones import Busqueda_Filtraciones
from models.usuarios import Usuario
import customtkinter

class Aplicacion (customtkinter.CTkToplevel):

    """ Modelo de clase de la consola. """

    #Declaracion de metodos.
    def __init__ (self, nombre, apellido) :

        """ Metodo Constructor."""
        super().__init__()
        
        #Configuracion de la ventana.
        self.title("App Tour Music")
        self.geometry("480x360")
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(1 , weight = 1)
        self.iconbitmap("assets\ondas-sonoras.ico")
        self.config(bg = "#460808")
        self.nombre = nombre
        self.apellido = apellido

        #Centrar ventana.
        window_width = self.winfo_reqwidth()
        window_height = self.winfo_reqheight()
        position_right = int(self.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(self.winfo_screenheight() / 2 - window_height / 2)
        self.geometry(f'+{position_right}+{position_down}')
        
        #Obtencion de las dimenciones de la pantalla.
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()
        
        #Carga de imagenes.
        discoteca = customtkinter.CTkImage(light_image = Image.open("assets\discoteca.jpg"), size = (ancho_pantalla, alto_pantalla))
        etiqueta_imagen = customtkinter.CTkLabel(master = self, image= discoteca, text = "")
        etiqueta_imagen.pack()

        #Texto de bienvenida.
        welcome = customtkinter.CTkLabel(self, text = f"Bienvenido {nombre} {apellido}", font = customtkinter.CTkFont(family="Arial", size=22, weight="bold"))
        welcome.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        
        #Definicion de botones
        buton = customtkinter.CTkButton(self, text = "Indice de eventos", command = self.eventos_detalles)
        buton.place(relx=0.1, rely=0.3, anchor="w")
        buton_historial = customtkinter.CTkButton(self, text = "Historial de Eventos Asistidos", command = self.eventos_asistidos)
        buton_historial.place(relx = 0.1, rely = 0.6, anchor = "w")
        buton_busqueda = customtkinter.CTkButton(self, text = "Busqueda y Filtrado", command = self.busqueda_filtraciones)
        buton_busqueda.place(relx = 0.1, rely = 0.9, anchor = "w")

        #Creacion de un Label transparente.
        label = customtkinter.CTkLabel(self, text = "HOla", bg = "#E5E5E5")
        label.place(relx = 0.5, rely = 0.6, anchor = "w")    
    def eventos_detalles (self) :

        """ Metodo por el cual se invoca a la clase Indice_de_eventos."""
        
        #Procesamiento de datos.
        indice_eventos = Indice_de_Eventos(self)

    def busqueda_filtraciones (self) :

        """ Metodo por el cual se invoca a la clase Busqueda_Filtraciones."""

        #Procesamiento de datos.
        busqueda_filtracio = Busqueda_Filtraciones(self)

    def eventos_asistidos (self) :

        """ Este metodo invoca a la clase Historial_Eventos_Asistidos."""

        #Procesamiento de datos.
        datos_usuarios = Usuario.cargar_usuarios("data/nombre_usuarios")
        #if (apellido == datos_usuarios.apellido and nombre == datos_usuarios.nombre) :


