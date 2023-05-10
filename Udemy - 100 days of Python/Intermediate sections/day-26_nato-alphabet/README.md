
# NATO ALPHABET CONVERTER

This project implements a program that converts words to the standardized phonetic alphabet used by the military and other organizations.

Goal of the project was to practice list and dictionary comprehension.

Implemented as part of the day 26 of the course *100 days of Python*. All implementation was taken care of prior to watch the solution videos.

## Key difference from course solution

Solution presented in the course does not account for the scenario where user types spaces or characters that are not letter

## How this app works

1. User is prompted to enter a word.

2. The program outputs a list of all the letters in the input converted to NATO phonetic alphabet.
## Implementation notes

Problem was broken down into the following TODOs:

- convert the nato_phonetic_alphabet.csv file to a dataframe
- convert the dataframe to a dictionary where each letter is a key and its corresponding code is the value
- receive string from user -> remove any spaces, because only characters will matter -> convert to uppercase
-  for each character, use the nato alphabeth dictionary to find the corresponding code -> append this code to a result list
- output the result list