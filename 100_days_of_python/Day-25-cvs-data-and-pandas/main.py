# import csv

# temp = []
# with open ("weather_data.csv", "r") as file:
#     weather_data = csv.reader(file)
#     for row in weather_data: 
#         if row [1] != 'temp':
#             temp.append(int(row[1]))

# print(temp)

import pandas

data = pandas.read_csv("weather_data.csv")
# average_temp = data.temp.mean()
# print(average_temp)

# print(data.temp.max())

#Get Data in the row 

# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.temp*9/5 +32)