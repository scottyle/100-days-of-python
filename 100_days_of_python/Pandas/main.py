import pandas as pd 

"""
This file will be used to go over the module pandas used for data analysis 
"""

#There are two core objects in pandas, Dataframe and series 
"""
A dataframe is a table, which contains an array of individual entries, each of which has a value and each entry corresponds to a row (record) and a column 

"""

print(pd.DataFrame({'Yes': [50,21], 'No': [131,2]}))

#Data frames are not limited to just integers they can consist of strings as well 

print(pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}))

print(

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

)

"""
You can create a new DF by passing a dict into pd.DataFrame() the keys of the dict are the column names like Bob and Sue above and the values are the lists of data
that go into those columns 

By default when you create a DF this way pandas automatically set the rows labels(called a index) to numbers starting from 0... etc 
This is fine but here is how you can name your columns by using the index= Paramater 

A series in contrast compared to a DF is a sequence of data values while a DF is a table a Series is a list 
"""

print(pd.Series([1,2,3,4,5]))

# A series is a single column of a DF, you can assign row labels to a series the same way using a index parameter, how series do not have column names

sales = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(sales)