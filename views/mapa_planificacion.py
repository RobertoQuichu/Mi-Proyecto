#Importacion de funciones.
from controller.centrar_ventanas import Centrar_Ventana
from tkintermapview import TkinterMapView
from tkinter import *
import customtkinter

#Declaracion de clases.
class Mapas_Planificacion (customtkinter.CTkToplevel) :

    """ 
    Esta clase mostrara una ventana emergente que permitira visualizar la ubicacion del evento 
    y poder planificar una ruta hasta el evento

    """
    def __init__(self, ventana, seleccionar_evento_callback = None, seleccionar_ubicacion_callback = None):
        super().__init__(ventana)
        self.seleccionar_local_callback = seleccionar_evento_callback
        self.seleccionar_ubicacion_callback = seleccionar_ubicacion_callback
        self.title("Mapa y Planificion de Rutas")
        Centrar_Ventana.centrar(self)
        self.geometry("720x480")
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        #Creacion de un frame para el mapa
        self.frame_mapa = customtkinter.CTkFrame(self)
        self.frame_mapa.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")
        self.frame_mapa.grid_rowconfigure(1, weight=1)
        self.frame_mapa.grid_rowconfigure(0, weight=0)
        self.frame_mapa.grid_columnconfigure(0, weight=1)
        self.frame_mapa.grid_columnconfigure(1, weight=0)
        self.frame_mapa.grid_columnconfigure(2, weight=1)
        self.mapa = TkinterMapView(self.frame_mapa, width = 600, height = 600, corner_radius = 0)
        self.mapa.set_position(-24.77616437851034, -65.41079411004006)
        self.mapa.set_zoom(16)
        self.mapa.grid(row=1, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=(0, 0), pady=(0, 0))

        #Frame para una listbox.
        self.frame_listbxo = customtkinter.CTkFrame(self)
        self.frame_listbxo.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        self.frame_listbxo.grid_columnconfigure(2, weight = 1)
        self.listbox = Listbox(self.frame_listbxo, width = 30, fg = "#2F242C", font = customtkinter.CTkFont(family="Arial", size=15, weight="bold"))
        self.listbox.bind('<<ListboxSelect>>', seleccionar_evento_callback)
        self.listbox.grid(row =0, column = 0, sticky = "snew", padx = 5, pady = 5)
        self.listbox.config(bg = "#E5E5E5", borderwidth = 5)

        #Boton para trazar una ruta hacia el evento.
        self.label_ruta = customtkinter.CTkLabel(self.frame_listbxo, text = "Trazar una ruta", anchor = "w", font = customtkinter.CTkFont(family = "Times New Roman", size = 12, weight = "bold"))
        self.label_ruta.grid(row = 3, column = 0, padx=(20, 20), pady = (20, 0))
        self.boton_ruta = customtkinter.CTkButton(self.frame_listbxo, text = "Trazar ruta", anchor = "w",
                                                  font=customtkinter.CTkFont(family = "Century Gothic", size = 11, weight = "bold"))
        self.boton_ruta.grid(row = 4, column = 0, padx=(20, 20), pady = (10, 20))

        #Controlar la apariencia de la ventana.
        self.apariencia_modo_label = customtkinter.CTkLabel(self.frame_listbxo, text="Cambiar de apariencia:", anchor="w", 
                                                            font = customtkinter.CTkFont(family = "Times New Roman", size = 12, weight = "bold"))
        self.apariencia_modo_label.grid(row=5, column=0, padx=(20, 20), pady=(20, 0))
        self.apariencia_modo_menu = customtkinter.CTkOptionMenu(self.frame_listbxo, values=["Light", "Dark", "System"],
                                                                       command=self.cambio_de_apariencia, font=customtkinter.CTkFont(family = "Century Gothic", size = 11, weight = "bold"))
        self.apariencia_modo_menu.grid(row=6, column=0, padx=(20, 20), pady=(10, 20))
        self.apariencia_modo_menu.set("Dark")

    def cambio_de_apariencia (self, nueva_apariencia: str) :
        customtkinter.set_appearance_mode(nueva_apariencia)

    def agregar_eventos(self, evento) :
        nombre = evento.nombre
        self.listbox.insert(END, nombre)

    def agregar_marcador_mapa(self, latitud, longitud, texto, imagen = None) :
        return self.mapa.set_marker(latitud, longitud, text = texto, image = imagen, command = self.seleccionar_ubicacion_callback)