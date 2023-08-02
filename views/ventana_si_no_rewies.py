#Importacion de funcions
import customtkinter 

#Declaracion de clases.
class Ventana_Si_No(customtkinter.CTkToplevel) :

    """ Esta clase mostra dos botones para indicar si el usuario desea volver a escribir una reseña."""

    def __init__(self, root) :
        super().__init__(root)
        self.title("Aviso")
        self.geometry("340x170")
        self.resizable(False, False)

        self.label = customtkinter.CTkLabel(self, text = "Ya has escrito una reseña de esta evento\n¿Desea volver a escribir otra reseña ?")
        self.label.grid(padx = 10, pady = 20, row = 0, column = 0, columnspan = 2)

        #Declaracion de botones
        self.frame = customtkinter.CTkFrame(self)
        self.frame.grid(row = 1, column = 0, padx = 10, pady = 30)
        self.boton = customtkinter.CTkButton(self.frame, text = "Si", command = self.afirmacion)
        self.boton.grid(row = 0, column = 0)
        self.boton_no = customtkinter.CTkButton(self.frame, text = "No", command = self.negacion)
        self.boton_no.grid(row = 0, column = 1, padx = 10, pady = 30)

    def afirmacion (self) :
        self.destroy()
        return 0
    
    def negacion (self) :
        self.destroy()
        return  1