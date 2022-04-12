"""
main script
---

If package is run as a script or with python -m, other modules in the same package are imported, and main() will execute.

main() -> None - Prints random word in random color.
"""

from ColorfulWords.colorprinting import *
from ColorfulWords.colorlogging import *
from ColorfulWords.randword import *


def main():
    """
    Prints random word in a random color.
    :return: None
    """

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

    selected_color = onlyLowerCaseAlpha(selected_color)
    selected_color_code = str(colorCode(selected_color))
    logging.debug(f"Random Color: \33[{selected_color_code}m{selected_color}\33[0m")
    print_color_map[selected_color](randword())


if __name__ == '__main__':
    main()
