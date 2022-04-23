"""
global_.py Module
---

Shared global state across modules.
Sets up logger with global variables. Needs to be imported to apply color to logging.

updateFormats() -> None - Prints random word in random color.
FMT - The format to output logs (By Default: [LEVEL]: message)
handler - Logging stream handler
"""

import logging
import json
from ColorfulWords.colorlogging import CustomFormatter
from ColorfulWords.colorprinting import colorCode


# Level name colors
def updateFormats() -> dict:
    """
    Sets up format for each of the different logging levels with a specified color.
    Default:
    * DEBUG: gray
    * INFO: green
    * WARNING: yellow
    * CRITICAL: red
    * ERROR: red
    :parameter: None
    :rtype: dict
    :return: FORMATS dictionary to be used in colorlogging.py module to apply color settings to logging.
    """
    with open("settings.json", "r") as ff:
        logging_colors = json.loads(ff.read())

    FORMATS = {
        logging.DEBUG: f"\33[{colorCode(logging_colors['debug'])}m{FMT}\33[0m",  # Gray
        logging.INFO: f"\33[{colorCode(logging_colors['info'])}m{FMT}\33[0m",  # Green
        logging.WARNING: f"\33[{colorCode(logging_colors['warning'])}m{FMT}\33[0m",  # Yellow
        logging.CRITICAL: f"\33[{colorCode(logging_colors['critical'])}m{FMT}\33[0m",  # Red
        logging.ERROR: f"\33[{colorCode(logging_colors['error'])}m{FMT}\33[0m",  # Red
    }
    return FORMATS


# Logging message formats
FMT = "[{levelname}]: {message}"  # Logging message format

# Logging Configuration
handler = logging.StreamHandler()
handler.setFormatter(CustomFormatter())
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[handler]
)
