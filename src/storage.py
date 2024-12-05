import json

from src import config


def collect_data(path: str = config.path) -> dict:
    ''''''
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def update_json(data: dict) -> None:
    ''''''
    with open(config.path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)