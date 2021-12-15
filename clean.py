# Import all modules
import csv 
import pandas as pd

# Reading the file
df = pd.read_csv('total_stars.csv')
# Print
print(df.shape)

# Cleaning the data by removing unwanted columns
del df["Luminosity"]
del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]
del df["Unnamed: 0"]
del df["Unnamed: 6"]

# Print
print(df.shape)

# Rename some column names
df = df.rename({
    'Star_name.1': "Star_name",
    'Distance.1': "Distance",
    'Mass.1': "Mass",
    'Radius.1': "Radius"
    }, axis = 'columns')

# Create new csv file
df.to_csv('final.csv')