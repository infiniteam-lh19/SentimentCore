from SentimentCore.core.observer import Observer


class LightConsumer(Observer):

    def update(self, subject):
        print("Emotion is " + str(subject))
