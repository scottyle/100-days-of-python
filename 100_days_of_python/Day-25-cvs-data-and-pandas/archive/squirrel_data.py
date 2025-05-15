#Goal is to create a csv called squirrel_count that has a small table which contains the fur color logged under the primary fur color 
#Going to figure out how many gray squirrels in total, black ones, cinnamon ones etc. 

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#Grabs the fur color and the count of each fur 
fur_colors = (data["Primary Fur Color"].value_counts())
squirrel_data = pandas.DataFrame(fur_colors)
squirrel_data.to_csv("squirrel_count.csv")
print(squirrel_data)