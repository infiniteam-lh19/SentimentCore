import requests
import json

def set_color_to_light(user_id, saturation, brightness, hue, light_id = 1, state = True):

	URL = "http://192.168.1.2/api/{}/lights/{}/state".format(user_id, light_id)

	BODY = {"on" : state, "sat" : saturation, "bri" : brightness, "hue" : hue}

	BODY = json.dumps(BODY)

	r = requests.put(url = URL, data = BODY)

	return r.text

response = set_color_to_light("", saturation=254, brightness = 150, hue = 5000)

print(response)