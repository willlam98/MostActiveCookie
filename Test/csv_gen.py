import os
import csv
import datetime

# data_list1 = [["cookie", "timestamp"],
#             ["AtY0laUfhglK3lC7","2018-12-09T14:19:00+00:00"],
#             ["SAZuXPGUrfbcn5UA","2018-12-09T10:13:00+00:00"],
#             ["5UAVanZf6UtGyKVS","2018-12-09T07:25:00+00:00"],
#             ["AtY0laUfhglK3lC7","2018-12-09T06:19:00+00:00"],
#             ["SAZuXPGUrfbcn5UA","2018-12-08T22:03:00+00:00"],
#             ["4sMM2LxV07bPJzwf","2018-12-08T21:30:00+00:00"],
#             ["fbcn5UAVanZf6UtG","2018-12-08T09:30:00+00:00"],
#             ["4sMM2LxV07bPJzwf","2018-12-07T23:30:00+00:00"]]

# with open('cookie_log_file1.csv', 'w', newline='') as file:
#     writer = csv.writer(file, delimiter=',')
#     writer.writerows(data_list1)

date = datetime.datetime.fromisoformat("2011-13- 02")
print(type(date), date)