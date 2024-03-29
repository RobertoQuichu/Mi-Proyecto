#Importacion de funciones.
from tkinter import *
from CTkMessagebox import CTkMessagebox
from models.reacciones import Reacciones
from models.usuarios import Usuario
from views.ventana_si_no_rewies import Ventana_Si_No
import customtkinter

#Declaracion de clases.
class Rewies (customtkinter.CTkFrame) :

    def __init__ (self, master, evento_seleccionado, detalles_eventos, controlador = None) :

        """ Metodo constructor."""

        super().__init__(master)
        self.master = master
        
        self.evento_seleccionado = evento_seleccionado
        self.detalles_eventos = detalles_eventos
        
        self.controlador = controlador
        self.comentarios = Reacciones.cargar_reacciones("data/rewies.json")

        #Cuadro de texto.
        self.frame2 = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame2.grid(row = 0, column = 0, sticky = "snew", padx = 10)     
        
        self.label = customtkinter.CTkLabel(self.frame2, text = f"Escribe una reseña sobre el evento: {self.evento_seleccionado.nombre}", font= customtkinter.CTkFont(family="Arial", size=12, weight="bold"))
        self.label.grid(row = 0, column = 0, sticky = "w")
        
        self.textbox = customtkinter.CTkTextbox(self.frame2, width=400, height = 70)
        self.textbox.grid(row = 1, column = 0, pady = 10, sticky = "w")

        #Botones de animo.
        self.frame_expe = customtkinter.CTkFrame(self.frame2, fg_color= "transparent")
        self.frame_expe.grid(row = 1, column = 0, sticky = "w", padx = 420)
        
        self.label_reaccion = customtkinter.CTkLabel(self.frame_expe, text = "Indique su animo:", font = customtkinter.CTkFont(family = "Arial", size = 12, weight = "bold"))
        self.label_reaccion.grid(row = 0, column = 0, padx = 5, pady = 5)
        
        self.boton_feliz = customtkinter.CTkButton(self.frame_expe, text = "😃", command = self.feliz, width = 50, hover = True,
                                                   font=customtkinter.CTkFont(family = "Century Gothic", size = 11, weight = "bold"))
        self.boton_feliz.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "w")
        
        self.boton_enojao = customtkinter.CTkButton(self.frame_expe, text = "😔", command = self.decepcion, width = 50, hover = True,
                                                    font=customtkinter.CTkFont(family = "Century Gothic", size = 11, weight = "bold"))
        self.boton_enojao.grid(row = 1, column = 1, padx = (0, 20), pady = 5, sticky = "w")

        #Slider de calificacion.
        self.frame_aux = customtkinter.CTkFrame(self.frame2)
        self.frame_aux.grid(row = 2, column = 0, sticky = "w", pady = 10)
        
        self.label_calificacion = customtkinter.CTkLabel(self.frame_aux, text = "Califica el evento: ", font = customtkinter.CTkFont(family = "Arial", size = 12, weight = "bold"))
        self.label_calificacion.grid(row = 0, column = 0, sticky = "w")
        
        self.slider = customtkinter.CTkSlider(self.frame_aux, from_=1, to=5, number_of_steps = 4., command = self.slider_event)
        self.slider.grid(row = 0, column = 1, sticky = "w")

        #Crea un CTkLabel para mostrar el valor actual del slider
        self.slider_value_label = customtkinter.CTkLabel(self.frame_aux, text="Valor actual: 1", font = customtkinter.CTkFont(family = "Arial", size = 12, weight = "bold"))
        self.slider_value_label.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)

        #Boton de guardado.
        self.boton_ingreso = customtkinter.CTkButton(self.frame_aux, text = "Guardar", command = self.guardar, width = 50,
                                                     font=customtkinter.CTkFont(family = "Century Gothic", size = 11, weight = "bold"))
        self.boton_ingreso.grid(row = 1, column = 2, sticky = "w", padx = 30, pady = 10)

        #Comentarios anteriores.
        self.frame_comentarios =customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_comentarios.grid(row = 1, column = 0, sticky = "w", padx = 5, pady = 5)
        
        self.label_anterior = customtkinter.CTkLabel(self.frame_comentarios, text = "Reseñas anteriores:", font = customtkinter.CTkFont(family = "Arial", size = 12, weight = "bold"))
        self.label_anterior.grid(row = 0, column = 0, padx = 10, sticky = "w")
        
        self.texto_anterior = customtkinter.CTkScrollableFrame(self.frame_comentarios, width = 555, height = 70)
        self.texto_anterior.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "n")

        #Boton de retorno.
        self.frame_retu = customtkinter.CTkFrame(self.frame_aux, fg_color = "transparent")
        self.frame_retu.grid(row = 1, column = 3)
        
        self.boton_return = customtkinter.CTkButton(self.frame_retu, text = "Volver", command = self.volver, width = 60,
                                                    font=customtkinter.CTkFont(family = "Century Gothic", size = 11, weight = "bold"))
        self.boton_return.grid(row = 0, column = 0, padx = 20)

        self.resenia_anteriores()

    def resenia_anteriores (self) :

        """ """

        usuarios = Usuario.cargar_usuarios("data/nombre_usuario.json")
        resenias = Reacciones.cargar_reacciones("data/rewies.json")
        for usuario in usuarios :
            for resenia in resenias :
                if resenia.id_usuario == usuario.id :
                    customtkinter.CTkLabel(self.texto_anterior, text=f"\tReseña de {usuario.nombre} {usuario.apellido} ", font = customtkinter.CTkFont(family = "Times New Roman", size = 12, weight = "bold")).grid(sticky = "w")
                    customtkinter.CTkLabel(self.texto_anterior, text=f"Comentario: {resenia.comentario}", font = customtkinter.CTkFont(family = "Times New Roman", size = 12, weight = "bold")).grid(sticky = "w")
                    customtkinter.CTkLabel(self.texto_anterior, text=f"Calificacion: {resenia.calificacion}", font = customtkinter.CTkFont(family = "Times New Roman", size = 12, weight = "bold")).grid(sticky = "w")
                    customtkinter.CTkLabel(self.texto_anterior, text=f"Reaccion: {resenia.animo}", font = customtkinter.CTkFont(family = "Times New Roman", size = 12, weight = "bold")).grid(sticky = "w")
                    customtkinter.CTkLabel(self.texto_anterior, text="").grid()

    def slider_event(self, value) :
        
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
        id_usuario_actual = self.controlador.get_usuario_actual().id
        id_evento_actual = self.evento_seleccionado.id
        asistencias = self.controlador.get_usuario_actual().asistencias
        print(asistencias)
        print(id_evento_actual)

        #Verificar si el usuario ya ha asistido al evento
        if id_evento_actual in self.controlador.get_usuario_actual().asistencias:
            print("El usuario asistio al evento")
            ventana_aux = Ventana_Si_No(self)
            ventana_aux.lift()                  
            self.wait_window(ventana_aux)       
            if not self.reaccion_seleccionada :
                CTkMessagebox(title = "Campo Vacío", message = "Por favor, indique su estado de animo en el evento: 😃/😔.")
            elif ventana_aux.afirmacion() == 0 :
                if texto and calification:
                    self.guardar_reseña(texto, calification, id_usuario_actual, id_evento_actual)
                    self.limpiar()
                else:
                    CTkMessagebox(title = "Campo Vacío", message = "Por favor, escriba una reseña.")
            else :
                self.volver()
        else :

            if texto and calification :
                self.guardar_reseña(texto, calification, id_usuario_actual, id_evento_actual)
                self.limpiar()
            else :
                CTkMessagebox(title = "Campo Vacío", message = "Por favor, escriba una reseña.")

    def guardar_reseña(self, texto, calificacion, id_usuario_actual, id_evento_actual) :
    
        #Generar una ID aleatoria para la reseña
        id_resenia = Reacciones.generar_id()

        #Guardar la reseña en el archivo de reseñas
        if self.reaccion_seleccionada :
            Reacciones.guardar_reacciones(
                id = id_resenia,
                id_evento = id_evento_actual,
                id_usuario = id_usuario_actual,
                calificacion = calificacion,
                comentario = texto,
                animo = self.reaccion_seleccionada,
                archivo_json = "data/rewies.json"
            )
        else :
            CTkMessagebox(title = "Campo Vacío", message = "Por favor, indique su reaccion del comentario.")

        #Mostrar mensaje de éxito
        CTkMessagebox(title = "Reseña Guardada", message = "La reseña se ha guardado correctamente.")

    def limpiar(self) :
    
        self.textbox.delete("1.0", "end")
        self.slider.set(1)
        self.reaccion_seleccionada = None