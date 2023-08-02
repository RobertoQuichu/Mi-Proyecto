#Importacion de funciones
import json 
import uuid

#Declaracion de clases.
class Reacciones:

    def __init__(self, id, id_evento, id_usuario, calificacion, comentario, animo):

        """ Metodo constructor."""

        self.id = id
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo 
       
    @classmethod
    def generar_id(cls):

        return str(uuid.uuid4())   

    @staticmethod
    def cargar_reacciones (archivo_json) :

        """ Metodo que permite cargar los datos almacenados en los archivos json."""
        try:
            with open(archivo_json, "r") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            datos = []
        return [Reacciones(**dato) for dato in datos]

    @classmethod
    def de_json(cls, datos_json) :
        datos = json.loads(datos_json)
        return cls(**datos)

    @staticmethod
    def guardar_reacciones(id, id_evento, id_usuario, calificacion, comentario, animo, archivo_json):

        """ Este método permite guardar una nueva rewie que no existe en los datos del sistema."""

        #Agregamos una nueva reseña a la lista de reseñas
        datos_guardados = Reacciones.cargar_reacciones(archivo_json)
        nueva_resenia = Reacciones(id, id_evento, id_usuario, calificacion, comentario, animo)
        datos_guardados.append(nueva_resenia)

        #Convertimos la lista de reseñas a formato JSON y guardamos en el archivo
        with open(archivo_json, "w") as archivo :
            json.dump([nueva_resenia.__dict__ for nueva_resenia in datos_guardados], archivo)