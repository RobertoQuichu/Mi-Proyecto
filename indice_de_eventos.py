#Importacion de funciones.
from tkinter import * 
import customtkinter
import json
import os

class Indice_de_eventos (customtkinter.CTkToplevel) :

    """ """

    #Declaracion de Metodos.

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
        print(eventos)
        return eventos
    def __init__(self, ventana = None) :

        """ Metodo Constructor de la clase."""

        #Procesamiento de datos.
        super().__init__(ventana)
        self.ventana = ventana
        self.title("Indice de Eventos")
        self.eventos = self.cargar_datos()

        #Crear una lista para mostrar los eventos
        self.lista_eventos = Listbox(self.ventana, width=50)
        self.lista_eventos.pack(padx=20, pady=10)
        for evento in self.eventos :
            self.lista_eventos.insert(END, evento["Nombre"])
        
        #Creacion del Boton.
        buton = customtkinter.CTkButton(self, text = "Indice de eventos", command = self.ver_detalles_evento)
        buton.place(relx=0.1, rely=0.3, anchor="w")

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
            customtkinter.CTkLabel(detalles_ventana, text=f"Nombre: {evento_seleccionado['Nombre']}").pack()
            customtkinter.CTkLabel(detalles_ventana, text=f"Artista: {evento_seleccionado['Artista']}").pack()
            customtkinter.CTkLabel(detalles_ventana, text=f"Género: {evento_seleccionado['Genero']}").pack()
            customtkinter.CTkLabel(detalles_ventana, text=f"Ubicación: {evento_seleccionado['Ubicacion']}").pack()

