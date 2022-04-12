import logging


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
        logging_format = FORMATS[levelname.levelno]
        formatter = logging.Formatter(logging_format, style="{")
        return formatter.format(levelname)


# Logging message formats
FMT = "[{levelname}]: {message}"  # Logging message format
# Level name colors
FORMATS = {
    logging.DEBUG: f"\33[37m{FMT}\33[0m",  # Gray
    logging.INFO: f"\33[32m{FMT}\33[0m",  # Green
    logging.WARNING: f"\33[33m{FMT}\33[0m",  # Yellow
    logging.CRITICAL: f"\33[31m{FMT}\33[0m",  # Red
    logging.ERROR: f"\33[31m{FMT}\33[0m",  # Red
}

# Logging Configuration
handler = logging.StreamHandler()
handler.setFormatter(CustomFormatter())
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[handler]
)
