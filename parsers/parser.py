"""
This module contains the base class of the (csv) parser
"""

from abc import abstractmethod
from exceptions.customed_exception import ParsingError

class Parser():

    FILE_TYPE_NOT_SUPPORTED_MESSAGE = 'File type not supported in parser, expecting {} format'

    def __init__(self, file_type):
        self.FILE_TYPE = file_type

    @abstractmethod
    def parse(self, file):
        raise ParsingError('No suitable parser available for {}'.format(file))

    def can_parse_file(self, file):
        return file.endswith(self.FILE_TYPE)
