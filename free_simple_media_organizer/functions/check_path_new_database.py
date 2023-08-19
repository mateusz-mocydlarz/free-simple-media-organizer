# -*- coding: utf-8 -*-
from os import listdir
import gettext

_ = gettext.gettext


def check_path_new_database(path) -> str:
    """Check path to new db

    Args:
        path (_type_): path to check
    """

    if path != "":
        if len(listdir(path)) == 0:
            return _("OK")
        else:
            return _("Path is not empty")
    else:
        return _("Not choosem path")


if __name__ == "__main__":
    test_path = "/Users/mocny/Documents/programming/python/free-simple-media-organizer/.tmp/testowa baza"
    print(check_path_new_database(test_path))
