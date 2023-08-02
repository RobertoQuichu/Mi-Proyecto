#Importacion de funciones.
from tkinter import *
from views.detalles_eventos import Detalles_Eventos
import customtkinter
from models.eventos import Eventos
from PIL import Image

class Indice_de_Eventos (customtkinter.CTkToplevel) :

    """ Esta clase muestra todos los eventos almacenados en los archivos de la aplicacion."""

    #Declaracion de Metodos.
    def __init__(self, ventana, controlador = None) :

        """ Metodo constructor de la clase Indice_de_Eventos"""

        super().__init__(ventana)
        self.controlador = controlador
        self.title("Indice de eventos")
        self.geometry("600x350")
        self.resizable(False, False)
        self.iconbitmap("assets\musica.ico")
        
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
        self.lista_eventos = Listbox(self.frame, width= 100, height = 100, fg = "#2F242C", font = customtkinter.CTkFont(family="Arial", size=15, weight="bold"))
        self.lista_eventos.grid(row= 0, column = 0, padx = 10, pady = 10, sticky="w")
        self.lista_eventos.config(bg = "#E5E5E5", borderwidth = 5)

        #Imagen de adorno.
        self.imagen_indices = customtkinter.CTkImage(light_image = Image.open("assets/evento1.jpg"), size = (300, 300))
        self.imagen_label = customtkinter.CTkLabel(master = self.frame, image= self.imagen_indices, text = "")
        self.imagen_label.grid(row = 0, column = 1, padx = 10, pady = 10)


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
            self.detallitos = Detalles_Eventos(self, evento_seleccionado, self.controlador)
            self.detallitos.grid(row=0, column=0, sticky="nsew")
            self.detallitos.grid_columnconfigure(0, weight = 1)
            self.detallitos.grid_rowconfigure(0, weight = 1)

    
