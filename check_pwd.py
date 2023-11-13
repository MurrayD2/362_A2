lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"


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
    if low is True and up is True and num is True:
        return True
    else:
        return False
