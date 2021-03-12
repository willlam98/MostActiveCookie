import datetime

class CookieInfo():

    def __init__(self, cookie, timestamp):
        self.cookie = cookie
        self.timestamp = timestamp

class CookieFactory():

    def __init__(self, cookie_log_data):
        self.cookie_log_data = [CookieInfo(data['cookie'], data['timestamp']) for data in cookie_log_data]
        # print(self.cookie_log_data)

    def group_cookies_by_date(self, date):
        cookie_count_dict = {}
        query_date = datetime.datetime.fromisoformat(date).date()

        for log in self.cookie_log_data:
            log_date = datetime.datetime.fromisoformat(log.timestamp).date()
            if log_date > query_date:
                continue
            elif log_date < query_date:
                break
            cookie_count_dict[log.cookie] = cookie_count_dict.get(log.cookie, 0) + 1

        return cookie_count_dict

    def get_daily_most_active_cookies(self, date):
        cookies = []

        cookie_count_dict = self.group_cookies_by_date(date)

        cookie_count_dict = dict(sorted(cookie_count_dict.items(), key=lambda item: item[1], reverse=True))

        max_occurance = max(cookie_count_dict.values())

        for key, value in cookie_count_dict.items():
            if value == max_occurance:
                cookies.append(key)
            else:
                break
        return cookies
