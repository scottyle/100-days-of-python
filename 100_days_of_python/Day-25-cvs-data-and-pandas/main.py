# data = []
# with open('weather_data.csv', 'r') as weather:
#     lines = weather.readlines()
#     for i in lines:
#         data.append(i)


# import csv 

# temp = []

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         if row[1] != 'temp':
#             temp.append(int(row[1]))
        
#     #Create a new list called temperatures that contains all the temp degrees 

# breakpoint()

import pandas
import statistics

# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))

# # average_temp = statistics.mean(data["temp"].to_list())
# # print(average_temp)

# average_temp = data["temp"].mean()
# print(average_temp)

# print(data["temp"].max())

#Get Data in Columns 
# print(data["condition"])
# #Note that the above statement we have to directly call the series, which could lead to errors, but pandas takes this into consideration and you can perform the one below
# print(data.condition)

#Get Data in Rows 
# print(data[data.day  == "Monday"])

#Pull out the data where the row of data is the maximum 

# print(data[data.temp == (data.temp.max())])

# monday = data[data.day == "Monday"]
# temp = monday.temp.convert_dtypes(convert_integer=True)
# degrees_in_f = temp * 9/5 + 32

#How to create a data from scratch 

# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

#Create a csv that contains the fur colour, count 

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_colours = (data["Primary Fur Color"].unique())

squirrel_dict = {
    "Fur Color": [],
    "Count": [], 
}

for fur in fur_colours:
    if pandas.notna(fur):
        squirrel_dict["Fur Color"].append(fur)
        fur_column = data[data["Primary Fur Color"] == fur]
        squirrel_dict["Count"].append(len(fur_column))

#Convert Dict to dataframes 
squirrel_data = pandas.DataFrame(squirrel_dict)
squirrel_data.to_csv("squirrel_count.csv")

def count_squirrels_by_fur_color(file_path): 
    """
    Count squirrels by their primary color and save results to csv
    
    Args:
        file_path: Path to Squirrel Data 
    """

    try: 
        #Read data 
        data = pandas.read_csv("squirrel_count.csv")

        #Use value_counts() to count occurences of each fur color 
        fur_counts = data["Primary Fur Color"].value_counts(dropna=True)

        #Conver to Dataframe for easy export 
        result = fur_counts.reset_index() 
        result.column = ["Fur Color", "Count"]

        #Save to CSV 
        result.to_csv("squirrel_count.csv")

        return result 
    
    except FileNotFoundError:
        print(f"Error: file {file_path} does not exist.")
    except Exception as e:
        print(f"An error has occurred {e}")
