# file = open("weather_data.csv", "r")
# data = file.readlines()
# file.close()

# print(data)

# import csv

# temperatures = []
# with open("weather_data.csv", "r") as file:
#     data = csv.reader(file)
#     # Now that we have the data we can now show it
#     for row in data:
#         if row[1] == 'temp':
#             pass
#         else:
#             temperatures.append(int(row[1]))
# print(temperatures)

import pandas
data  = pandas.read_csv("weather_data.csv")
# print(data["temp"])
print(data.to_dict())

temp_list = data["temp"].to_list()

# TO find the avg temp
sum_temp = 0
for temp in temp_list:
    sum_temp += temp

average_temp = sum_temp / len(temp_list)
print(average_temp)