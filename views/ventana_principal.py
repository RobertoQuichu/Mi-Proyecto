#Importacion de funciones.
from PIL import Image, ImageTk
from tkinter import * 
from views.indice_de_eventos import Indice_de_Eventos
from views.busqueda_y_filtraciones import Busqueda_Filtraciones
from models.usuarios import Usuario
import customtkinter

class Aplicacion (customtkinter.CTkFrame) :

    """ Modelo de clase de la consola. """

    #Declaracion de metodos.
    def __init__ (self, master, inicio_sesion, controlador = None) :

        """ Metodo Constructor."""
        super().__init__(master)
        
        #Configuracion de la ventana.
        self.controller = controlador
        self.master = master
        self.inicio_sesion = inicio_sesion
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

        #Frame principal
        self.framepri = customtkinter.CTkFrame(self)
        self.framepri.grid(row = 0, column = 0, sticky = "snew")
        self.framepri.grid_columnconfigure(0, weight = 1)
        self.framepri.grid_rowconfigure(0, weight = 1)

        # Obtener el usuario actual del controlador de datos y mostrarlo en el texto de bienvenida.
        usuario_actual = self.controller.get_usuario_actual()
        nombre = usuario_actual.nombre
        apellido = usuario_actual.apellido

        #Texto de bienvenida.
        self.frame_bienvenida = customtkinter.CTkFrame(self.framepri)
        self.frame_bienvenida.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "w")
        self.welcome = customtkinter.CTkLabel(self.frame_bienvenida, text = f"Bienvenido {nombre} {apellido}", font = customtkinter.CTkFont(family="Arial", size=18, weight="bold", underline = True, slant = "italic"))
        self.welcome.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        #Definicion de botones
        self.frame_boton = customtkinter.CTkFrame(self.frame_bienvenida, fg_color="transparent")
        self.frame_boton.grid(row = 1, column = 0, padx = 5, pady = 5)
        
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
        """self.frame_imagen = customtkinter.CTkFrame(self.framepri)
        self.frame_imagen.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.imagen2 = customtkinter.CTkImage(light_image = Image.open("data/palera.jpg"), size = (300, 400))
        self.imagen_label = customtkinter.CTkLabel(master=self.frame_imagen, image=self.imagen2, text="")
        self.imagen_label.grid(padx=10, pady=10)"""

    def eventos_detalles (self) :

        """ Metodo por el cual se invoca a l a clase Indice_de_eventos."""
        
        #Procesamiento de datos.
        indice_eventos = Indice_de_Eventos(self, self.controller)
        id_usuario_actual = self.controller.get_usuario_actual().id
        print( id_usuario_actual)

    def busqueda_filtraciones (self) :

        """ Metodo por el cual se invoca a la clase Busqueda_Filtraciones."""

        #Procesamiento de datos.
        busqueda_filtracio = Busqueda_Filtraciones(self, self.controller)

    def eventos_asistidos (self) :

        """ Este metodo invoca a la clase Historial_Eventos_Asistidos.""" 
                    
        #Creacion de un Label transparente.
        self.label = customtkinter.CTkFrame(self.framepri, width = 250, height = 150)
        self.label.grid(row = 1, column = 1, padx = 40, pady = 30)    
        datos_usuarios = Usuario.cargar_usuarios("data/nombre_usuarios")
        #if (apellido == datos_usuarios.apellido and nombre == datos_usuarios.nombre) :

    def new_sesion (self) :

        print("Holis")
        self.framepri.grid_remove()
        self.inicio_sesion.volver_inicio_sesion()