import json
import os


class Config:
    def __init__(self, config_path="config.json"):
        self.config_path = config_path
        self._load_config()

    def _load_config(self):
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Config file {self.config_path} not found!")

        with open(self.config_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def get(self, key, default=None):
        return self.data.get(key, default)

    def save(self):
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)


config = Config()


def debug_print(*args):
    if config.get("debug", False):
        print("[DEBUG]:", *args)
