"""
This modules contains static utility functions to validate user input 
"""

import os
import datetime
from exceptions.customed_exception import InputError

class InputValidation():

    INVALID_INPUT_DATE_MESSAGE = 'Invalid input date format, expecting YYYY-MM-DD'
    INVALID_INPUT_FILE_EXTENSION_MESSAGE = 'Invalid file cookie log file format, expecting .csv file'
    INVALID_INPUT_FILE_PATH_MESSAGE = 'File or directory do not exist'

    @staticmethod    
    def validate_date(date):
        try:
            return datetime.datetime.fromisoformat(date).date()
        except ValueError as value_error:
            raise InputError(InputValidation.INVALID_INPUT_DATE_MESSAGE) from value_error

    @staticmethod
    def validate_file_existence(filename):
        if not os.path.exists(filename):
            raise InputError(InputValidation.INVALID_INPUT_FILE_PATH_MESSAGE)

        return filename
