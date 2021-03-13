"""
Module contains a simple pre-defined fields csv parser
with row validation on timestamp supported
"""

import csv
import datetime
from exceptions.customed_exception import FileTypeNotSupported, ParsingError
from parsers.parser import Parser

class CSVParser(Parser):

    LOG_FILE_FIELD_NAMES = ['cookie', 'timestamp']
    TIMESTAMP_FORMAT = 'YYYY-MM-DDTHH:MM:SS+HH:MM'

    def __init__(self):
        super().__init__(file_type='.csv')

    def parse(self, file):
        if not self.can_parse_file(file):
            raise FileTypeNotSupported(Parser.FILE_TYPE_NOT_SUPPORTED_MESSAGE.format(self.FILE_TYPE))

        log_data = []

        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            self.__validate_fieldnames(reader.fieldnames)

            for row_number, row in enumerate(reader, start=1):
                validated_row = self.__validate_row(row, row_number)
                log_data.append(validated_row)

        return log_data

    def __validate_row(self, row, row_number):
        timestamp = row['timestamp']

        try:
            row['timestamp'] = datetime.datetime.fromisoformat(timestamp)
            return row
        except ValueError as value_error:
            raise ParsingError('Invalid timestamp found {} in row #{}, expecting {}'
                    .format(timestamp, row_number, self.TIMESTAMP_FORMAT)) from value_error

    def __validate_fieldnames(self, fieldnames):
        if not fieldnames == self.LOG_FILE_FIELD_NAMES:
            raise ParsingError("Invalid log file header, expecting '{}'"
                    .format(','.join(self.LOG_FILE_FIELD_NAMES)))
