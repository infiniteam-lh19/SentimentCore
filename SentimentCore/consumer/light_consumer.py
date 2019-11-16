import colorsys
import json

import requests

from SentimentCore.core.observer import Observer
from SentimentCore.util.color_space_utils import calculate_color
from SentimentCore.util.rgb_xy_converter import Converter


class LightConsumer(Observer):

    def __init__(self):
        self._token = "U5n6uDzCWE0dyMGOU3auhvRKS7WaxCYiWHeMIAxx"
        self._light_ids = [1, 2]
        self._angry_color = (255, 0, 0)
        self._happy_color = (0, 255, 0)
        self._bri = 30
        self._converter = Converter()

    def update(self, emotional_score):
        r, g, b = calculate_color(self._angry_color, self._happy_color, emotional_score)
        xy = self._converter.rgb_to_xy(r, g, b)
        state = True

        for light_id in self._light_ids:
            URL = "http://192.168.1.2/api/{}/lights/{}/state".format(self._token, light_id)
            BODY = {"on": state, "xy": xy, "bri": self._bri}
            BODY = json.dumps(BODY)

            requests.put(url=URL, data=BODY)

