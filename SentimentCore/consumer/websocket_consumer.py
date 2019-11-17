import colorsys
import json

from flask import Flask, render_template
from flask_socketio import SocketIO

import requests
import threading

from SentimentCore.core.observer import Observer
from SentimentCore.util.color_space_utils import red_white_green
from SentimentCore.util.rgb_xy_converter import Converter

class WebSocketConsumer(Observer):

    def start(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'secret!'
        self.socketio = SocketIO(self.app, cors_allowed_origins="*")
        self.socketio.run(self.app)
        print("Websocket server started.")

    def __init__(self):
        threading.Thread(target=self.start).start()

    def update(self, tuple):
        sentence, emotional_score, start, end = tuple
        self.socketio.emit('update', {'source': 0, 'text': sentence, 'score': emotional_score, 'start': start, 'end': end})


