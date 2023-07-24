#Importacion de funciones.
from tkinter import *
from models.ubicaciones import Ubicacion
import customtkinter
from models.eventos import Eventos

class Indice_de_Eventos (customtkinter.CTkToplevel) :

    """ """

    #Declaracion de Metodos.
    def __init__(self, ventana) :

        """ Metodo constructor de la clase Indice_de_Eventos"""

        super().__init__(ventana)
        self.title("Indice de eventos")
        self.geometry("360x240")
        
        #Creacion de un frame.
        frame = customtkinter.CTkFrame(self)
        frame.grid(row=0, column=0, sticky="nsew", padx = 10, pady = 10) 

        #Configurar las filas y columnas de la ventana principal para que el frame ocupe todo el espacio disponible.
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #Configurar las filas y columnas del frame para que el contenido se expanda en todas las direcciones.
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        
        #Creacion de una Listbox.
        lista_eventos = Listbox(frame, width= 30, height = 10)
        lista_eventos.grid(padx = 10, pady = 10, sticky="nsew")

        #Boton para explorar eventos.
        boton = customtkinter.CTkButton(frame, text = "Explorar Evento")
        boton.grid(pady = 5)

        #Obtener los eventos almacenados.
        eventos = Eventos.cargar_eventos("data/indice_de_eventos.json")
        ubicaciones = Ubicacion.cargar_ubicaciones("data/ubicaciones.json")
        self.eventos = eventos
        self.ubicaciones = ubicaciones
        self.imagenes = []
        
        #Obtener la lista de eventos desde el controlador.
        for evento in self.eventos :
            lista_eventos.insert(END, evento.nombre)
        lista_eventos.bind("<<ListBoxSelect>>", self.mostrar_detalles_evento)
    
    def cargar_imagenes (self) :

        #Procesamiento de datos.
        for evento in self.eventos :
            imagen_evento = customtkinter.CTkImage(light_image = Image.open(f"assets/{evento.imagen}"), size=(200, 200))
            self.imagenes.append(imagen_evento)
    
    def mostrar_detalles_evento(self, event):
        # Obtener el índice del evento seleccionado en el ListBox
        index = Listbox.curselection()

    
