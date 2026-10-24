import requests
import urllib.parse

route_url = "https://graphhopper.com/api/1/route?"
key = "f1fd44e9-4ef0-4055-b636-17fbc36b8879"

SALIDA = ("s", "salir")


def geocoding(location, key):
    while location == "":
        location = input("Ingrese la ubicación nuevamente: ")
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode(
        {"q": location, "limit": "1", "key": key, "locale": "es"})

    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code

    if json_status == 200 and len(json_data["hits"]) != 0:
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
        name = json_data["hits"][0]["name"]
        value = json_data["hits"][0]["osm_value"]
        country = json_data["hits"][0].get("country", "")
        state = json_data["hits"][0].get("state", "")

        if state and country:
            new_loc = name + ", " + state + ", " + country
        elif country:
            new_loc = name + ", " + country
        else:
            new_loc = name

        print("URL de la API de Geocodificación para " + new_loc +
              " (Tipo de ubicación: " + value + ")\n" + url)
    else:
        lat = "null"
        lng = "null"
        new_loc = location
        if json_status != 200:
            print("Estado de la API de Geocodificación: " + str(json_status) +
                  "\nMensaje de error: " + json_data.get("message", ""))
    return json_status, lat, lng, new_loc


while True:
    print("\n+++++++++++++++++++++++++++++++++++++++++++++")
    print("Perfiles de vehículo disponibles en Graphhopper:")
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print("car (auto), bike (bicicleta), foot (a pie)")
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    profile = ["car", "bike", "foot"]
    vehicle = input("Ingrese un perfil de vehículo de la lista (s o salir para terminar): ").strip()
    if vehicle.lower() in SALIDA:
        print("Saliendo del programa. ¡Hasta luego!")
        break
    elif vehicle in profile:
        vehicle = vehicle
    else:
        vehicle = "car"
        print("No se ingresó un perfil válido. Se usará el perfil car (auto).")

    loc1 = input("Ubicación de origen (s o salir para terminar): ").strip()
    if loc1.lower() in SALIDA:
        print("Saliendo del programa. ¡Hasta luego!")
        break
    orig = geocoding(loc1, key)

    loc2 = input("Destino (s o salir para terminar): ").strip()
    if loc2.lower() in SALIDA:
        print("Saliendo del programa. ¡Hasta luego!")
        break
    dest = geocoding(loc2, key)

    print("=================================================")
    if orig[0] == 200 and dest[0] == 200:
        op = "&point=" + str(orig[1]) + "%2C" + str(orig[2])
        dp = "&point=" + str(dest[1]) + "%2C" + str(dest[2])
        paths_url = route_url + urllib.parse.urlencode(
            {"key": key, "vehicle": vehicle, "locale": "es"}) + op + dp
        paths_status = requests.get(paths_url).status_code
        paths_data = requests.get(paths_url).json()
        print("Estado de la API de Rutas: " + str(paths_status) +
              "\nURL de la API de Rutas:\n" + paths_url)
        print("=================================================")
        print("Indicaciones desde " + orig[3] + " hasta " + dest[3] +
              " en " + vehicle)
        print("=================================================")

        if paths_status == 200:
            km = paths_data["paths"][0]["distance"] / 1000
            millas = km / 1.61
            seg = int(paths_data["paths"][0]["time"] / 1000 % 60)
            mins = int(paths_data["paths"][0]["time"] / 1000 / 60 % 60)
            hrs = int(paths_data["paths"][0]["time"] / 1000 / 60 / 60)
            print("Distancia recorrida: {0:.2f} millas / {1:.2f} km".format(millas, km))
            print("Duración del viaje: {0:02d}:{1:02d}:{2:02d}".format(hrs, mins, seg))
            print("=================================================")
            print("Narrativa del viaje:")
            for each in range(len(paths_data["paths"][0]["instructions"])):
                path = paths_data["paths"][0]["instructions"][each]["text"]
                distance = paths_data["paths"][0]["instructions"][each]["distance"]
                print("{0} ( {1:.2f} km / {2:.2f} millas )".format(
                    path, distance / 1000, distance / 1000 / 1.61))
            print("=================================================")
        else:
            print("Mensaje de error: " + paths_data.get("message", ""))
            print("*************************************************")