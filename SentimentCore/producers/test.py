from SentimentCore.producers.keyboard_producer import KeyboardProducer
import time
from string import ascii_lowercase
import random
import SentimentCore.util.keyboard_driver as kb

class TestConsumer():

    def consume(self, event):
        print(str(event))

# --

kb.set_color_all_nc("000000")
kb.commit()

def rand_b():
    return random.randint(0, 255)

while True:
    for c in ascii_lowercase:
        kb.set_color_key_nc(c, kb.hex(rand_b(), rand_b(), rand_b()))

    kb.commit()