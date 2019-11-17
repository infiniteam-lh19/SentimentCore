import random
from time import sleep

from SentimentCore.consumer.keyboard_consumer import KeyboardConsumer
from SentimentCore.consumer.light_consumer import LightConsumer
from SentimentCore.consumer.websocket_consumer import WebSocketConsumer
from SentimentCore.core.state_change_dispatcher import StateChangeDispatcher
from SentimentCore.producers.audio_producer import AudioProducer
from dnnsent import sentiment

from SentimentCore.util.keylogger import register_keylogger


def main():
    score = sentiment.sentiment_score("Test that shit")
    print(score)

   # audio_producer = AudioProducer()

    dispatcher = StateChangeDispatcher()
    keyboardConsumer = KeyboardConsumer()
    lightConsumer = LightConsumer()
    websocketConsumer = WebSocketConsumer()

    #dispatcher.attach(lightConsumer)
    dispatcher.attach(keyboardConsumer)
    dispatcher.attach(websocketConsumer)

    register_keylogger(dispatcher)

    for sentence in audio_producer:
        print(sentence)
        score = sentiment.sentiment_score(sentence)
        print(score)
        dispatcher.event_update(score)


if __name__ == '__main__':
    main()
