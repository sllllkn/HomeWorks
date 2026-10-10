
import string
import keyword

def check_variable_name(name):
    if not name:
        return False

    if name in keyword.kwlist:
        return False

    if name[0].isdigit():
        return False

    if any(char.isupper() for char in name):
        return False

    if any(char in string.punctuation and char != "_" for char in name):
        return False

    if "__" in name:
        return False

    return True
