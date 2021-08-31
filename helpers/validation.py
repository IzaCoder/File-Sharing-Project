import re

def valid_password(password):
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]',
                             password) is None
    password_ok = not (
        digit_error
        or uppercase_error
        or lowercase_error
        or symbol_error
    )

    return password_ok
