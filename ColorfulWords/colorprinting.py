"""
colorprinting.py Module
---

Adds color printing, escape sequence, and other text formatting functionality.

Color Printing Functions:
    * printRed - Prints in red
    * printGreen - Prints in green
    * printYellow - Prints in yellow
    * printBlue - Prints in blue
    * printPurple - Prints in purple
    * printCyan - Prints in cyan
    * printGray - Prints in gray
    * printWhite - Prints in white
    * printBlack - Prints in black

Other Functions:
    * colorCode - returns ANSI code value of respective color
    * onlyLowerCaseAlpha - returns formatted text with only lowercase, alphabetical characters

"""
import logging
import random
import re

from ColorfulWords.randword import randword


def printRed(text: str) -> None:
    """
    Prints param with Red color formatting using ANSI escape sequences.
    :param text: text to be printed
    :return: None
    """
    print(f"\033[31m {text}\033[00m")


def printGreen(text: str) -> None:
    """
    Prints param with Green color formatting using ANSI escape sequences.
    :param text: text to be printed
    :return: None
    """
    print(f"\033[32m {text}\033[00m")


def printYellow(text: str) -> None:
    """
    Prints param with Yellow color formatting using ANSI escape sequences.
    :param text: text to be printed
    :return: None
    """
    print(f"\033[33m {text}\033[00m")


def printBlue(text: str) -> None:
    """
    Prints param with Light Purple color formatting using ANSI escape sequences.
    :param text: text to be printed
    :return: None
    """
    print(f"\033[34m {text}\033[00m")


def printPurple(text: str) -> None:
    """
    Prints param with Purple color formatting using ANSI escape sequences.
    :param text: text to be printed
    :return: None
    """
    print(f"\033[35m {text}\033[00m")


def printCyan(text: str) -> None:
    """
    Prints param with Yellow color formatting using ANSI escape sequences.
    :param text: text to be printed
    :return: None
    """
    print(f"\033[36m {text}\033[00m")


def printGray(text: str) -> None:
    """
    Prints param with Gray color formatting using ANSI escape sequences.
    :param text: text to be printed
    :return: None
    """
    print(f"\033[37m {text}\033[00m")


def printWhite(text: str) -> None:
    """
    Prints param with White color formatting using ANSI escape sequences.
    :param text: text to be printed
    :return: None
    """
    print(f"\033[97m {text}\033[00m")


def printBlack(text: str) -> None:
    """
    Prints param with Black color formatting using ANSI escape sequences.
    :param text: text to be printed
    :return: None
    """
    print(f"\033[30m {text}\033[00m")


def random_color_word() -> None:
    """
        Prints random word in a random color.
        :return: None
    """
    print_color_map = {
        "red": printRed,
        "green": printGreen,
        "yellow": printYellow,
        "blue": printBlue,
        "purple": printPurple,
        "cyan": printCyan,
        "gray": printGray,
        "white": printWhite,
        "black": printBlack
    }

    selected_color = random.choice([
        "Red",
        "Green",
        "Yellow",
        "Blue",
        "Purple",
        "Cyan",
        "Gray",
        "White",
        "Black"
    ])

    selected_color = onlyLowerCaseAlpha(selected_color)
    selected_color_code = str(colorCode(selected_color))
    logging.debug(f"Random Color: \33[{selected_color_code}m{selected_color}\33[0m")
    print_color_map[selected_color](randword())


def colorCode(color: str) -> int:
    """
    Returns ANSI code of inputted color as an int. Number can be used to properly format colors in terminal.
    :rtype: int
    :param color: Name of Color. Options:
    red, green, yellow, blue, purple, cyan, gray, white, black.
    :return: ANSI code of inputted color
    """
    color_formatted = onlyLowerCaseAlpha(color)
    color_map = {
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "purple": 35,
        "cyan": 36,
        "gray": 37,
        "white": 97,
        "black": 30
    }
    if color_formatted not in color_map.keys():
        raise KeyError("Not a supported Color")
    else:
        return int(color_map[color_formatted])


def onlyLowerCaseAlpha(text: str) -> str:
    """
    Returns formatted text with only lowercase, alphabetical characters.
    :param text: text to be formatted
    :return: formatted string
    """
    return str((re.sub(r'[^a-zA-Z]+', '', text)).lower())
