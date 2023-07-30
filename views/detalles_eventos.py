#Importacion de funciones.
from models.eventos import Eventos
from models.ubicaciones import Ubicacion
from PIL import Image
from views.rewies import Rewies
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
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

        #Creacion de un frame principal.
        self.frame_pri = customtkinter.CTkFrame(self)
        self.frame_pri.grid(row = 0, column = 0, sticky = "snew")

        #Configurar las filas y columnas del CTkFrame
        self.frame_pri.grid_rowconfigure(0, weight=1)
        self.frame_pri.grid_columnconfigure(0, weight=1)

        #Creacion de un frame para mostrar los detalles del evento.
        self.scroll = customtkinter.CTkScrollableFrame(self.frame_pri, orientation = "horizontal")
        self.scroll.grid(row=0, column=0, columnspan=2, sticky="nsew", padx = 5, pady = 5)

        #Creacion de un frame para los botones.
        self.button_frame = customtkinter.CTkFrame(self.frame_pri, bg_color = "transparent")
        self.button_frame.grid(row=0, column=2, sticky="ns", padx = 5, pady = 5)

        #Boton de retorno
        self.boton = customtkinter.CTkButton(self.button_frame, text="Volver", command=self.back)
        self.boton.grid(row = 2, column = 0, padx = 10, pady = 10)

        #Boton de reseñas.
        self.boton_reseñas = customtkinter.CTkButton(self.button_frame, text="Escribir una reseña.", command = self.resenas_rewies)
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

        customtkinter.CTkLabel(self.scroll, text=f"Artista: {self.evento_seleccionado.artista}").grid(sticky = "w")
        customtkinter.CTkLabel(self.scroll, text=f"Género: {self.evento_seleccionado.genero}").grid(sticky = "w")
        customtkinter.CTkLabel(self.scroll, text=f"Ubicación: {self.evento_seleccionado.ubicacion}").grid(sticky = "w")
        customtkinter.CTkLabel(self.scroll, text=f"Hora de inicio: {self.evento_seleccionado.hora_inicio}").grid(sticky = "w")
        customtkinter.CTkLabel(self.scroll, text=f"Hora de fin: {self.evento_seleccionado.hora_fin}").grid(sticky = "w")
        customtkinter.CTkLabel(self.scroll, text=f"Descripción: {self.evento_seleccionado.descripcion}").grid(sticky = "w")

    def cargar_imagenes (self) :

        """ """

        #Procesamiento de datos.
        for evento in self.eventos :
            imagen_evento = customtkinter.CTkImage(light_image = Image.open(f"assets/{evento.imagen}"), size=(200, 200))
            self.imagenes.append(imagen_evento)

    def back (self) :

        """Metodo para volver al frame anterior."""

        self.grid_forget()

    def resenas_rewies (self) :
        
        self.frame_pri.grid_forget()
        self.resenas = Rewies(self, self.evento_seleccionado, self)
        self.resenas.grid(row = 0, column = 0, sticky = "snew")

    def volver_desde_rewies(self) :

        self.resenas.grid_forget()  # Oculta el frame de Rewies
        self.frame_pri.grid(row=0, column=0, sticky="snew")  # Vuelve a mostrar el frame de Detalles_Eventos