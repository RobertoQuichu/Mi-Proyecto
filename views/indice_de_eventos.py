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
    
    def mostrar_detalles_evento(self, event):
    
        #Obtener el índice del evento seleccionado
        index = event.widget.curselection()
        if index:
            index = int(index[0])
            evento_seleccionado = self.eventos[index]

            #Mostrar una ventana emergente con los detalles del evento
            detalles_ventana = customtkinter.CTkToplevel(self)
            detalles_ventana.title(evento_seleccionado.nombre)

            #Cargar y mostrar la imagen del evento
            imagen_evento = customtkinter.CTkImage(light_image = Image.open("assets/" + evento_seleccionado.imagen), size = (200, 200))
            etiqueta_imagen = customtkinter.CTkLabel(detalles_ventana, image=imagen_evento)
            etiqueta_imagen.pack()

            #Crear etiquetas para mostrar los detalles del evento
            customtkinter.CTkLabel(detalles_ventana, text=f"Artista: {evento_seleccionado.artista}").pack()
            customtkinter.CTkLabel(detalles_ventana, text=f"Género: {evento_seleccionado.genero}").pack()
            customtkinter.CTkLabel(detalles_ventana, text=f"Ubicación: {evento_seleccionado.ubicacion}").pack()
            customtkinter.CTkLabel(detalles_ventana, text=f"Hora de inicio: {evento_seleccionado.hora_inicio}").pack()
            customtkinter.CTkLabel(detalles_ventana, text=f"Hora de fin: {evento_seleccionado.hora_fin}").pack()
            customtkinter.CTkLabel(detalles_ventana, text=f"Descripción: {evento_seleccionado.descripcion}").pack()
            detalles_ventana.grab_set()
