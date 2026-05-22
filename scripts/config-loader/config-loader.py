#!/usr/bin/env python3
import json
import os
from pathlib import Path

class ConfigLoader:
    def __init__(self, env_prefix="APP"):
        self.config = {}
        self.env_prefix = env_prefix

    def load_json(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.config.update(self._flatten(data))
        return self

    def load_env(self):
        for key, value in os.environ.items():
            if key.startswith(f"{self.env_prefix}_"):
                config_key = key[len(self.env_prefix)+1:].lower()
                self.config[config_key] = value
        return self

    def _flatten(self, d, prefix=""):
        items = {}
        for k, v in d.items():
            key = f"{prefix}.{k}" if prefix else k
            if isinstance(v, dict):
                items.update(self._flatten(v, key))
            else:
                items[key] = v
        return items

    def get(self, key, default=None):
        return self.config.get(key, default)

if __name__ == "__main__":
    cfg = ConfigLoader().load_env()
    print(cfg.config)
