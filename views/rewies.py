#Importacion de funciones.
from tkinter import *
from CTkMessagebox import CTkMessagebox
from models.reacciones import Reacciones
import customtkinter
import uuid

#Declaracion de clases.
class Rewies (customtkinter.CTkFrame) :

    def __init__ (self, master, evento_seleccionado, detalles_eventos) :

        """ Metodo constructor."""

        super().__init__(master)
        self.master = master
        self.evento_seleccionado = evento_seleccionado
        self.detalles_eventos = detalles_eventos

        #Creacion de un frame principal
        self.frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame.grid(row = 3, column = 0, sticky = "w")
        self.frame.grid_columnconfigure(0, weight = 1)

        #Cuadro de texto.
        self.frame2 = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame2.grid(row = 1, column = 0, sticky = "snew", padx = 10)     
        self.label = customtkinter.CTkLabel(self.frame2, text = f"Escribe una reseña sobre el evento: {self.evento_seleccionado.nombre}", font= customtkinter.CTkFont(family="Arial", size=12, weight="bold"))
        self.label.grid(row = 0, column = 0, sticky = "w")
        self.textbox = customtkinter.CTkTextbox(self.frame2, width=400, height = 70)
        self.textbox.grid(row = 1, column = 0, pady = 10, sticky = "w")

        #Botones de animo.
        self.frame_expe = customtkinter.CTkFrame(self.frame2, fg_color= "transparent")
        self.frame_expe.grid(row = 1, column = 0, sticky = "w", padx = 420)
        self.label_reaccion = customtkinter.CTkLabel(self.frame_expe, text = "Indique su animo:")
        self.label_reaccion.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.boton_feliz = customtkinter.CTkButton(self.frame_expe, text = "😃", command = self.feliz, width = 50)
        self.boton_feliz.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "w")
        self.boton_enojao = customtkinter.CTkButton(self.frame_expe, text = "😔", command = self.decepcion, width = 50)
        self.boton_enojao.grid(row = 1, column = 1, padx = (0, 20), pady = 5, sticky = "w")

        #Slider de calificacion.
        self.frame_aux = customtkinter.CTkFrame(self.frame2)
        self.frame_aux.grid(row = 2, column = 0, sticky = "w", pady = 10)
        self.label_calificacion = customtkinter.CTkLabel(self.frame_aux, text = "Califica el evento: ")
        self.label_calificacion.grid(row = 0, column = 0, sticky = "w")
        self.slider = customtkinter.CTkSlider(self.frame_aux, from_=1, to=5, number_of_steps = 4., command = self.slider_event)
        self.slider.grid(row = 0, column = 1, sticky = "w")

        #Crea un CTkLabel para mostrar el valor actual del slider
        self.slider_value_label = customtkinter.CTkLabel(self.frame_aux, text="Valor actual: 1")
        self.slider_value_label.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)

        #Boton de guardado.
        self.boton_ingreso = customtkinter.CTkButton(self.frame_aux, text = "Guardar", command = self.guardar, width = 50)
        self.boton_ingreso.grid(row = 1, column = 2, sticky = "w", padx = 30, pady = 10)

        #Comentarios anteriores.
        self.frame_comentarios =customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_comentarios.grid(row = 0, column = 0, sticky = "w", padx = 5, pady = 5)
        self.label_anterior = customtkinter.CTkLabel(self.frame_comentarios, text = "Reseñas anteriores:", font = customtkinter.CTkFont(family = "Arial", size = 12, weight = "bold"))
        self.label_anterior.grid(row = 1, column = 0, padx = 10, sticky = "w")
        self.texto_anterior = customtkinter.CTkTextbox(self.frame_comentarios, width = 570, height = 70)
        self.texto_anterior.grid(row = 2, column = 0, padx = 5, pady = 5)

        #Boton de retorno.
        self.frame_retu = customtkinter.CTkFrame(self.frame_aux, fg_color = "transparent")
        self.frame_retu.grid(row = 1, column = 3)
        self.boton_return = customtkinter.CTkButton(self.frame_retu, text = "Volver", command = self.volver, width = 60)
        self.boton_return.grid(row = 0, column = 0, padx = 20)

    def slider_event(self, value):
        self.slider_value_label.configure(text=f"Valor actual: {value}")

    def volver (self) :

       self.grid_forget
       self.detalles_eventos.volver_desde_rewies()
        
    def feliz (self) :

        self.reaccion_seleccionada = "😃"
    
    def decepcion (self) :
    
        self.reaccion_seleccionada = "😔"
    
    def guardar (self) :

        texto = self.textbox.get("1.0", "end-1c")
        calification = self.slider.get()
        if texto and calification :
            
            #Generar una ID aleatoria para el usuario
            id_resenia = str(uuid.uuid4())
            Reacciones.guardar_reacciones(id=id_resenia, id_evento="", id_usuario="", calificacion=calification, comentario=texto, animo=self.reaccion_seleccionada, archivo_json="data/rewies.json")


        
        else :
        
            CTkMessagebox(title="Campo Vacio", message="Por favor escriba un reseña")
