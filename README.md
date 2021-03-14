# Most Active Cookie
Here presents an application to find the most active cookies on a given date.

## Running locally
For running locally, for example
```bash
./dist/program -f ./cookie_log.csv -d 2018-12-09
```
where -f and -d denotes the input .csv file and query date respectively.

Or running the program Python file on Linux environment
```bash
./program.py ./cookie_log.csv -d 2018-12-09
```

## Running all tests case
This application uses pytest as the testing framework.

For running the tests, first of all to create a virtual enviroment and install the relevant packages
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
In running all test cases:
```bash
pytest
```
## Rebuild program
```bash
pyinstaller --onefile ./program.py
```
The executable program will be located in `./dist/`

## To deactivate the environment
```bash
deactivate
```