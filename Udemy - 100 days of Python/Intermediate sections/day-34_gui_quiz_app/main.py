# This code implements a Quiz Game as part of the day 17 of the python course
# goal: get practice with oop and python syntax when defining custom classes

from data import questions_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizzInterface

# create question bank
question_bank = []
# for each question in the question_data list
for question in questions_data:
    # get references to the text and answer attributes for that question
    q_text = question['question']
    q_answer = question['correct_answer']
    # create an object from the class Question using the text and answer attributes
    new_question = Question(q_text, q_answer)
    # append this object to the question_bank list
    question_bank.append(new_question)

# create an object from the QuizBrain class using the question_bank list
quiz = QuizBrain(question_bank)
# create an object from the QuizInterface class passing the quiz object from the class QuizBrain 
quiz_ui = QuizzInterface(quiz)