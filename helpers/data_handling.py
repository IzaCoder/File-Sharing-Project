import json

# Declare constant
BASE_PATH = "./data/"

# Define method to get data from file
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
    
    # Open data file
    with open(BASE_PATH + data + ".json", "r") as data_file:
        # Return a dictionary from the JSON
        return json.loads(data_file.read())

# Define method to update the data in a file
def update(data_file, data):
    # Open data file in write mode
    with open(BASE_PATH + data_file + ".json", "w") as data_file:
        # Write JSON string to file
        data_file.write(json.dumps(data))
