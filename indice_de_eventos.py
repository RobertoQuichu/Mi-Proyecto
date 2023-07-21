#Importacion de funciones.
from tkinter import * 
import customtkinter
import json
import os

class Indice_de_eventos :

    """ """

    #Declaracion de Metodos.
    def __init__(self, ventana) :

        """ Metodo Constructor de la clase."""

        #Procesamiento de datos.
        self.ventana = ventana
        self.ventana.title("Indice de Eventos")
        self.eventos = self.cargar_datos()

        #Crear una lista para mostrar los eventos
        self.lista_eventos = Listbox(self.ventana, width=50)
        self.lista_eventos.pack(padx=20, pady=10)
        for evento in self.eventos :
            self.lista_eventos.insert(END, evento["Nombre"])

         #Agregar un botón para ver los detalles del evento seleccionado
        self.boton_ver_detalles = customtkinter.CTkButton(self.ventana, text="Ver Detalles", command=self.ver_detalles_evento)
        self.boton_ver_detalles.pack(pady=5)

    def ver_detalles_evento(self):
        # Obtener el índice del evento seleccionado
        index = self.lista_eventos.curselection()
        if index:
            index = int(index[0])
            evento_seleccionado = self.eventos[index]

            #Mostrar una ventana emergente con los detalles del evento
            detalles_ventana = customtkinter.CTkToplevel()
            detalles_ventana.title("Detalles del Evento")

            #Crear etiquetas para mostrar los detalles del evento
            customtkinter.CTkLabel(detalles_ventana, text=f"Nombre: {evento_seleccionado['nombre']}").pack()
            customtkinter.CTkLabel(detalles_ventana, text=f"Artista: {evento_seleccionado['artista']}").pack()
            customtkinter.CTkLabel(detalles_ventana, text=f"Género: {evento_seleccionado['genero']}").pack()
            customtkinter.CTkLabel(detalles_ventana, text=f"Ubicación: {evento_seleccionado['ubicacion']}").pack()

    @classmethod
    def cargar_datos (cls) :

        """ Esta metodo lee los datos almacenados en el archivos json de indice_de_eventos.json"""

        #Ruta del archivo json.
        nombre_usuario = os.path.join("data", "indice_de_eventos.json")

        #Cargar el archivos json.
        try :
            with open(nombre_usuario, "r" ) as indices :
                eventos = json.load(indices)
        except FileExistsError :
            eventos = []
        return eventos
