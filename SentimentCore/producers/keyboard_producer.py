import pyxhook

class KeyboardProducer():

    _listeners = []

    def add_listener(self, that):
        self._listeners.append(that)

    def on_event(self, event):
        for listener in self._listeners:
            listener.consume(event) # TODO

    def __init__(self):

        self.hook = pyxhook.HookManager()
        self.hook.KeyDown = self.on_event
        self.hook.HookKeyboard()
        self.hook.start()
