#Importacion de funciones.
from PIL import Image
from tkinter import * 
from views.indice_de_eventos import Indice_de_Eventos
from views.busqueda_y_filtraciones import Busqueda_Filtraciones
from models.usuarios import Usuario
import customtkinter

class Aplicacion (customtkinter.CTkFrame) :

    """ Modelo de clase de la consola. """

    #Declaracion de metodos.
    def __init__ (self, master, nombre, apellido) :

        """ Metodo Constructor."""
        super().__init__(master)
        
        #Configuracion de la ventana.
        self.master = master
        self.nombre = nombre
        self.apellido = apellido

        #Texto de bienvenida.
        self.frame_bienvenida = customtkinter.CTkFrame(self)
        self.frame_bienvenida.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "w")
        self.frame_bienvenida.grid_columnconfigure(0, weight = 1)
        self.welcome = customtkinter.CTkLabel(self.frame_bienvenida, text = f"Bienvenido {self.nombre} {self.apellido}", font = customtkinter.CTkFont(family="Arial", size=18, weight="bold"))
        self.welcome.grid(row = 0, column = 0)
        
        #Definicion de botones
        self.frame_boton = customtkinter.CTkFrame(self)
        self.frame_boton.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "w")
        self.buton = customtkinter.CTkButton(self.frame_boton, text = "Indice de eventos", command = self.eventos_detalles)
        self.buton.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.buton_historial = customtkinter.CTkButton(self.frame_boton, text = "Historial de Eventos Asistidos", command = self.eventos_asistidos)
        self.buton_historial.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.buton_busqueda = customtkinter.CTkButton(self.frame_boton, text = "Busqueda y Filtrado", command = self.busqueda_filtraciones)
        self.buton_busqueda.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.boton_salir = customtkinter.CTkButton(self.frame_boton, text = "Salir", command = self.master.destroy)
        self.boton_salir.grid(row = 4, column = 0, padx = 10, pady = 10)
        self.boton_volver = customtkinter.CTkButton(self.frame_boton, text = "Volver a iniciar sesion", command = self.new_sesion)
        self.boton_volver.grid(row = 3, column = 0, padx = 10, pady = 10)

        #Frame de imagen.
        self.frame_imagen2 = customtkinter.CTkFrame(self)
        self.frame_imagen2.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.imagen2 = customtkinter.CTkImage(light_image=Image.open("data/palera.jpg"), size=(300, 400))
        self.imagen_label2 = customtkinter.CTkLabel(master=self.frame_imagen, image=self.imagen, text="")
        self.imagen_label2.grid(padx=10, pady=10)

    def eventos_detalles (self) :

        """ Metodo por el cual se invoca a l a clase Indice_de_eventos."""
        
        #Procesamiento de datos.
        indice_eventos = Indice_de_Eventos(self)

    def busqueda_filtraciones (self) :

        """ Metodo por el cual se invoca a la clase Busqueda_Filtraciones."""

        #Procesamiento de datos.
        busqueda_filtracio = Busqueda_Filtraciones(self)

    def eventos_asistidos (self) :

        """ Este metodo invoca a la clase Historial_Eventos_Asistidos.""" 
                    
        #Creacion de un Label transparente.
        self.label = customtkinter.CTkFrame(self, width = 250, height = 150)
        self.label.grid(row = 1, column = 1, padx = 40, pady = 30)    
        datos_usuarios = Usuario.cargar_usuarios("data/nombre_usuarios")
        #if (apellido == datos_usuarios.apellido and nombre == datos_usuarios.nombre) :


    def new_sesion (self) :

        self.grid_forget()