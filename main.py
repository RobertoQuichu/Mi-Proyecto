#Importacion de funciones.
import customtkinter 
from views.ventana_principal import Aplicacion

#Inicializador de la aplicacion.
if __name__ == '__main__' :

    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    app = Aplicacion()
    app.mainloop()