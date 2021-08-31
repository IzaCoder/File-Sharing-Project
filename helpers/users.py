import json
import os

import globals

# Declare variables
USERS_PATH = "./data/users.json"

def get():
    """
    This method returns a dictionary containing user info for all users. The dictionary is formatted like (types are in parentheses):
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
    with open(USERS_PATH, "r") as f:
        # Return dictionary described in docstring
        return json.loads(f.read())

def update(users):
    """
    Update 
    with open(USERS_PATH, "w") as f:
        f.write(json.dumps(users))

def new_user(username, password):
    # Get variables
    users = get()
    global_vars = globals.get()

    # Update variables
    os.environ[username] = password
    global_vars["logged_in"] = username
    
    # Create dictionary with user info
    # Password is omitted for security reasons
    user_dict = {
        "username": username,
        "documents": [],
        "groups": [],
        "folders": []
    }

    # Update variables again
    users[username] = user_dict

    # Write the changes made to the files
    update(users)
    globals.update(global_vars)