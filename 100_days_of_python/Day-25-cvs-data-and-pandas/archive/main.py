#Open the weather_data csv and use readlines() to create a list named data thta contains the values from the csv file 
# import csv 
import pandas


#This grabs the file but its pretty painful to clean up the data and be able to extract each row etc... so what can we do?
# def get_weather_data():
#     data = []
#     with open("./weather_data.csv") as file:
#         for weather_data in file:
#             data.append(weather_data.strip())
#     print(data)

# get_weather_data()

# with open("./weather_data.csv") as data_file:
#     #This creates an object a csv.reader object 
#     data = csv.reader(data_file)
#     next(data)
#     #Create a new list called temperatures and this list is going to contain all of the temperatures inside weather_data
#     temperatures = []
#     for row in data:
#         temperatures.append(int(row[1]))
#     print(temperatures)

#This is pretty tedious to perform data analysis on a small excel file so we should use pandas instead for example
#We compare the above code to the below code 

data = pandas.read_csv("./weather_data.csv")

#One good thing to do when learning and building out new code is to do a type method check to see what data type we're
#working with 

# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()

# print(type(temp_list))

#Get the maximum value from the column of temperatures using the methods 

# highest_temp = data["temp"].max()
# print(highest_temp)

# #Get data in columns 
# print(data["condition"])
# #Another way of using this square bracket notion so that we do not have to be careful about the string 
# print(data.condition)

#Get a data in a row 
# print(data[data.day == "Monday"])

#Challenge pull out the row of data which had the highest temp in the week 

# max_temp = data.temp.max()
# print(data[data.temp == max_temp])
# print(data[data.day == "Monday"])

# monday = data[data.day == "Monday"]
# print(monday.temp)

#How to create a dataframe from scratch 
data_dict = {
    "students" : ["Amy", "James","Angela"],
    "scores": [76,56,65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

print(data)
