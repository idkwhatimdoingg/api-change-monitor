import json
from pathlib import Path


STATE_FILE = Path("data/state.json")


def save_state(state):
    STATE_FILE.parent.mkdir(exist_ok=True)

    with open(STATE_FILE, "w", encoding="utf-8") as file:
        json.dump(state, file, indent=4)


def load_state():
    if not STATE_FILE.exists():
        return {}

    with open(STATE_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return {
        int(key): value
        for key, value in data.items()
    }