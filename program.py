"""
    FILENAME: program.py
"""
from parsers.cli_parser import CLIParser
from parsers.csv_parser import CSVParser
from cookie_factory.CookieFactory import CookieFactory

def main():
    cli_parser = CLIParser()
    args = cli_parser.parse_args()
    
    if not args.file or not args.date:
        print('Missing argument for file or data')
        exit(1)
    
    csv_parser = CSVParser()
    cookie_log_data = csv_parser.read_from_csv(args.file)
    cookie_factory = CookieFactory(cookie_log_data)
    cookies = cookie_factory.get_daily_most_active_cookies(args.date)
    
    for cookie in cookies:
        print(cookie)
    

if __name__ == '__main__':
    main()
