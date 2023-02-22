import re

regex = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"


def check_valid_email(address):
    """Return True if email is valid"""
    if re.fullmatch(regex, address):
        return True
    return False
