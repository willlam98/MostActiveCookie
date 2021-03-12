import csv

class CSVParser():
    
    def __init__(self):
        self.time_to_cookies_access_dict = {}

    def read_from_csv(self, file):
        try:
            with open(file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                return [row for row in reader]
        except FileNotFoundError as e:
            print('No such file or directory:', e)
            exit(1)