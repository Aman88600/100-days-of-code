# file = open("weather_data.csv", "r")
# data = file.readlines()
# file.close()

# print(data)

import csv

temperatures = []
with open("weather_data.csv", "r") as file:
    data = csv.reader(file)
    # Now that we have the data we can now show it
    for row in data:
        if row[1] == 'temp':
            pass
        else:
            temperatures.append(int(row[1]))
print(temperatures)