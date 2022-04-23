"""
randword.py Module
---

Adds color printing, escape sequence, and other text formatting functionality.

def randword() -> str - Returns a random uppercase word


"""

from random_word import RandomWords
"""
Copyright (c) 2018 Vaibhav Singh
Copyrights licensed under MIT License
https://github.com/vaibhavsingh97/random-word/blob/master/LICENSE
"""

import random
import string


def randword() -> str:
    """ Returns a random uppercase word with no punctuation.

    Intended to be concatenated at the end of file names to rapidly generate unique filenames. Generates 6-digit number on failure.
    :rtype: str
    :param: None
    :return: word
    """

    r = RandomWords()
    try:
        word = str((str(r.get_random_word()).upper()).replace("-", ""))
        while word == "NONE":
            word = str((str(r.get_random_word()).upper()).translate(str.maketrans('', '', string.punctuation)))
    except (RuntimeError, TypeError, NameError, KeyError, ValueError, ModuleNotFoundError):
        # Whoops, here's a random number instead!
        return str(random.randint(100000, 999999))
    return word
