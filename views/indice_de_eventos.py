#Importacion de funciones.
from tkinter import *
from PIL import ImageTk
from models.eventos import Eventos 
from models.ubicaciones import Ubicacion
import customtkinter

class Indice_de_Eventos (customtkinter.CTkToplevel) :

    """ """

    #Declaracion de Metodos.
    def __init__(self, ventana) :

        """ Metodo constructor de la clase Indice_de_Eventos"""

        super().__init__(ventana)
        self.title("Indice de Eventos")
        self.geometry("480x360")
        self.iconbitmap("assets/ondas-sonoras.ico")

        # Cargamos la ruta del archivo json
        ruta_indices = "data/indice_de_eventos.json"
        eventos_indices = Eventos.cargar_eventos(ruta_indices)

        # Creacion de una Listbox para mostrar los eventos cargados.
        eventos_listbox = Listbox(self, width=50)
        eventos_listbox.pack()

        for evento in eventos_indices:
            eventos_listbox.insert(END, evento.nombre)

        # Asociar un evento para mostrar detalles cuando se selecciona un evento de la lista
        eventos_listbox.bind('<<ListboxSelect>>', lambda event: self.mostrar_detalles_evento(event, eventos_indices))

    def mostrar_detalles_evento(self, event, eventos_indices):
        # Obtener el índice del evento seleccionado
        index = event.widget.curselection()
        if index:
            index = int(index[0])
            evento_seleccionado = eventos_indices[index]

            # Mostrar una ventana emergente con los detalles del evento
            detalles_ventana = Toplevel()
            detalles_ventana.title(evento_seleccionado.nombre)

            # Cargar y mostrar la imagen del evento
            imagen_evento = Image.open("assets/" + evento_seleccionado.imagen)
            etiqueta_imagen = Label(detalles_ventana, image=imagen_evento)
            etiqueta_imagen.pack()

            # Crear etiquetas para mostrar los detalles del evento
            Label(detalles_ventana, text=f"Artista: {evento_seleccionado.artista}").pack()
            Label(detalles_ventana, text=f"Género: {evento_seleccionado.genero}").pack()
            Label(detalles_ventana, text=f"Ubicación: {evento_seleccionado.ubicacion}").pack()
            Label(detalles_ventana, text=f"Hora de inicio: {evento_seleccionado.hora_inicio}").pack()
            Label(detalles_ventana, text=f"Hora de fin: {evento_seleccionado.hora_fin}").pack()
            Label(detalles_ventana, text=f"Descripción: {evento_seleccionado.descripcion}").pack()

            # Mostrar la ventana de detalles del evento
            detalles_ventana.mainloop()


    
        



