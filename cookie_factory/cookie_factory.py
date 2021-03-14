"""
This module contains CookieFactory class which is responsible for
obtaining most active cookies on a specific day
"""

class CookieFactory():

    def __init__(self, cookie_log_data):
        self.cookie_log_data = cookie_log_data

    def get_daily_most_active_cookies(self, date):
        cookies = []

        cookie_count_dict = self.__group_cookies_by_date(date)
        max_occurance = max(cookie_count_dict.values(), default=0)

        for key, value in cookie_count_dict.items():
            if value == max_occurance:
                cookies.append(key)

        return cookies

    def __group_cookies_by_date(self, query_date):
        """
            This function uses binary search to aggregate cookies by date
            since the given input is sorted byb timestamp
        """
        cookie_count_dict = {}

        upper_bound = self.__binary_search_date_bound(self.cookie_log_data, query_date, upper_bound=True)

        if upper_bound == len(self.cookie_log_data) or not self.cookie_log_data[upper_bound]['timestamp'].date() == query_date:
            return cookie_count_dict
        
        lower_bound = self.__binary_search_date_bound(self.cookie_log_data, query_date, upper_bound=False)

        for log in self.cookie_log_data[upper_bound:lower_bound]:
            cookie_count_dict[log['cookie']] = cookie_count_dict.get(log['cookie'], 0) + 1

        return cookie_count_dict

    def __binary_search_date_bound(self, log_data, query_date, upper_bound):
        start = 0
        end = len(log_data)

        while start < end:
            mid = (start + end) // 2
            date_at_mid = log_data[mid]['timestamp'].date()
            if (upper_bound and query_date == date_at_mid) or date_at_mid < query_date:
                end = mid
            else:
                start = mid + 1

        return start