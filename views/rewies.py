#Importacion de funciones.
from tkinter import *
import customtkinter

#Declaracion de clases.
class Rewies (customtkinter.CTkFrame) :

    def __init__ (self, master, evento_seleccionado) :

        """ Metodo constructor."""

        super().__init__(master)
        self.master = master
        self.evento_seleccionado = evento_seleccionado
        
        #Creacion de un frame principal
        self.frame = customtkinter.CTkFrame(self)
        self.frame.grid(row = 0, column = 0, sticky = "snew")
        self.frame.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

        #Boton de retorno.
        self.boton_return = customtkinter.CTkButton(self.frame, text = "Volver", command = self.volver)
        self.boton_return.grid(row = 0, column = 2, padx = 10, pady = 10)

        #Cuadro de texto.
        self.frame2 = customtkinter.CTkFrame(self.frame)
        self.frame2.grid(row = 0, column = 0, sticky = "w", padx = 20, pady = 20)
        self.label = customtkinter.CTkLabel(self.frame2, text = f"Escribe una reseña sobre el evento: {self.evento_seleccionado.nombre}", font= customtkinter.CTkFont(family="Arial", size=12, weight="bold"))
        self.label.grid(row = 1, column = 0, sticky = "w", padx = 30)

        self.textbox = customtkinter.CTkTextbox(self.frame2, width=350, height = 70)
        self.textbox.grid(row = 3, column = 0, padx = 10, pady = 10)
        self.boton_ingreso = customtkinter.CTkButton(self.frame2, text = "Guardar", command = self.guardar, width = 50)
        self.boton_ingreso.grid(row = 4, column = 0, sticky = "w", padx = 5, pady = 5)

        #Botones de animo.
        self.boton_feliz = customtkinter.CTkButton(self.frame2, text = "😃", command = self.feliz, width = 50)
        self.boton_feliz.grid(row = 4, column = 1, padx = 5, pady = 5, sticky = "w")
        self.boton_enojao = customtkinter.CTkButton(self.frame2, text = "😔", command = self.decepcion, width = 50)
        self.boton_enojao.grid(row = 4, column = 2, padx = 5, pady = 5, sticky = "w")

    def volver (self) :

        self.grid_forget()
        
    def feliz (self) :

        print("hizo click 1")
    
    def decepcion (self) :
    
        print("hizo click 2")
    
    def guardar (self) :

        texto = self.textbox.get("1.0", "end-1c")
        print(texto)