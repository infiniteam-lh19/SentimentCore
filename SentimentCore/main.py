import random
from time import sleep

from SentimentCore.consumer.keyboard_consumer import KeyboardConsumer
from SentimentCore.consumer.light_consumer import LightConsumer
from SentimentCore.core.state_change_dispatcher import StateChangeDispatcher
from SentimentCore.producers.audio_producer import AudioProducer
from dnnsent import sentiment


def main():
    score = sentiment.sentiment_score("Test that shit")
    print(score)

   # audio_producer = AudioProducer()

    dispatcher = StateChangeDispatcher()
    keyboardConsumer = KeyboardConsumer()
    lightConsumer = LightConsumer()

    #dispatcher.attach(lightConsumer)
    dispatcher.attach(keyboardConsumer)

    for sentence in audio_producer:
        print(sentence)
        score = sentiment.sentiment_score(sentence)
        print(score)
        dispatcher.event_update(score)


if __name__ == '__main__':
    main()