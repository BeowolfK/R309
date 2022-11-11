import re


def isValidEmail(email):
    regex = re.compile(
        r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    )
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def isValidName(name):
    regex = re.compile(r"[a-zA-Z]+")
    if re.fullmatch(regex, name):
        return True
    else:
        return False
