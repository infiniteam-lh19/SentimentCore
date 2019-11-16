from SentimentCore.core.fiddle_classes import ConcreteObserverA, ConcreteObserverB, ConcreteSubject


def main():
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()

if __name__ == "__main__":
    main()
    # The client code.

