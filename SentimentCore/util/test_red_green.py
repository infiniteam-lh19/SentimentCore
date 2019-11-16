import colorsys
import SentimentCore.util.keyboard_driver as kb
import SentimentCore.util.color_space_utils as color_utils
import time

red = (255, 0, 0)
green = (0, 255, 0)


while True:
    n = 100
    for i in [*range(n), *range(n, 0, -1)]:
        result = color_utils.calculate_color(red, green, i / n)
        r, g, b = result
        code = kb.hex(r, g, b)

        kb.set_color_all_nc(code)
        kb.commit()

        time.sleep(0.01)