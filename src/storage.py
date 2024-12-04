import json

from src.config import default_path


def collect_data(path: str = default_path) -> dict:
    ''''''
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def update_json(data: dict) -> None:
    ''''''
    with open(default_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    data = collect_data()
    print(len(data))
