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
    
        #Boton de retorno.
        self.boton = customtkinter.CTkButton(self, text= "Volver", command = self.back)
        self.boton.grid(row = 1, column = 1, sticky = "s")
    def muestra_detalles (self) :

        """"""

    def cargar_imagenes (self) :

        #Procesamiento de datos.
        for evento in self.eventos :
            imagen_evento = customtkinter.CTkImage(light_image = Image.open(f"assets/{evento.imagen}"), size=(200, 200))
            self.imagenes.append(imagen_evento)

    def back (self) :

        """"""

