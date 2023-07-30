#Importacion de funciones.
from tkinter import *
from CTkMessagebox import CTkMessagebox
from models.reacciones import Reacciones
import customtkinter

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
        self.frame.grid(row = 0, column = 0, sticky = "e")
        self.frame.grid_columnconfigure(0, weight = 1)

        #Boton de retorno.
        self.boton_return = customtkinter.CTkButton(self.frame, text = "Volver", command = self.volver)
        self.boton_return.grid(row = 0, column = 3, padx = 10, pady = 10, sticky = "e")

        #Swigets para indicar si asistio al evento.
        self.labe_asistencia = customtkinter.CTkLabel (self.frame, text = "¿Asistio al evento?", font = customtkinter.CTkFont(family = "Arial", size = 12, weight = "bold"))
        self.labe_asistencia.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "w")
        self.boton_si = customtkinter.CTkButton(self.frame, text = "Si", command = self.afirmacion, width = 50)
        self.boton_si.grid(row = 0, column = 1, sticky = "e", padx = 10, pady = 10)
        self.boton_no = customtkinter.CTkButton(self.frame, text = "No", width = 50, command = self.negacion)
        self.boton_no.grid(row = 0, column = 2, sticky = "w", padx = 10, pady = 10)

        #Comentarios anteriores.
        self.frame_comentarios =customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_comentarios.grid(row = 1, column = 0, sticky = "w", padx = 5, pady = 5)
        self.label_anterior = customtkinter.CTkLabel(self.frame_comentarios, text = "Reseñas anteriores:", font = customtkinter.CTkFont(family = "Arial", size = 12, weight = "bold"))
        self.label_anterior.grid(row = 1, column = 0, padx = 10, sticky = "w")
        self.texto_anterior = customtkinter.CTkTextbox(self.frame_comentarios, width = 400, height = 70)
        self.texto_anterior.grid(row = 2, column = 0, padx = 5, pady = 5)

    def negacion (self) :

        self.frame2.grid_forget()

    def afirmacion (self) :
        
        #Cuadro de texto.
        self.frame2 = customtkinter.CTkFrame(self)
        self.frame2.grid(row = 4, column = 0, sticky = "snew")     

        self.label = customtkinter.CTkLabel(self.frame2, text = f"Escribe una reseña sobre el evento: {self.evento_seleccionado.nombre}", font= customtkinter.CTkFont(family="Arial", size=12, weight="bold"))
        self.label.grid(row = 0, column = 0, sticky = "snew", padx = 30)
        self.textbox = customtkinter.CTkTextbox(self.frame2, width=400, height = 70)
        self.textbox.grid(row = 1, column = 0, padx = 10, pady = 10)

        #Botones de animo.
        self.boton_ingreso = customtkinter.CTkButton(self.frame2, text = "Guardar", command = self.guardar, width = 50)
        self.boton_ingreso.grid(row = 2, column = 0, sticky = "w", padx = 5, pady = 5)
        self.label_animo = customtkinter.CTkLabel(self.frame2, text = "Indique su experiencia en el evento.")
        self.boton_feliz = customtkinter.CTkButton(self.frame2, text = "😃", command = self.feliz, width = 50)
        self.boton_feliz.grid(row = 1, column = 2, padx = 5, pady = 5, sticky = "w")
        self.boton_enojao = customtkinter.CTkButton(self.frame2, text = "😔", command = self.decepcion, width = 50)
        self.boton_enojao.grid(row = 1, column = 3, padx = 5, pady = 5, sticky = "w")

    def volver (self) :

        self.grid_forget()
        self.detalles_eventos.mostrar_detalles_evento()
        
    def feliz (self) :

        self.reaccion_seleccionada = "😃"
    
    def decepcion (self) :
    
        self.reaccion_seleccionada = "😔"
    
    def guardar (self) :

        texto = self.textbox.get("1.0", "end-1c")
        if texto :
            
            Reacciones.guardar_reacciones(texto, self.reaccion_seleccionada, "data/rewies.json")
        
        else :
        
            CTkMessagebox(title="Campo Vacio", message="Por favor ingrese sus datos")
