lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special = "~`!@#$%^&*()_+-= ("


def check_pwd(pwd: str) -> bool:
    """Takes a password and verifies if whether or not it means requirements.
    :param pwd: a password string
    :return: True if password is valid, False otherwise
    """
    if len(pwd) < 8:
        return False
    if len(pwd) > 20:
        return False
    low = False
    for letter in lowercase:
        if letter in pwd:
            low = True
            break
        up = False
    up = False
    for letter in uppercase:
        if letter in pwd:
            up = True
            break
    num = False
    for number in numbers:
        if number in pwd:
            num = True
            break
    spec = False
    for character in special:
        if character in pwd:
            spec = True
            break
    if up is True and low is True and num is True and spec is True:
        return True
    else:
        return False
