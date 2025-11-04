import pandas 

#Create a CSV called squirrel_count.csv (logged under the "Primary Fur Color column")
#Called Fur Color, Count 

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

df_squirrels = data['Primary Fur Color'].value_counts().to_frame()

df_squirrels.to_csv('squirrel_count.csv')
