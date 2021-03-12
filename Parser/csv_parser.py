import csv
import os
import datetime

class CSVParser():
    
    def __init__(self, file):
        self.time_to_cookies_dict = {}
        try:
            with open(file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                print(dict(reader))
        except FileNotFoundError as e:
            print('No such file or directory:', e)