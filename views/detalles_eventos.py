#Importacion de funciones.
from models.eventos import Eventos
from models.ubicaciones import Ubicacion
from PIL import Image
import customtkinter

class Detalles_Eventos (customtkinter.CTkFrame) :

    """ """

    def __init__(self, master, evento_seleccionado) :

        """Metodo constructo."""
        
        super().__init__(master) 
        self.master = master
        self.evento_seleccionado = evento_seleccionado
        self.eventos = Eventos.cargar_eventos("data/indice_de_eventos.json")
        self.ubicaciones = Ubicacion.cargar_ubicaciones("data/ubicaciones.json")
        self.imagenes = []

        #Configurar las filas y columnas del CTkFrame
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        #Creacion de un frame para mostrar los detalles del evento.
        self.frame = customtkinter.CTkFrame(self)
        self.frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        #Creacion de un label para mostrar los detalles.
        self.label = customtkinter.CTkLabel(self.frame, text="", font = customtkinter.CTkFont(family="Arial", size=12))
        self.label.grid(pady=20, sticky="nsew")

        #Creacion de un frame para los botones.
        self.button_frame = customtkinter.CTkFrame(self, bg_color = "transparent")
        self.button_frame.grid(row=0, column=2, sticky="ns")

        #Boton de retorno
        self.boton = customtkinter.CTkButton(self.button_frame, text="Volver", command=self.back)
        self.boton.grid(row = 2, column = 0, padx = 10, pady = 10)

        #Boton de reseñas.
        self.boton_reseñas = customtkinter.CTkButton(self.button_frame, text="Escribir una reseña.")
        self.boton_reseñas.grid(row = 3, column=0, padx = 10, pady = 10)

        #Boton para compartir evento en redes sociales.
        self.boton_redes = customtkinter.CTkButton(self.button_frame, text="Compartir en tus redes sociales.")
        self.boton_redes.grid(row = 4, column = 0, padx = 10, pady = 10)

        #Boton para visualizar el mapa.
        self.boton_mapa = customtkinter.CTkButton(self.button_frame, text="Visualizar en un mapa.")
        self.boton_mapa.grid(row = 5, column = 0, padx = 10, pady = 10)

        self.muestra_detalles()

    def muestra_detalles (self) :

        """ """
        info = f"""Nombre: {self.evento_seleccionado.nombre}\nArtista: {self.evento_seleccionado.artista}\nGenero: {self.evento_seleccionado.genero}\n
Ubicacion: {self.evento_seleccionado.ubicacion}\nHora de incio: {self.evento_seleccionado.hora_inicio}\nHora de fin: {self.evento_seleccionado.hora_fin}\n
Descripcion: {self.evento_seleccionado.descripcion}\nImagen: {self.evento_seleccionado.imagen}"""
        self.label["text"] = info
        print(info)

    def cargar_imagenes (self) :

        """ """

        #Procesamiento de datos.
        for evento in self.eventos :
            imagen_evento = customtkinter.CTkImage(light_image = Image.open(f"assets/{evento.imagen}"), size=(200, 200))
            self.imagenes.append(imagen_evento)

    def back (self) :

        """Metodo para volver al frame anterior."""

        self.grid_forget()

