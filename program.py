#!/usr/bin/python3
"""
This is a command line program that outputs the most active cookies
regards to the input query date in a .csv file

usage: ./program.py [-h] [-f FILE] [-d DATE]

Find the most active cookies on a specific date from a .csv file.

optional arguments:
  -h, --help  show this help message and exit
  -f FILE     Target .csv file
  -d DATE     Specify date in YYYY-MM-DD format
"""

from parsers.cli_parser import CLIParser
from parsers.csv_parser import CSVParser
from validation.input_validation import InputValidation
from cookie_factory.cookie_factory import CookieFactory
from exceptions.customed_exception import ParsingError, FileTypeNotSupported, InputError

def main():
    cli_parser = CLIParser()
    args = cli_parser.parse()

    try:
        input_file = InputValidation.validate_file_existence(args.file)
        query_date = InputValidation.validate_date(args.date)

        csv_parser = CSVParser()
        cookie_log_data = csv_parser.parse(input_file)

        cookie_factory = CookieFactory(cookie_log_data)
        most_active_cookies = cookie_factory.get_daily_most_active_cookies(query_date)
        
        for cookie in most_active_cookies:
            print(cookie)

    except (FileTypeNotSupported, ParsingError, InputError) as e:
        print(e)

if __name__ == '__main__':
    main()
