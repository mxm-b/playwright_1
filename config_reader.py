import json


class ConfigReader:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def read_config(self):
        with open("config.json", "r") as f:
            config = json.load(f)
            return config

    def get_tests(self):
        config = self.read_config()
        return config["tests"]
