#  Introducton to pandas 


#  Install pandas 
import pandas as pd

# For reading file in pandas use .read_fileformat
df = pd.read_csv(r'C:\Users\smit\Downloads\shopping_trends.csv')

#  For returning rows by default it is returning 5 rows if not write number

print(df.head())

#  For checking number of rows and column of dataset
df.shape

# Just want to see number of rows

print(df.shape[0])

# Just want to see number of columns

print(df.shape[1])

#  For get the name of all columns

print(df.columns)

for i in df.columns:
    print(i)

# for type of data in pandas 

type(df)

#  For particular column datatype

df.info