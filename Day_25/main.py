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

# data  = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# print(data.to_dict())

# temp_list = data["temp"].to_list()

# TO find the avg temp
# 1st way
# sum_temp = 0
# for temp in temp_list:
#     sum_temp += temp

# average_temp = sum_temp / len(temp_list)
# print(average_temp)

# 2 nd way
# print(data["temp"].max())


# print(data[data.temp == data["temp"].max()])
# monday = data[data.day == "Monday"]
# print((monday.temp * (9/5)) + 32)

# names = {"students" : ["Aman", "Nikhil"]}
# data = pandas.DataFrame(names)
# data.to_csv("names.csv")

import pandas
data = pandas.read_csv("Squirrel_Data.csv")
fur_color = data[data["Primary Fur Color"] == "Gray"]
fur_color_count = {"fur" : ["grey", "red", "black"], "count" : [len(data[data["Primary Fur Color"] == "Gray"]), len(data[data["Primary Fur Color"] == "Cinnamon"]), len(data[data["Primary Fur Color"] == "Black"])]}
data = pandas.DataFrame(fur_color_count)
data.to_csv("fur_data.csv")