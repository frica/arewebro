import sys
from pathlib import Path
import random
import os

BRO_LIST = ("Fabien", "Pierre", "Moufid",
            "Hugues", "Arnaud", "Bertrand",
            "David", "Amael", "Bastien",
            "Laurent", "François", "Adrien",
            "Alexandre")


def are_we_bro(name1, name2):
    f""" check if person {name1} if friend with person {name2}
        :return boolean
    """
    # TODO: better string compare
    if name1 in BRO_LIST and name2 in BRO_LIST:
        return True
    else:
        return False


def pick_random_image():
    """ pick a random image in the img folder
     :return filepath of an image
    """
    p = Path("../img")
    files = [x for x in p.iterdir() if x.is_file()]
    if not files:
        return None

    random_file = random.choice(files)
    print(resource_path(random_file))
    return resource_path(random_file)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
