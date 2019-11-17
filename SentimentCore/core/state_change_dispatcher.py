from _ast import List

from SentimentCore.core.subject import Subject


class StateChangeDispatcher(Subject):

    _state: int = None
    _observers: List = []

    def attach(self, observer) -> None:
        print("StateChangeDispatcher: Attached an Consumer.")
        self._observers.append(observer)

    def detach(self, observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("StateChangeDispatcher: Notifying observers...")
        for observer in self._observers:
            observer.update(self._state)

    def event_update(self, state) -> None:
        if not state == self._state:
            self._state = state
            self.notify()