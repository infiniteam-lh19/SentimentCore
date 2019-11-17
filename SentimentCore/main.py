import random
from time import sleep, time

from senti_classifier import senti_classifier

from SentimentCore.consumer.keyboard_consumer import KeyboardConsumer
from SentimentCore.consumer.light_consumer import LightConsumer
from SentimentCore.consumer.websocket_consumer import WebSocketConsumer
from SentimentCore.core.state_change_dispatcher import StateChangeDispatcher
from SentimentCore.producers.audio_producer import AudioProducer
import numpy as np
from dnnsent import sentiment

from SentimentCore.util.keylogger import register_keylogger


def main():
    audio_producer = AudioProducer()

    dispatcher = StateChangeDispatcher()
    keyboardConsumer = KeyboardConsumer()
    lightConsumer = LightConsumer()
    websocketConsumer = WebSocketConsumer()

    dispatcher.attach(lightConsumer)
    dispatcher.attach(keyboardConsumer)
    dispatcher.attach(websocketConsumer)

    #register_keylogger(dispatcher)

    start_time = round(time() * 1000)
    source = 1
    for sentence in audio_producer:
        # print(sentence)
        # pos_score, neg_score = senti_classifier.polarity_scores([sentence])
        # score_vec = np.array([pos_score, neg_score], dtype=np.float)
        # print(score_vec)
        # vector_norm = score_vec / float(2 * np.linalg.norm(score_vec))
        # print(vector_norm)
        # final_score = 0.5 + vector_norm[0] - vector_norm[1]
        # print(final_score)
        final_score = sentiment.sentiment_score(sentence)
        print(sentence)
        print(final_score)
        end_time = round(time() * 1000)
        obj = sentence, final_score, source, start_time, end_time
        dispatcher.event_update(obj)
        start_time = end_time

if __name__ == '__main__':
    main()
