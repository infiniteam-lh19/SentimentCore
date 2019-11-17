from pynput.keyboard import Key, Listener
from dnnsent import sentiment
import time


def current_millis():
    return round(time.time() * 1000)


start = 0
end = 0
should_start = True

last_sentence = []
last_word = []

terminating = [".", "!", "?"]

def register_keylogger(dispatcher):

    def on_press(key):
        global last_word
        global last_sentence
        global start
        global end
        global should_start

        is_space = False
        back_space = False
        is_enter = False
        c = ''
        try: # Character
            c = key.char
        except AttributeError as ex: # Other
            if key == Key.space: # Space
                is_space = True
            elif key == Key.backspace: # Backspace
                back_space = True
            elif key == Key.enter:
                is_enter = True
            else: # Other
                return

        if should_start:
            should_start = False
            start = current_millis()

        is_terminating = c in terminating or is_enter

        if is_terminating or is_space:
            if len(last_word) > 0:
                last_sentence.append("".join(last_word))

        if is_terminating:
            sentence = " ".join(last_sentence)
            score = sentiment.sentiment_score(sentence)

            end = current_millis()

            print("'%s' / %s" % (sentence, score))

            dispatcher.event_update((sentence, score, start, end))

            should_start = True

            last_word.clear()
            last_sentence.clear()
        elif is_space:
            last_word.clear()
        elif back_space:
            if len(last_word) > 0:
                last_word.pop()
            else:
                if len(last_sentence) > 0:
                    last_word = list(last_sentence.pop())
                else:  # Nothing
                    should_start = True
        else:
            last_word.append(c)

    with Listener(on_press=on_press) as listener:
        listener.join()

