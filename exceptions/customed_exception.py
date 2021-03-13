"""
    This module contains different types of customed exceptions
"""

class CSVFormatError(Exception):
    """Raise for invalid log-file headers and invalid dates format"""
    pass

class InputError(Exception):
    """Raise any exception with invalid input"""
    pass

class ParsingError(Exception):
    """Raise any exception in parser"""
    pass
