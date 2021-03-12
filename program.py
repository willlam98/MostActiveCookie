"""
    FILENAME: program.py
"""
from Parser.cli_parser import CLIParser
from Parser.csv_parser import CSVParser


if __name__ == '__main__':
    cli_parser = CLIParser()
    args = cli_parser.parse_args()
    
    if not args:
        print('Missing argument')
        exit()
    
    csv_parser = CSVParser(args.file)
