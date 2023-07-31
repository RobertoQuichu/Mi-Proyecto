#Importacion de funciones.
"""import folium
import requests
import polyline

#Declaracion de clases.
class Ruta_Planificacion :

    def __init__ (self) :
        pass
    def get_route(pickup_lat, pickup_lon, dropoff_lat, dropoff_lon, url="https://router.project-osrm.org/route/v1/driving/"):

        location = f"{pickup_lat},{pickup_lon};{dropoff_lat},{dropoff_lon}"
        response = requests.get(url + location)

        if response.status_code != 200:
            print(f"Error en la solicitud con código de estado {response.status_code}")
            return None

        response_json = response.json()
        route = polyline.decode(response_json['routes'][0]['geometry'])
        start_point = [response_json['waypoints'][0]['location'][1], response_json['waypoints'][0]['location'][0]]
        end_point = [response_json['waypoints'][1]['location'][1], response_json['waypoints'][1]['location'][0]]
        distance = response_json['routes'][0]['distance']

        return {
            'route': route,
            'start_point': start_point,
            'end_point': end_point,
            'distance': distance
               }

    def draw_map(lon_a, lat_a, lon_b, lat_b):

        route_data = get_route(lat_a, lon_a, lat_b, lon_b)

        if not route_data:
            print("No se pudo obtener los datos de la ruta.")
            return None

        map_instance = folium.Map(location=[lon_a, lat_a], zoom_start=15)

        folium.PolyLine(locations=route_data['route'], color="blue").add_to(map_instance)
        folium.Marker(location=[lon_a, lat_a], popup="Origin").add_to(map_instance)
        folium.Marker(location=[lon_b, lat_b], popup="Destination").add_to(map_instance)

        return map_instance

        # Coordenadas de origen y de destino
    lat_a, lon_a = -24.779672953246383, -65.43110913553649
    lat_b, lon_b = -24.848495969962894, -65.39926567496262

    drawn_map = draw_map(lat_a, lon_a, lat_b, lon_b)   
    drawn_map"""