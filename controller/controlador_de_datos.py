#Importacion de funciones.
import json

#Declaracion de clases.
class Controlador_de_Datos :

    """ Esta clase almacenara los datos del usuario y se encargar de cargar los identificadores de los eventos a los cuales asistio."""

    def __init__(self, usuario, archivo_json) :
        self.usuario_actual = usuario
        self.archivo_json = archivo_json

    def get_usuario_actual(self) :
        return self.usuario_actual

    def agregar_evento_asistencia(self, evento_id) :

        if evento_id not in self.usuario_actual.asistencias:
            self.usuario_actual.asistencias.append(evento_id)
            self.guardar_asistencias()

    def eliminar_evento_asistencia(self, evento_id) :

        if evento_id in self.usuario_actual.asistencias:
            self.usuario_actual.asistencias.remove(evento_id)
            self.guardar_asistencias()

    def guardar_asistencias(self) :

        with open(self.archivo_json, "r") as archivo:
            datos = json.load(archivo)

        for dato in datos :
            if dato["id"] == self.usuario_actual.id :
                dato["asistencias"] = self.usuario_actual.asistencias

        with open(self.archivo_json, "w") as archivo :
            json.dump(datos, archivo, indent = 4)