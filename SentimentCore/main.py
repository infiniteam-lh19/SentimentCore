import random
from time import sleep

from SentimentCore.consumer.keyboard_consumer import KeyboardConsumer
from SentimentCore.consumer.light_consumer import LightConsumer
from SentimentCore.consumer.websocket_consumer import WebSocketConsumer
from SentimentCore.core.state_change_dispatcher import StateChangeDispatcher

def main():
    print("Test")

    dispatcher = StateChangeDispatcher()
    keyboardConsumer = KeyboardConsumer()
    lightConsumer = LightConsumer()
    websocketConsumer = WebSocketConsumer()

    dispatcher.attach(lightConsumer)
    dispatcher.attach(keyboardConsumer)
    dispatcher.attach(websocketConsumer)

    while True:
        dispatcher.event_update(random.random())
        sleep(1)



if __name__ == '__main__':
    main()
