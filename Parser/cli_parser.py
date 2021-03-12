"""
    FILENAME
"""
import argparse


class CLIParser():

    def __init__(self):
        self.cli_parser = argparse.ArgumentParser(
            description='Find the most active cookie from input .csv file.')
        self.cli_parser.add_argument('-f', dest='file', help='Input .csv file name')
        self.cli_parser.add_argument('-d', dest='date', help='Specify date in YYYY-MM-DD format')

    def parse_args(self):
        args = self.cli_parser.parse_args()

        if not args.file or not args.date:
            return None

        return args
