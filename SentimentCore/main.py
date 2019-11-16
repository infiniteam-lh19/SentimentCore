import random
from time import sleep

from SentimentCore.consumer.light_consumer import LightConsumer
from SentimentCore.core.fiddle_classes import ConcreteSubject, ConcreteObserverA, ConcreteObserverB
from SentimentCore.core.state_change_dispatcher import StateChangeDispatcher


def main():
    print("Test")

    dispatcher = StateChangeDispatcher()
    lightConsumer = LightConsumer()

    dispatcher.attach(lightConsumer)

    while True:
        dispatcher.event_update(random.randint(1, 10))
        sleep(0.5)



if __name__ == '__main__':
    main()