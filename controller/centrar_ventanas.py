#Importacion de funciones.
from tkinter import *

#Declaracion de clases.
class Centrar_Ventana :

    """Esta clase sirve para centrar una ventana con respecto a las dimensiones de la pantalla."""

    @classmethod
    def centrar(cls, ventana):

        window_width = ventana.winfo_reqwidth()
        window_height = ventana.winfo_reqheight()
        position_right = int(ventana.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(ventana.winfo_screenheight() / 2 - window_height / 2)
        ventana.geometry(f'{position_right}+{position_down}')
        