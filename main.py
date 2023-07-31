#Importacion de funciones.
from tkinter import * 
from CTkMessagebox import CTkMessagebox
from views.ventana_principal import Aplicacion
from models.usuarios import Usuario
from PIL import Image
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
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
        self.iconbitmap("assets\musica.ico")
        self.geometry("620x325")
        self.rowconfigure(0, weight = 1)
        self.columnconfigure (0, weight = 1)

        #Centrar ventana.
        self.window_width = self.winfo_reqwidth()
        self.window_height = self.winfo_reqheight()
        self.position_right = int(self.winfo_screenwidth() / 2 - self.window_width / 2)
        self.position_down = int(self.winfo_screenheight() / 2 - self.window_height / 2)
        self.geometry(f'+{self.position_right}+{self.position_down}')
        self.resizable(False, False)

        #Creacion de un frame principal.
        self.frame_principal = customtkinter.CTkFrame(self)
        self.frame_principal.grid(row = 0, column = 0, sticky = "snew")
        self.frame_principal.grid_rowconfigure(0, weight=1)
        self.frame_principal.grid_columnconfigure(0, weight=1)

        #Creacion de un Frame para los botones.
        self.frame = customtkinter.CTkFrame(self.frame_principal, width=110, height = 400)
        self.frame.grid(sticky="nsew", row = 0, column = 0, padx = 10, pady = 10)

        #Creacion de un Frame para una imagen.
        self.frame_imagen = customtkinter.CTkFrame(self.frame_principal, fg_color = "transparent")
        self.frame_imagen.grid(column = 1, sticky = "nsew", row = 0)
        self.imagen = customtkinter.CTkImage(light_image = Image.open("assets/artificial.jpg"), size = (300, 300))
        self.imagen_label = customtkinter.CTkLabel(master = self.frame_imagen, image= self.imagen, text = "")
        self.imagen_label.grid(padx = 10, pady = 10)

        #Creacion de un label de bienvenidad.
        self.label = customtkinter.CTkLabel(self.frame, text= "Bienvenido", font = customtkinter.CTkFont(family="Arial", size=15, weight="bold", underline = True, slant = "italic"), text_color = "#2F242C")
        self.label.grid(row = 0, column = 0, columnspan=2, padx = 10, pady = 10)

        #Creacion de etiqueta y entrada para el nombre.
        self.etiqueta_nombre = customtkinter.CTkLabel(self.frame, text="Ingrese su nombre:", font=customtkinter.CTkFont(family="Arial", size=12))
        self.etiqueta_nombre.grid(row=1, column=0, padx=5, pady=10, sticky="e")
        self.entrada_nombre = customtkinter.CTkEntry(self.frame)
        self.entrada_nombre.grid(row=1, column=1, padx=5, pady=10, sticky="w")

        #Creacion de etiqueta y entrada para el apellido.
        self.etiqueta_apellido = customtkinter.CTkLabel(self.frame, text="Ingrese su apellido:", font=customtkinter.CTkFont(family="Arial", size=12))
        self.etiqueta_apellido.grid(row=2, column=0, padx=(10, 5), pady=5, sticky="e")
        self.entrada_apellido = customtkinter.CTkEntry(self.frame)
        self.entrada_apellido.grid(row=2, column=1, padx=(5, 10), pady=5, sticky="w")

        #Creacion de botones de inicio y de cierre.
        self.boton_inicio = customtkinter.CTkButton(self.frame, text="Iniciar Aplicacion", command=self.iniciar_app)
        self.boton_inicio.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
        self.boton_cierre = customtkinter.CTkButton(self.frame, text="Cerrar Aplicacion", command=self.destroy)
        self.boton_cierre.grid(row=4, column=0, columnspan=2, padx=5, pady=10)
    
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
            self.frame_principal.grid_forget()        
            self.app = Aplicacion(self, nombre, apellido, self)
            self.app.grid(row = 0, column = 0, sticky = "snew")

        else:
            CTkMessagebox(title="Campo Vacio", message="Por favor ingrese sus datos")
    
    def volver_inicio_sesion (self) :

        self.app.grid_forget()  # Oculta el frame de Rewies
        self.frame_principal.grid(row = 0, column = 0, sticky = "snew")  # Vuelve a mostrar el frame de Detalles_Eventos

#Inicializador de la aplicacion.
if __name__ == '__main__' :

    app = Inicio_de_app()
    app.mainloop()
