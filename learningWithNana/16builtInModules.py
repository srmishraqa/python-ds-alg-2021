"""
Python has built in modules which has variable and functions to do certain operations
we don't need to write functions for the same, we just need to import and make use of them
"""
# to work with Operating system python has os module
import os  # to work with OS
import logging  # to log errors

print(os.name)

logger = logging.getLogger("MAIN")
logger.error("Print a sample error message")
