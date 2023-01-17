#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

import logzero
from logzero import logger
from datetime import date
from datetime import datetime


def main():
    """ Main entry point of the app """
    day = datetime.now().strftime("%Y%m%d_%H%M%S")
    logzero.logfile(f"./log/{day}.log")
    logger.info("hello world")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
