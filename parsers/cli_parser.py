"""
Module contains a command line parser with pre-defined input arguments
"""

import argparse

class CLIParser():

    def __init__(self):
        self.cli_parser = argparse.ArgumentParser(
            description='Find the most active cookies on a specific date from a .csv file.')
        self.cli_parser.add_argument('-f', dest='file', help='Target .csv file')
        self.cli_parser.add_argument('-d', dest='date', help='Specify date in YYYY-MM-DD format')

    def parse(self):
        args = self.cli_parser.parse_args()
        self.__check_args(args)

        return args

    def __check_args(self, args):
        if not args.file and not args.date:
            self.cli_parser.print_help()
            exit(1)
        elif not args.file:
            self.cli_parser.error('Expected one argument [-f FILE]')
        elif not args.date:
            self.cli_parser.error('Expected one argument [-d DATE]')        
