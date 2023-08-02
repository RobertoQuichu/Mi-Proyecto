#Importacion de funciones.
import folium
import requests
import polyline

#Declaracion de clases.
class Ruta_Planificacion:

    def __init__(self):
        pass

    def get_route(self, pickup_lat, pickup_lon, dropoff_lat, dropoff_lon, url="https://router.project-osrm.org/route/v1/driving/"):
        localizacion = f"{pickup_lat},{pickup_lon};{dropoff_lat},{dropoff_lon}"
        response = requests.get(url + localizacion)

        if response.status_code != 200:
            print(f"Error en la solicitud con código de estado {response.status_code}")
            return None

        response_json = response.json()
        ruta = polyline.decode(response_json['routes'][0]['geometry'])
        punto_inicial = [response_json['waypoints'][0]['location'][1], response_json['waypoints'][0]['location'][0]]
        punto_final = [response_json['waypoints'][1]['location'][1], response_json['waypoints'][1]['location'][0]]
        distancia = response_json['routes'][0]['distance']

        return {
            'ruta': ruta,
            'punto inicial': punto_inicial,
            'punto final': punto_final,
            'distancia': distancia
        }

    def draw_map(self, lon_a, lat_a, lon_b, lat_b):
        route_data = self.get_route(lat_a, lon_a, lat_b, lon_b)

        if not route_data:
            print("No se pudo obtener los datos de la ruta.")
            return None

        map_instance = folium.Map(location=[lat_a, lon_a], zoom_start=15)

        folium.PolyLine(locations=route_data['route'], color="blue").add_to(map_instance)
        folium.Marker(location=[lat_a, lon_a], popup="Origin").add_to(map_instance)
        folium.Marker(location=[lat_b, lon_b], popup="Destination").add_to(map_instance)

        return map_instance