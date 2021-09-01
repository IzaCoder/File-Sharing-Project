import json
import os

import helpers.data_handling

# Declare variables
USERS_PATH = "./data/users.json"


def new_user(username, password):
    # Get variables
    users = helpers.data_handling.get("users")
    global_vars = helpers.data_handling.get("globals")

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
    helpers.data_handling.update("users", users)
    helpers.data_handling.update("globals", global_vars)
