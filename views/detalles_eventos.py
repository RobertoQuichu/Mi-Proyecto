#Importacion de funciones.
from models.eventos import Eventos
from models.ubicaciones import Ubicacion
from PIL import Image
import customtkinter

class Detalles_Eventos (customtkinter.CTkFrame) :

    """ """

    def __init__(self, master) :

        """Metodo constructo."""
        
        super().__init__(master) 
        self.master = master
        self.eventos = Eventos.cargar_eventos("data/indice_de_eventos.json")
        self.ubicaciones = Ubicacion.cargar_ubicaciones("data/ubicaciones.json")
        self.imagenes = []
            
        #Boton de retorno
        self.boton = customtkinter.CTkButton(self, text= "Volver", command = self.back)
        self.boton.grid(row = 1, column = 2, padx = 10, pady = 10, sticky = "e")

        #Boton de reseñas.
        self.boton_reseñas = customtkinter.CTkButton(self, text = "Escribir una reseña.")
        self.boton_reseñas.grid(row = 2, column = 2, padx = 10, pady = 10, sticky = "e")

        #Boton para compartir evento en redes sociales.
        self.boton_redes = customtkinter.CTkButton(self, text = "Compartir en tus redes sociales.")
        self.boton_redes.grid(row = 3, column = 2, padx = 10, pady = 10, sticky = "e")

        #Boton para visualizar el mapa.
        self.boton_mapa = customtkinter.CTkButton(self, text = "Visualizar en un mapa.")
        self.boton_mapa.grid(row = 4, column = 2, padx = 10, pady = 10, sticky = "e")
    
    def muestra_detalles (self) :

        """ """
        pass

    def cargar_imagenes (self) :

        """ """

        #Procesamiento de datos.
        for evento in self.eventos :
            imagen_evento = customtkinter.CTkImage(light_image = Image.open(f"assets/{evento.imagen}"), size=(200, 200))
            self.imagenes.append(imagen_evento)

    def back (self) :

        """Metodo para volver al frame anterior."""

        self.grid_forget()

