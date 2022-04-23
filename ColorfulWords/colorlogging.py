"""
colorlogging.py Module
---

Formats Logging to have colors according to FORMAT dict (specified in global_.py module)

CustomFormatter(logging.Formatter) - A class used to modify the existing logging Formatter instance by adding colors to logger messages.
| format(levelname) -> object - creates formatter object with the FORMAT dict (specified in global_.py module)
"""
import logging
#from ColorfulWords.global_ import *
from ColorfulWords import global_


class CustomFormatter(logging.Formatter):
    """
    A class used to modify the existing logging Formatter instance by adding colors to logger messages.

    Method
    ---
    format(levelname) -> object
    """

    def format(self, levelname) -> object:
        """
        Reformat the logging format to print each message in its respective color based on levelname.
        :param: name of level (e.g. DEBUG)
        :rtype: object
        """
        FORMATS = global_.updateFormats()
        logging_format = FORMATS[levelname.levelno]
        formatter = logging.Formatter(logging_format, style="{")
        return formatter.format(levelname)
