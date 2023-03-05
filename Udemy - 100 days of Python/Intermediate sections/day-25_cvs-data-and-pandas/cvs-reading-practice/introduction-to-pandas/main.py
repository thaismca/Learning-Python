PROJECT_DIRECTORY_PATH = "./Intermediate sections/day-25_cvs-data-and-pandas/cvs-reading-practice/introduction-to-pandas/"
WEATHER_FILE_PATH = "./Intermediate sections/day-25_cvs-data-and-pandas/cvs-reading-practice/introduction-to-pandas/weather_data.csv"

# using csv library
import csv

with open(WEATHER_FILE_PATH) as weather_data:
    data = csv.reader(weather_data)
    temperatures = []
    for row in data:
        try:
            temperatures.append(int(row[1]))
        except:
            pass

# print(temperatures)

# using pandas
import pandas

data = pandas.read_csv(WEATHER_FILE_PATH)
# getting data from the entire dataframe (table)
print(f'\nAccessing and printing the entire dataframe (table)\n{data}')
# getting data from series (column)
print(f'\nAccessing and printing series/column "temp"\n{data["temp"]}')
print(f'\nAccessing and printing average/mean of all temperatures\n{data["temp"].mean()}')
print(f'\nAccessing and printing the highest of all temperatures\n{data.temp.max()}')

# get all data in row
print(f'\nAccessing and printing the row where the highest of all temperatures is found\n{data[data["temp"] == data["temp"].max()]}')
print(f'\nAccessing and printing the row where the day is Monday\n{data[data.day == "Monday"]}')

# get one specific data in a row
print(f'\nAccessing and printing the temperature on Wednesday\n{data[data.day == "Wednesday"].temp}')

# create a dataframe from dictionary
data_dict = {
    "students": ["Amy", "Ben", "Carl"],
    "scores": [78, 75, 64]
}
dict_to_dataframe = pandas.DataFrame(data_dict)
print(f"\nThis is the dictionary\n{data_dict}")
print(f"\nThis is the dataframe from dictionary\n{dict_to_dataframe}")

# create csv file from dataframe
dict_to_dataframe.to_csv(PROJECT_DIRECTORY_PATH + "new_data.csv")