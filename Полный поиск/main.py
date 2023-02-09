from io import BytesIO
import requests
from PIL import Image
import functions


geocoder_api_server, geocoder_params = functions.make_geocoder_params()
response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    pass

json_response = response.json()

map_api_server, map_params = functions.make_map_params(json_response)
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()