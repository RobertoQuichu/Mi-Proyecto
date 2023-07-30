#Importacion de funciones.
from controller.controlador_frame import Controlador_Frames
from tkinter import *
from models.ubicaciones import Ubicacion
from views.detalles_eventos import Detalles_Eventos
import customtkinter
from models.eventos import Eventos

class Indice_de_Eventos (customtkinter.CTkToplevel) :

    """ Esta clase muestra todos los eventos almacenados en los archivos de la aplicacion."""

    #Declaracion de Metodos.
    def __init__(self, ventana) :

        """ Metodo constructor de la clase Indice_de_Eventos"""

        super().__init__(ventana)
        self.title("Indice de eventos")
        self.geometry("600x350")
        self.resizable(False, False)
        
        #Creacion de un frame.
        self.frame = customtkinter.CTkFrame(self)
        self.frame.grid(row=0, column=0, sticky="nsew") 

        #Configurar las filas y columnas de la ventana principal para que el frame ocupe todo el espacio disponible.
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #Configurar las filas y columnas del frame para que el contenido se expanda en todas las direcciones.
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        
        #Creacion de una Listbox.
        self.lista_eventos = Listbox(self.frame, width= 10, height = 10)
        self.lista_eventos.grid(padx = 50, pady = 50, sticky="nsew")

        #Boton para explorar eventos.
        self.boton = customtkinter.CTkButton(self.frame, text = "Explorar Evento")
        self.boton.grid(pady = 5)

        #Obtener los eventos almacenados.
        eventos = Eventos.cargar_eventos("data/indice_de_eventos.json")
        self.eventos = eventos
        
        #Obtener la lista de eventos desde el controlador.
        for evento in self.eventos :
            self.lista_eventos.insert(END, evento.nombre)
        self.lista_eventos.bind("<Double-Button-1>", self.mostrar_detalles_evento)
    
    def mostrar_detalles_evento(self, event) :

        # Obtener el índice del evento seleccionado en el ListBox
        index = self.lista_eventos.curselection()
        if index:

            index = int(index[0])
            evento_seleccionado = self.eventos[index]
            self.detallitos = Detalles_Eventos(self, evento_seleccionado)
            self.detallitos.grid(row=0, column=0, sticky="nsew")
            self.detallitos.grid_columnconfigure(0, weight = 1)
            self.detallitos.grid_rowconfigure(0, weight = 1)

    
