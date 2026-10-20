import json


class ConfigReader:

    _instance = {}

    def __new__(cls, config_file):
        if config_file not in cls._instance:
            cls._instance[config_file] = super().__new__(cls)
        return cls._instance[config_file]

    def __init__(self, config_file):
        self.config_file = config_file

    def read_config(self, config_file):
        with open(config_file, "r") as f:
            config = json.load(f)
            return config

    def get_url(self):
        config = self.read_config(self.config_file)
        return config["testing_url"]