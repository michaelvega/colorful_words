"""
main script
---

For help: -h.
If package is run as a script or with python -m, other modules in the same package are imported, and main() will execute.

main() -> None - Prints random word in random color.
"""

import argparse
import os
import json
import logging
from ColorfulWords import global_


def main() -> None:
    """
    Takes in two positional command line arguments, logging_level and color, to indicate which logging level should be changed to what color.
    Updates settings.json.
    :return: None
    """
    possible_levels = ["debug", "info", "warning", "critical", "error"]
    possible_colors = ["red", "green", "yellow", "blue", "purple", "cyan", "gray", "white", "black"]

    parser = argparse.ArgumentParser(
        description="""
        ColorfulWords! Pass in a logging level then a color to change the level's output color in logs.
        """
    )

    # Set up positional arguments
    parser.add_argument('logging_level', help="Logging Level to update (debug, info, warning, critical, or error)")
    parser.add_argument('color', help="Updated Color (red, green, yellow, blue, purple, cyan, gray, white, or black)")

    args = parser.parse_args()

    # open settings JSON file

    with open("settings.json", 'r') as f1:
        settings = json.loads(f1.read())

    # update settings dict
    if args.logging_level in possible_levels:
        if args.color in possible_colors:
            if args.logging_level == "debug":
                settings['debug'] = args.color
            elif args.logging_level == "info":
                settings['info'] = args.color
            elif args.logging_level == "warning":
                settings['warning'] = args.color
            elif args.logging_level == "critical":
                settings['critical'] = args.color
            elif args.logging_level == "error":
                settings['error'] = args.color
        else:
            raise ValueError("Invalid Color")
    else:
        raise ValueError("Invalid Level")

    # Write back settings JSON file with settings dict
    json_object = json.dumps(settings, indent=4)
    with open("settings.json", 'w') as f2:
        f2.write(json_object)

    # Update the formats
    global_.updateFormats()

    # global_.handler.setFormatter(colorlogging.CustomFormatter())

    logging.debug("New Colors")
    logging.info("New Colors")
    logging.warning("New Colors")
    logging.error("New Colors")
    logging.critical("New Colors")


if __name__ == '__main__':
    logging.debug("Default")
    logging.info("Colors")
    logging.warning("Are")
    logging.critical("Shown")
    logging.error("Here")
    main()
