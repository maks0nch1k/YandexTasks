def make_geocoder_params():
    toponym_to_find = "СПб Митрополичий сад"

    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    return geocoder_api_server, geocoder_params


def make_map_params(json_response):
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]

    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    lowerCorner = toponym["boundedBy"]["Envelope"]["lowerCorner"].split()
    upperCorner = toponym["boundedBy"]["Envelope"]["upperCorner"].split()
    spn = (str((float(upperCorner[0]) - float(lowerCorner[0])) / 2), str((float(upperCorner[1]) - float(lowerCorner[1])) / 2))
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join(spn),
        "l": "map",
        "pt": ",".join(toponym_coodrinates.split())
    }

    return map_api_server, map_params