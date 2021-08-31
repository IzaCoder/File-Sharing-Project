import json

# Declare constant
BASE_PATH = "./data/"

def get(data):
    with open(BASE_PATH + data + ".json", "r") as data_file:
        return json.loads(data_file.read())
