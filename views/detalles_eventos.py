#Importacion de funciones.
from models.eventos import Eventos
from models.ubicaciones import Ubicacion
from controller.controlador_indice_eve import Controlador_Indices
from PIL import Image
from views.rewies import Rewies
import customtkinter

class Detalles_Eventos (customtkinter.CTkFrame) :

    """ """

    def __init__(self, master, evento_seleccionado, controlador = None) :

        """Metodo constructo."""
        
        super().__init__(master) 
        self.master = master
        self.evento_seleccionado = evento_seleccionado 
        self.controlador = controlador
        self.eventos = Eventos.cargar_eventos("data/indice_de_eventos.json")
        self.ubicaciones = Ubicacion.cargar_ubicaciones("data/ubicaciones.json")
        self.imagenes = []
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

        #Creacion de un frame principal.
        self.frame_pri = customtkinter.CTkFrame(self)
        self.frame_pri.grid(row = 0, column = 0, sticky = "snew")
        self.frame_pri.grid_rowconfigure(0, weight=1)
        self.frame_pri.grid_columnconfigure(0, weight=1)

        #Creacion de un frame para mostrar los detalles del evento.
        self.scroll = customtkinter.CTkScrollableFrame(self.frame_pri, orientation = "horizontal")
        self.scroll.grid(row=0, column=0, columnspan=2, sticky="nsew", padx = 5, pady = 5)

        #Creacion de un frame para los botones.
        self.button_frame = customtkinter.CTkFrame(self.frame_pri, bg_color = "transparent")
        self.button_frame.grid(row=0, column=2, sticky="ns", padx = 5, pady = 5)

        #Boton de retorno
        self.boton = customtkinter.CTkButton(self.button_frame, text="Volver", command=self.back, 
                                             font=customtkinter.CTkFont(family = "Century Gothic", size=11, weight="bold"))
        self.boton.grid(row = 2, column = 0, padx = 10, pady = 10)

        #Boton para compartir evento en redes sociales.
        self.boton_redes = customtkinter.CTkButton(self.button_frame, text="Compartir en tus redes sociales.",
                                                   font=customtkinter.CTkFont(family = "Century Gothic", size=11, weight="bold"))
        self.boton_redes.grid(row = 3, column = 0, padx = 10, pady = 10)

        #Boton para visualizar el mapa.
        self.boton_mapa = customtkinter.CTkButton(self.button_frame, text="Visualizar en un mapa.", command = self.mapas_planificaciones,
                                                  font=customtkinter.CTkFont(family = "Century Gothic", size=11, weight="bold"))
        self.boton_mapa.grid(row = 4, column = 0, padx = 10, pady = 10)

        #Creacion de un swtich.
        self.labe_asistencia = customtkinter.CTkLabel(self.button_frame, text= "¿Asistio al evento?", 
                                                      font=customtkinter.CTkFont(family = "Times New Roman", size=12, weight="bold"))
        self.labe_asistencia.grid(row = 5, column = 0, padx = 10, pady = 10)
        
        self.combo = customtkinter.CTkComboBox(self.button_frame, values = ["", "Si", "No"], command = self.afirmaciones,
                                               font=customtkinter.CTkFont(family = "Century Gothic", size=11, weight="bold"))
        self.combo.grid(row = 6, column = 0, padx = 10, pady = 10)

        self.muestra_detalles()

    def afirmaciones (self, value) :
        
        usuario_actual = self.controlador.get_usuario_actual()

        if value == "Si" :

            if usuario_actual :

                self.controlador.agregar_evento_asistencia(self.evento_seleccionado.id)

            self.boton_reseñas = customtkinter.CTkButton(self.button_frame, text = "Escribir una reseña" ,command = self.resenas_rewies,
                font=customtkinter.CTkFont(family = "Century Gothic", size=11, weight="bold"))
            
            self.boton_reseñas.grid(row=7, column=0, padx=10, pady=10)
        else :
            
            if usuario_actual :
                self.controlador.eliminar_evento_asistencia(self.evento_seleccionado.id)

            if hasattr(self, 'boton_reseñas'):
                self.boton_reseñas.grid_forget()

    def mapas_planificaciones (self) :

        mapa_plani = Controlador_Indices(self)

    def muestra_detalles (self) :

        """ """

        customtkinter.CTkLabel(self.scroll, text=f"Artista: {self.evento_seleccionado.artista}", font=customtkinter.CTkFont(family = "Times New Roman", size=12, weight="bold")).grid(sticky = "w")
        customtkinter.CTkLabel(self.scroll, text=f"Género: {self.evento_seleccionado.genero}", font=customtkinter.CTkFont(family = "Times New Roman", size=12, weight="bold")).grid(sticky = "w")
        customtkinter.CTkLabel(self.scroll, text=f"Ubicación: {self.evento_seleccionado.ubicacion}", font=customtkinter.CTkFont(family = "Times New Roman", size=12, weight="bold")).grid(sticky = "w")
        customtkinter.CTkLabel(self.scroll, text=f"Fecha: {self.evento_seleccionado.hora_inicio[:10]}", font=customtkinter.CTkFont(family = "Times New Roman", size=12, weight="bold")).grid(sticky = "w")
        customtkinter.CTkLabel(self.scroll, text=f"Hora de inicio: {self.evento_seleccionado.hora_inicio[11:]}", font=customtkinter.CTkFont(family = "Times New Roman", size=12, weight="bold")).grid(sticky = "w")
        customtkinter.CTkLabel(self.scroll, text=f"Hora de fin: {self.evento_seleccionado.hora_fin[11:]}", font=customtkinter.CTkFont(family = "Times New Roman", size=12, weight="bold")).grid(sticky = "w")
        customtkinter.CTkLabel(self.scroll, text=f"Descripción: {self.evento_seleccionado.descripcion}", font=customtkinter.CTkFont(family = "Times New Roman", size=12, weight="bold")).grid(sticky = "w")

    def cargar_imagenes (self) :

        """ """

        #Procesamiento de datos.
        for evento in self.eventos :
            imagen_evento = customtkinter.CTkImage(light_image = Image.open(f"assets/{evento.imagen}"), size=(200, 200))
            self.imagenes.append(imagen_evento)

    def back (self) :

        """Metodo para volver al frame anterior."""

        self.grid_forget()

    def resenas_rewies (self) :
        
        self.frame_pri.grid_forget()
        self.resenas = Rewies(self, self.evento_seleccionado, self, self.controlador)
        self.resenas.grid(row = 0, column = 0, sticky = "snew")

    def volver_desde_rewies(self) :

        self.resenas.grid_forget() 
        self.frame_pri.grid(row = 0, column = 0, sticky = "snew")  