#Importacion de funciones.
from controller.centrar_ventanas import Centrar_Ventana
from models.eventos import Eventos
from models.ubicaciones import  Ubicacion
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk
from tkinter import *
import customtkinter

#Declaracion de clases.
class Mapas_Planificacion (customtkinter.CTkToplevel) :

    """ 
    Esta clase mostrara una ventana emergente que permitira visualizar la ubicacion del evento 
    y poder planificar una ruta hasta el evento

    """
    def __init__(self, ventana, seleccionar_evento_callback=None, seleccionar_ubicacion_callback=None):
        super().__init__(ventana)
        self.seleccionar_local_callback = seleccionar_evento_callback
        self.seleccionar_ubicacion_callback = seleccionar_ubicacion_callback
        self.title("Mapa y Planificion de Rutas")
        Centrar_Ventana.centrar(self)
        self.geometry("720x480")

        #Carga de datos.
        self.evento = Eventos.cargar_eventos("data/indice_de_eventos.json")
        self.ubicaciones = Ubicacion.cargar_ubicaciones("data/ubicaciones.json")

        #Creacion de un frame para el mapa
        self.frame_mapa = customtkinter.CTkFrame(self)
        self.frame_mapa.grid(row = 0, column = 0, sticky = "snew")
        self.frame_mapa.grid_columnconfigure(0, weight = 1)
        self.mapa = TkinterMapView(self.frame_mapa, width=600, height=600, corner_radius=0)
        self.mapa.set_position(-24.77616437851034, -65.41079411004006)
        self.mapa.set_zoom(16)
        self.mapa.grid(sticky = "snew")

        #Frame para una listbox.
        self.frame_listbxo = customtkinter.CTkFrame(self)
        self.frame_listbxo.grid(row = 0, column = 1, sticky = "snew", padx = 10, pady = 10)
        self.frame_listbxo.grid_columnconfigure(1, weight = 1)
        self.listbox = Listbox(self.frame_listbxo, width = 30)
        self.listbox.bind('<<ListboxSelect>>', seleccionar_evento_callback)
        self.listbox.grid(row =0, column = 0, sticky = "snew")


    def agregar_eventos(self, evento) :
        nombre = evento.nombre
        self.listbox.insert(END, nombre)

    def agregar_marcador_mapa(self, latitud, longitud, texto, imagen = None) :
        return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen, command=self.seleccionar_ubicacion_callback)