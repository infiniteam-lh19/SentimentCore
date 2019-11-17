import colorsys
import json

import requests

from SentimentCore.core.observer import Observer
from SentimentCore.util.color_space_utils import red_white_green
from SentimentCore.util.rgb_xy_converter import Converter


class LightConsumer(Observer):

    def __init__(self):
        self._token = "U5n6uDzCWE0dyMGOU3auhvRKS7WaxCYiWHeMIAxx"
        self._light_ids = [1, 2]
        self._bri = 30
        self._converter = Converter()

    def update(self, tuple):
        sentence, emotional_score, start, end = tuple
        r, g, b = red_white_green(emotional_score)
        xy = self._converter.rgb_to_xy(r, g, b)
        state = True

        for light_id in self._light_ids:
            URL = "http://192.168.1.2/api/{}/lights/{}/state".format(self._token, light_id)
            BODY = {"on": state, "xy": xy, "bri": self._bri}
            BODY = json.dumps(BODY)

            requests.put(url=URL, data=BODY)

