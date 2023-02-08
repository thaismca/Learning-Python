# a program that generates a band name by concatenating two strings provided by the user
# getting familiar with python syntax

#1. Create a greeting for your program.
print('Welcome to the Band Name Generator!')
#2. Ask the user for the city that they grew up in.
city = input('Which city did you grow up in?\n')
#3. Ask the user for the name of a pet.
pet = input('What is your pet name?\n')
#4. Combine the name of their city and pet and show them their band name.
band = city + " " + pet
print('The name of your band could be ' + band)