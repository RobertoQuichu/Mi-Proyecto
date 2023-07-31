#Importacion de funciones.
from tkinter import *
from PIL import Image, ImageTk
from models.eventos import Eventos 
from models.ubicaciones import Ubicacion
from views.mapa_planificacion import Mapas_Planificacion

class Controlador_Indices :
    
    def __init__(self, ventana) :
        self.imagenes = []
        self.marcadores = []
        self.vista = Mapas_Planificacion(ventana, self.seleccionar_eventos, seleccionar_ubicacion)

        #Cargamos la ruta del archivo json
        self.eventos = Eventos.cargar_eventos("data/indice_de_eventos.json")
        self.ubicaciones = Ubicacion.cargar_ubicaciones("data/ubicaciones.json")
        self.cargar_eventos()
        self.cargar_imagenes()
        self.cargar_marcadores()

    def cargar_eventos(self) :
        for evento in self.eventos:
            self.vista.agregar_eventos(evento)
    
    def cargar_imagenes (self) :

        #Procesamiento de datos.
        for evento in self.eventos :
            imagen_evento = ImageTk.PhotoImage(Image.open(f"assets/{evento.imagen}").resize((150, 150)))
            self.imagenes.append(imagen_evento)
            print(evento.imagen)

    def cargar_marcadores (self) :

        #Procesamiento de datos.
        for ubicacion, local in zip(self.ubicaciones, self.eventos):
            imagen = self.imagenes[ubicacion.id - 1]
            marcador = self.vista.agregar_marcador_mapa(ubicacion.latitud, ubicacion.longitud, local.nombre, imagen)
            marcador.hide_image(True)
            self.marcadores.append(marcador)
    
    def seleccionar_eventos(self, event):
        
        #Obtiene el índice del elemento seleccionado
        indice_seleccionado = self.vista.listbox.curselection()
        
        #Obtiene el local seleccionado
        evento_seleccionado = self.eventos[indice_seleccionado[0]]
        
        ubicacion_seleccionada = Ubicacion(0, 0, 0, "")
        
        #Busca la ubicación correspondiente al local seleccionado
        for ubicacion in self.ubicaciones:
            if ubicacion.id == evento_seleccionado.id_ubicacion:
                ubicacion_seleccionada = ubicacion
                break
        
        #Centra el mapa en la ubicación seleccionada
        self.vista.mapa.set_position(ubicacion_seleccionada.latitud, ubicacion_seleccionada.longitud)

        print(f"Latitud: {ubicacion_seleccionada.latitud}, Longitud: {ubicacion_seleccionada.longitud}")

def seleccionar_ubicacion(marcador) :
    
    if marcador.image_hidden is True:
        marcador.hide_image(False)
    else:
        marcador.hide_image(True)
    nombre_evento = marcador.text
    print("Ubicación seleccionada: ", marcador.text)