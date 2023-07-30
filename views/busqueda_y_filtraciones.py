#Importacion de funciones.
from tkinter import *
from views.detalles_eventos import Detalles_Eventos
import customtkinter
from CTkMessagebox import CTkMessagebox
from models.eventos import Eventos

#Declaracion de clases.
class Busqueda_Filtraciones(customtkinter.CTkToplevel):

    """ """

    #Declaracion de metodos.
    def __init__ (self, ventana) :
        
        """Metodo Constructor."""
        super().__init__(ventana)
        self.title("Busqueda y Filtraciones.")
        self.geometry("600x350")    
        self.resizable(False, False)
        self.iconbitmap("assets\musica.ico")
        eventos = Eventos.cargar_eventos("data/indice_de_eventos.json")
        self.eventos = eventos

        #Frame principal.
        self.frame_pri = customtkinter.CTkFrame(self)
        self.frame_pri.grid(row = 0, column = 0, sticky = "snew")
        self.frame_pri.grid_rowconfigure(0, weight=1)
        self.frame_pri.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #Creacion de una tabla.
        self.tabview = customtkinter.CTkTabview(self.frame_pri, width=350)
        self.tabview.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.tabview.add("Busqueda")
        self.tabview.add("Filtrado")
        self.tabview.tab("Busqueda").grid_columnconfigure(0, weight=1) 
        self.tabview.tab("Filtrado").grid_columnconfigure(0, weight=1)

        #Etiquetas de busqueda.
        self.etiqueta_busqueda = customtkinter.CTkLabel(self.tabview.tab("Busqueda"), text = "Ingrese el nombre del evento: ")
        self.etiqueta_genero = customtkinter.CTkLabel(self.tabview.tab("Busqueda"), text = "Escriba el genero musical: ")
        self.etiqueta_artista = customtkinter.CTkLabel(self.tabview.tab("Busqueda"), text = "Ingrese el nombre del artista: ")
        self.etiqueta_busqueda.grid(row=0, column = 0, pady = 7)
        self.etiqueta_genero.grid(row=1, column = 0, pady = 7)
        self.etiqueta_artista.grid(row=2, column = 0, pady = 7)

        #Entrys de busqueda.
        self.entrada_busqueda = customtkinter.CTkEntry(self.tabview.tab("Busqueda"))
        self.entrada_busqueda.grid(row = 0, column = 1)
        self.entrada_genero = customtkinter.CTkEntry(self.tabview.tab("Busqueda"))
        self.entrada_genero.grid(row = 1, column = 1)
        self.entrada_artista = customtkinter.CTkEntry(self.tabview.tab("Busqueda"))
        self.entrada_artista.grid(row = 2, column = 1)

        #Boton de busqueda.
        self.boton = customtkinter.CTkButton(self.tabview.tab("Busqueda"), text="Iniciar busqueda", command = self.busqueda)
        self.boton.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "nsew")
        
        #Etiquetas de filtrado.
        self.etiqueta_ubicacion = customtkinter.CTkLabel(self.tabview.tab("Filtrado"), text = "Ingrese la ubicacion del evento: ")
        self.etiqueta_horario = customtkinter.CTkLabel(self.tabview.tab("Filtrado"), text = "Escriba el horario del evento: ")
        self.etiqueta_ubicacion.grid(row=0, column = 0, pady = 7)
        self.etiqueta_horario.grid(row=1, column = 0, pady = 7)

        #Entrys de filtrado.
        self.entrada_ubicacion = customtkinter.CTkEntry(self.tabview.tab("Filtrado"))
        self.entrada_ubicacion.grid(row = 0, column = 1)
        self.entrada_horario = customtkinter.CTkEntry(self.tabview.tab("Filtrado"), placeholder_text="00:00")
        self.entrada_horario.grid(row = 1, column = 1, sticky = "w",padx=5)
        self.entrada_horario.configure(width = 50)

        #Boton de filtrado:
        self.boton_filtro = customtkinter.CTkButton(self.tabview.tab("Filtrado"), text="Iniciar busqueda", command = self.busqueda_filtrado)
        self.boton_filtro.grid(row = 3, column = 0, padx = 5, pady = 5)
 
        #Frame para contener la listabox de eventos encontrados.
        self.frame2 = customtkinter.CTkFrame(self.frame_pri, width=350, height = 200)
        self.frame2.grid(row = 0, column = 2, padx = 10, pady = 10)

        #Creacion de una Listbox para mostrar los eventos encontrados.
        self.listbox = Listbox(self.frame2, height=15, width = 30)
        self.listbox.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.listbox.bind("<Double-Button-1>", self.seleccionar_evento)

    def seleccionar_evento (self, event) :

        # Obtener el índice del evento seleccionado en el ListBox
        index = self.listbox.curselection()
        if index:
            index = int(index[0])
            evento_seleccionado = self.eventos[index]
            self.detalles = Detalles_Eventos(self, evento_seleccionado)
            self.detalles.grid(row=0, column=0, sticky="nsew")


    def busqueda (self) :

        """ 
        Este metodo se encargar de realizar una busqueda de un evento segun: el nombre del evento, el genero musical y el
        nombre del artista.
            
        """

        #Procesamiento de datos.
        nombre_evento = self.entrada_busqueda.get()
        genero = self.entrada_genero.get()
        artista = self.entrada_artista.get()
        resultado = []

        #Borramos los resultados anteriores de la listbox.
        self.listbox.delete(0, END)

        if not nombre_evento and not genero and not artista:
            CTkMessagebox(title="Campos vacíos", message="Rellene al menos uno de los campos de búsqueda.")
            return
        
        #Cargar eventos del archivo json.
        for evento in self.eventos :
            if (
                nombre_evento.lower() == evento.nombre.lower()
                and genero.lower() in evento.genero.lower()
                and artista.lower() in evento.artista.lower()
               ): 
                resultado.append(evento)
        if resultado :
            self.agregar_eventos_encontrado(resultado)
        else :
            CTkMessagebox(title="No encontrado", message="No se encontro un evento con las caracteristicas mencionadas")
    
    def busqueda_filtrado (self) :
        
        """ """

        #Procesamiento de datos.
        hora = self.entrada_horario.get()
        ubicacion = self.entrada_ubicacion.get()
        resultado = []
    
        #Borramos los resultados anteriores de la listbox.
        self.listbox.delete(0, END)

        if not hora and not ubicacion :
            CTkMessagebox(title="Campos vacíos", message="Rellene al menos uno de los campos de búsqueda.")
            return
        
        for evento in self.eventos :
            if (evento.hora_inicio[11:] == hora and (ubicacion.lower() in evento.ubicacion.lower())) : 
                resultado.append(evento)
        if resultado :
            self.agregar_eventos_encontrado(resultado)
        else :
            CTkMessagebox(title="No encontrado", message="No se encontro un evento con las caracteristicas mencionadas") 

    def agregar_eventos_encontrado (self, eventos_encontrados) :

        """ Esta funcion agrega los eventos encontrados a la litsbox."""

        #Procesamiento de datos.
        for evento in eventos_encontrados :
            self.listbox.insert(END, evento.nombre)

