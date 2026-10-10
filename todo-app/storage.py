import json


def load_todos():
    try:
        with open("todo.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_todos(todos):
    with open("todo.json", "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)
