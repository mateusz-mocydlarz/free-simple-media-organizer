# -*- coding: utf-8 -*-
from socket import gethostname
from getpass import getuser


def get_hostname_user() -> str:
    """Return concatenate string hostname and username

    Returns:
        str: hostname/username
    """
    return f"{ gethostname() }/{ getuser() }"


if __name__ == "__main__":
    print(get_hostname_user())
