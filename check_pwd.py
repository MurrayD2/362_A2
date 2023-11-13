def check_pwd(pwd: str) -> bool:
    """Takes a password and verifies if whether or not it means requirements.
    :param pwd: a password string
    :return: True if password is valid, False otherwise
    """
    if len(pwd) < 8:
        return False
    if len(pwd) > 20:
        return False
    else:
        return True
