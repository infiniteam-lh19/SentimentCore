from SentimentCore.core.observer import Observer
from SentimentCore.util.color_space_utils import red_white_green
import SentimentCore.util.keyboard_driver as keyboard_driver


class KeyboardConsumer(Observer):
    def __init__(self):
        pass

    def update(self, emotional_score):
        r, g, b = red_white_green(emotional_score)
        print("Color is: %s, %s, %s" %(r, g, b))
        keyboard_driver.set_color_all_nc(keyboard_driver.hex(r, g, b))
        keyboard_driver.commit()
