import customtkinter

#Declaracion de clases.
class Controlador_Frames :

    """ Esta clase permitira el cambio y retornos de frames que se utilizen en la aplicacion."""

    #Declaracion de metodos.
    def __init__ (self) :

        """ Metodo constructor."""

        #Procesamiento de datos.
        self.vista_nueva = None
        self.vista_anterior = None

    def nueva_vista (self, vista, *args, **kwargs) :

        """ """

        if self.vista_nueva is not None :
            self.vista_nueva.grid_forget()
        self.vista_previa = self.vista_nueva
        self.vista_previa = vista(*args, **kwargs)
        self.vista_previa.grid (row = 0, column = 0, sticky = "snew")
        self.vista_previa.grid_rowconfigure(0, weight = 1)
        self.vista_previa.grid_columnconfigure(0, weight = 1)

    def volver_vista (self) :

        """"""

        if self.vista_anterior :
            self.nueva_vista(self.vista_previa.__class__, self.vista_previa.master)
    