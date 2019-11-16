from SentimentCore.core.observer import Observer
from SentimentCore.util.color_space_utils import calculate_color
import SentimentCore.util.keyboard_driver as keyboard_driver


class KeyboardConsumer(Observer):
    def __init__(self):
        self._angry_color = (255, 0, 0)
        self._happy_color = (0, 255, 0)

    def update(self, emotional_score):
        r, g, b = calculate_color(self._angry_color, self._happy_color, emotional_score)
        print("Color is: %s, %s, %s" %(r, g, b))
        keyboard_driver.set_color_all_nc(keyboard_driver.hex(r, g, b))
        keyboard_driver.commit()
