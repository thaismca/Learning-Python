# code written as part of the day 9 of the course -> dictionares
# getting familiar with python syntax to work with dictionaries

# By the end of the program, you should have a new dictionary called student_grades
# This new dictionary should contain student names for keys and their grades for values

# starting code copied from the exercise available on codingrooms
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
# loop through the dictionary students_score
for student in student_scores:
    # 
    if student_scores[student] > 90:
        student_grades[student] = 'Outstanding'
    elif student_scores[student] > 80:
        student_grades[student] = 'Exceeds Expectations'
    elif student_scores[student] > 70:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'
    

# 🚨 Don't change the code below 👇
print(student_grades)