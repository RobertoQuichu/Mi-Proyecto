#Importacion de funciones.
from tkinter import * 
from CTkMessagebox import CTkMessagebox
from views.ventana_principal import Aplicacion
from models.usuarios import Usuario
import customtkinter

class Inicio_de_app(customtkinter.CTk)  :

    """ 
    Esta clase inicia la ventana principal en la cual el usuario ingresara su nombre
    con el cual el programa se referira a el
    
    """
    #Declaracion de metodos.
    def __init__(self) :
        
        """ Metodo constructor. """
        
        #Procesamiento de datos.
        super().__init__()
        self.title("App Music Tour")
        self.iconbitmap("assets\ondas-sonoras.ico")

        #Centrar ventana.
        window_width = self.winfo_reqwidth()
        window_height = self.winfo_reqheight()
        position_right = int(self.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(self.winfo_screenheight() / 2 - window_height / 2)
        self.geometry(f'+{position_right}+{position_down}')
        
        #Creacion de un Frame.
        frame = customtkinter.CTkFrame(self, width=310)
        frame.grid(sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        #Creacion de etiqueta y entrada para el nombre.
        self.etiqueta_nombre = customtkinter.CTkLabel(frame, text="Ingrese su nombre:", font=customtkinter.CTkFont(family="Arial", size=12))
        self.etiqueta_nombre.grid(row=0, column=0, padx=5, pady=10, sticky="e")
        self.entrada_nombre = customtkinter.CTkEntry(frame)
        self.entrada_nombre.grid(row=0, column=1, padx=5, pady=10, sticky="w")

        #Creacion de etiqueta y entrada para el apellido.
        self.etiqueta_apellido = customtkinter.CTkLabel(frame, text="Ingrese su apellido:", font=customtkinter.CTkFont(family="Arial", size=12))
        self.etiqueta_apellido.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="e")
        self.entrada_apellido = customtkinter.CTkEntry(frame)
        self.entrada_apellido.grid(row=1, column=1, padx=(5, 10), pady=5, sticky="w")

        #Creacion de botones de inicio y de cierre.
        boton_inicio = customtkinter.CTkButton(frame, text="Iniciar Aplicacion", command=self.iniciar_app)
        boton_inicio.grid(row=2, column=0, columnspan=2, padx=5, pady=10)
        boton_cierre = customtkinter.CTkButton(frame, text="Cerrar Aplicacion", command=self.destroy)
        boton_cierre.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
    
    def iniciar_app(self):

        """Este método da inicio a las comandos principales de la aplicación."""

        #Procesamiento de datos.
        nombre = self.entrada_nombre.get()
        apellido = self.entrada_apellido.get()

        #Cargamos los archivos existentes.
        if nombre and apellido:

            #Creamos una instancia de Usuario con los datos ingresados
            nuevo_usuario = Usuario(id="", nombre=nombre, apellido=apellido, asistencias=[])

            #Guardamos el nuevo usuario en el archivo JSON
            nuevo_usuario.guardar_usuario(nuevo_usuario ,"data/nombre_usuario.json")

            self.app = Aplicacion(nombre, apellido)
            self.app.protocol("WW_DELETE_WINDOW", self.withdraw())
        else:
            CTkMessagebox(title="Campo Vacio", message="Por favor ingrese sus datos")
