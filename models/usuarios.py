#Importacion de funciones
import json 
import uuid

#Declaracion de clases.
class Usuario:

    def __init__(self, id, nombre, apellido, asistencias = None) :
        
        """ Metodo constructor."""
        
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        if asistencias is None :
            self.asistencias = []
        else :
            self.asistencias = asistencias

    @classmethod
    def generar_id(cls):

        return str(uuid.uuid4())

    @staticmethod
    def cargar_usuarios(archivo_json) :

        """ Metodo que permite cargar los datos almacenados en los archivos json."""
        try:
            with open(archivo_json, "r") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            datos = []
        return [Usuario(**dato) for dato in datos]

    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)

    @staticmethod
    def guardar_usuario(nuevo_usuario, archivo_json):

        """ Este método permite guardar un nuevo usuario que no existe en los datos del sistema."""

        #Cargamos los usuarios existentes desde el archivo
        datos_guardados = Usuario.cargar_usuarios(archivo_json)

        #Verificamos si el nuevo usuario ya existe en la lista de usuarios
        if any(usuario.apellido == nuevo_usuario.apellido and usuario.nombre == nuevo_usuario.nombre for usuario in datos_guardados):
            
            print("El usuario ya existe en la lista.")
        
        else:
            
            #Agregamos el nuevo usuario a la lista de usuarios
            datos_guardados.append(nuevo_usuario)

            #Convertimos la lista de usuarios a formato JSON y guardamos en el archivo
            with open(archivo_json, "w") as archivo:
                json.dump([usuario.__dict__ for usuario in datos_guardados], archivo)
