"""
This module contains CookieFactory class which is responsible for
obtaining most active cookies on a specific day
"""

class CookieFactory():

    def __init__(self, cookie_log_data):
        self.cookie_log_data = cookie_log_data

    def __group_cookies_by_date(self, query_date):
        cookie_count_dict = {}

        for log in self.cookie_log_data:
            log_cookie = log['cookie']
            log_date = log['timestamp'].date()

            if log_date > query_date:
                continue
            elif log_date < query_date:
                break

            cookie_count_dict[log_cookie] = cookie_count_dict.get(log_cookie, 0) + 1

        return cookie_count_dict

    def get_daily_most_active_cookies(self, date):
        cookies = []

        cookie_count_dict = self.__group_cookies_by_date(date)
        max_occurance = max(cookie_count_dict.values(), default=0)

        for key, value in cookie_count_dict.items():
            if value == max_occurance:
                cookies.append(key)

        return cookies
