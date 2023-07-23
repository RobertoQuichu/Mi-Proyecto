#Importacion de funciones.
import customtkinter 
from views.login import Inicio_de_app

#Inicializador de la aplicacion.
if __name__ == '__main__' :

    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    app = Inicio_de_app()
    app.mainloop()