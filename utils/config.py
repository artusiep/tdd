import json
import os

from utils.singleton import Singleton


class Config(metaclass=Singleton):
    dirname = os.path.dirname(__file__)
    def __init__(self, path=os.path.join(dirname, '../config.json')):
        self.config = self.load_config(path)

    def load_config(self, path):
        with open(path) as config:
            return json.load(config)

    @property
    def language(self):
        return self.config['language']
