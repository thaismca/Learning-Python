import html
from question_model import Question

class QuizBrain:
    """Models the Quiz Brain"""
    def __init__(self, question_list:list[Question]):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0


    def next_question(self) -> Question:
        '''Returns the next question dictionary to the user, where the question text is treated to display the question's number and
        all its html entities are unescaped.'''
        # get reference to the question in the question list which index corresponds to question_number
        self.current_question = self.question_list[self.question_number]
        # increment question_number
        # this allows program to retrieve the question from the next index the next time the function is called during program execution
        # it also corrects the number to be displayed for the current question
        self.question_number += 1
        # get the text from the current question and unescape it
        self.current_question.text = f'{self.question_number}: {html.unescape(self.current_question.text)}'
        
        return self.current_question



    def still_has_questions(self) -> bool:
        '''Returns True if there are still questions available in the quiz, and False if there aren't.'''
        return self.question_number < len(self.question_list)
    
    
    def is_correct_answer(self, user_answer) -> bool:
        '''Returns True if user answer matches the current question correct answer, and False if it doesn't.'''
        if  self.current_question.answer == user_answer:
            self.score += 1
            return True
        else:
            return False
