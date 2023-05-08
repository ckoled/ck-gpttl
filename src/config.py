import configparser

class _Config:
    def __init__(self):
        parser = configparser.ConfigParser()
        parser.read('config.ini')
        self.openai = dict(parser.items('openai'))

config = _Config()