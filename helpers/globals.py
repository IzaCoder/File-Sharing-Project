import json

GLOBALS_PATH = "./data/globals.json"

def get():
    with open(GLOBALS_PATH, "r") as f:
        return json.loads(f.read())

def update(globals):
    with open(GLOBALS_PATH, "w") as f:
        f.write(json.dumps(globals))