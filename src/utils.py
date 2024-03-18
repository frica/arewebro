from pathlib import Path
import random


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
    return random_file
