import json

# Declare constant
BASE_PATH = "./data/"

def get(data):
    """
    This method returns data from the specified JSON file (don't include the extension, nor path).
    If data == users,
    this method returns a dictionary containing user info for all users. The dictionary is formatted like (types are in parentheses):
    {
        username (string): {
            "username": username (string),
            "documents": documents (list),
            "groups": groups (list),
            "folders": folders (list)
        }
    }
    To access this dictionary (assuming the return value of this method is assigned to `users`), use `users[username]`.
    Then, to access a specific property of that user, use `users[username][property]`.
    """
    with open(BASE_PATH + data + ".json", "r") as data_file:
        return json.loads(data_file.read())
