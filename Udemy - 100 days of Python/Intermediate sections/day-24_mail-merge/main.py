TEMPLATE_PATH = "./Intermediate sections/day-24_mail-merge/input/starting_letter.txt"
NAMES_LIST = "./Intermediate sections/day-24_mail-merge/input/invited_names.txt"
OUTPUT_PATH = "./Intermediate sections/day-24_mail-merge/output"

# TODO: create letter using starting_letter.txt
with open(TEMPLATE_PATH) as template:
    letter = template.read()

# TODO: for each name in invited_names.txt, replace [name] placeholder with the actual name
# Python File readlines() Method: return all lines in the file, as a list where each line is an item in the list object

# TODO: save letters in the output folder