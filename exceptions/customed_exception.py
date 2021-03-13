"""
    This module contains different types of customed exceptions
"""

class InputError(Exception):
    """Raise any exception with invalid input"""
    pass

class ParsingError(Exception):
    """Raise any exception in parser"""
    pass

class FileTypeNotSupported(Exception):
    """Raise an exception when a file type is not supported"""
    pass