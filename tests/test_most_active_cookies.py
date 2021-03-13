import datetime
import pytest
from cookie_factory.cookie_factory import CookieFactory

def init_cookie_factory():
    log_data = [{'cookie': 'AtY0laUfhglK3lC7','timestamp': '2018-12-09T14:19:00+00:00'},
                {'cookie': 'SAZuXPGUrfbcn5UA', 'timestamp': '2018-12-09T10:13:00+00:00'},
                {'cookie': '5UAVanZf6UtGyKVS', 'timestamp': '2018-12-09T07:25:00+00:00'},
                {'cookie': 'AtY0laUfhglK3lC7', 'timestamp': '2018-12-09T06:19:00+00:00'},
                {'cookie': 'SAZuXPGUrfbcn5UA', 'timestamp': '2018-12-08T22:03:00+00:00'},
                {'cookie': '4sMM2LxV07bPJzwf', 'timestamp': '2018-12-08T21:30:00+00:00'},
                {'cookie': 'fbcn5UAVanZf6UtG', 'timestamp': '2018-12-08T09:30:00+00:00'},
                {'cookie': '4sMM2LxV07bPJzwf', 'timestamp': '2018-12-07T23:30:00+00:00'}]

    for log in log_data:
        log['timestamp'] = datetime.datetime.fromisoformat(log['timestamp'])

    return CookieFactory(log_data)

class TestCookieFactory():

    cookie_factor = init_cookie_factory()

    @pytest.mark.parametrize(
        'query_date, expected',
        [('2018-12-09', ['AtY0laUfhglK3lC7']),
         ('2018-12-08', ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG']),
         ('2018-12-07', ['4sMM2LxV07bPJzwf']),
         ('2021-03-17', [])
        ]
    )
    def test_daily_most_active_cookie(self, query_date, expected):
        query_date = datetime.datetime.strptime(query_date, '%Y-%m-%d').date()
        assert self.cookie_factor.get_daily_most_active_cookies(query_date) == expected
