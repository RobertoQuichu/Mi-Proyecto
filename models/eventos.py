#Importacion de funciones.
import json 

#Declaracion de clases.
class Eventos :

    """ Esta clase carga los datos almacenados en los archivos json."""

    #Declaracion de metodos.
    def __init__ (self, id, nombre, artista, genero, ubicacion ,id_ubicacion, hora_inicio, hora_fin, descripcion, imagen) :

        """ Metodo constructor de la clase Eventos."""

        #Procesamiento de datos.
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero 
        self.ubicacion = ubicacion
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.descripcion = descripcion
        self.imagen = imagen

    def a_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def de_json(cls, datos_json) :
        
        datos = json.loads(datos_json)
        return cls(**datos)

    @staticmethod
    def cargar_eventos(archivo_json) :

        with open(archivo_json, "r") as archivo:
            datos = json.load(archivo)
        return [Eventos(**dato) for dato in datos] 