#Importacion de funciones.
from tkinter import *
from tkintermapview import TkinterMapView
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
        lista_eventos = Listbox(self, width= 30, height = 10)
        lista_eventos.place(relx = 0.5, rely = 0.5, relheight = 0.7, relwidth = 0.7,anchor = CENTER)

        #Obtener los eventos almacenados.
        eventos = Eventos.cargar_eventos("data/indice_de_eventos.json")
        ubicaciones = Ubicacion.cargar_ubicaciones("data/ubicaciones.json")
        self.eventos = eventos
        self.ubicaciones = ubicaciones
        

        #Obtener la lista de eventos desde el controlador.
        for evento in self.eventos :
            lista_eventos.insert(END, evento.nombre)
        lista_eventos.bind("<<ListBoxSelect>>", self.mostrar_detalles_evento)
    
    def cargar_imagenes (self) :

        #Procesamiento de datos.
        for evento in self.eventos :
            imagen_evento = customtkinter.CTkImage(light_image = Image.open(f"assets/{evento.imagen}"), size=(200, 200))
            self.imagenes.append(imagen_evento)
    
    def mostrar_detalles_evento(self, event, Listbox):
        # Obtener el índice del evento seleccionado en el ListBox
        index = Listbox.curselection()
        if index:
            index = int(index[0])
            evento_seleccionado = self.eventos[index]

            # Crear una etiqueta para mostrar la imagen del evento seleccionado
            imagen_label = customtkinter.CTkLabel(self, image=self.imagenes[index])
            imagen_label.place(relx=0.5, rely=0.25, anchor=CENTER)

            # Crear una etiqueta para mostrar los detalles del evento seleccionado
            detalles_label = customtkinter.CTkLabel(self, text=f"Nombre: {evento_seleccionado.nombre}\nFecha: {evento_seleccionado.fecha}\nLugar: {evento_seleccionado.lugar}")
            detalles_label.place(relx=0.5, rely=0.75, anchor=CENTER)
    
