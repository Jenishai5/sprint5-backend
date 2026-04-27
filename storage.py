import json
import os

FILE = "history.json"


def load_history():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_entry(entry):
    history = load_history()
    history.append(entry)

    with open(FILE, "w") as f:
        json.dump(history, f, indent=2)
