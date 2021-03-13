import pytest
from exceptions.customed_exception import InputError
from validation.input_validation import InputValidation

class TestInputValidation():

    @pytest.mark.parametrize("test_input_date", ["2018-12-33", "2018-01-99", "2018-12-9", "2018-2-09", "2018-12-09T14:19:00+00:00"])
    def test_invalid_input_date_format(self, test_input_date):
        with pytest.raises(InputError):
            InputValidation.validate_date(test_input_date)

    @pytest.mark.parametrize("test_input_date", ["2018-12-09", "2018-12-09", "2018-05-15", "2021-03-13", "1998-03-17"])
    def test_valid_input_date_format(self, test_input_date):
        input_date_format = '%Y-%m-%d'
        assert InputValidation.validate_date(test_input_date).strftime(input_date_format) == test_input_date

    @pytest.mark.parametrize("input_file", ["./cookie_log.csv", "./program.py"])
    def test_existing_input_file(self, input_file):
        assert InputValidation.validate_file_existence(input_file) == input_file

    @pytest.mark.parametrize("input_file", ["./hello_world.py", "./cookie_log.txt"])
    def test_non_existing_input_file(self, input_file):
        with pytest.raises(InputError):
            InputValidation.validate_file_existence(input_file)