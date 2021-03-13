import datetime
import pytest
from exceptions.customed_exception import FileTypeNotSupported, ParsingError
from parsers.csv_parser import CSVParser

class TestCSVParser():

    csv_parser = CSVParser()

    def test_csv_successful_parsing(self):
        log_file = './cookie_log.csv'

        expected_result = [{'cookie': 'AtY0laUfhglK3lC7','timestamp': '2018-12-09T14:19:00+00:00'},
                        {'cookie': 'SAZuXPGUrfbcn5UA', 'timestamp': '2018-12-09T10:13:00+00:00'},
                        {'cookie': '5UAVanZf6UtGyKVS', 'timestamp': '2018-12-09T07:25:00+00:00'},
                        {'cookie': 'AtY0laUfhglK3lC7', 'timestamp': '2018-12-09T06:19:00+00:00'},
                        {'cookie': 'SAZuXPGUrfbcn5UA', 'timestamp': '2018-12-08T22:03:00+00:00'},
                        {'cookie': '4sMM2LxV07bPJzwf', 'timestamp': '2018-12-08T21:30:00+00:00'},
                        {'cookie': 'fbcn5UAVanZf6UtG', 'timestamp': '2018-12-08T09:30:00+00:00'},
                        {'cookie': '4sMM2LxV07bPJzwf', 'timestamp': '2018-12-07T23:30:00+00:00'}]

        for result in expected_result:
            result['timestamp'] = datetime.datetime.fromisoformat(result['timestamp'])

        assert self.csv_parser.parse(log_file) == expected_result

    def test_csv_parser_with_invalid_fieldname(self):
        log_file = './tests/data/cookie_log_invalid_fields.csv'
        with pytest.raises(ParsingError):
            self.csv_parser.parse(log_file)

    def test_csv_parser_with_non_csv_file_type(self):
        log_file = './tests/data/cookie_log.txt'
        with pytest.raises(FileTypeNotSupported):
            self.csv_parser.parse(log_file)

    @pytest.mark.parametrize("log_file",
    ["./tests/data/cookie_log_invalid_fields.csv", "./tests/data/cookie_log_invalid_timestamp.csv"]
    )
    def test_csv_parser_with_invalid_fields_or_invalid_timestamp(self, log_file):
        with pytest.raises(ParsingError):
            self.csv_parser.parse(log_file)
