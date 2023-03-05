# using data from 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv
# generate a csv file containing a small table containing the primary fur colors and the squirrels count for each color
CENSUS_FILE_PATH = "./Intermediate sections/day-25_cvs-data-and-pandas/cvs-reading-practice/squirrel-census-data-analysis/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
PROJECT_DIRECTORY_PATH = "./Intermediate sections/day-25_cvs-data-and-pandas/cvs-reading-practice/squirrel-census-data-analysis/"
import pandas

data = pandas.read_csv(CENSUS_FILE_PATH)

# list of all black squirrels
black_squirrels = data[data["Primary Fur Color"] == "Black"]
# list of all cinnamon squirrels
cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
# list of all gray squirrels
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]

# create dictionary with squirrels colors and respective counts
squirrel_colors_dict = {
    "colors": ["Black", "Cinnamon", "Gray"],
    "count": [len(black_squirrels), len(cinnamon_squirrels), len(gray_squirrels)]
}

# create dataframe from dictionary
dict_to_dataframe = pandas.DataFrame(squirrel_colors_dict)
# create csv from dataframe
dict_to_dataframe.to_csv(PROJECT_DIRECTORY_PATH + "new_data.csv")