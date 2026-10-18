"""Shared JSON loader used by reporting scripts."""

import json


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
