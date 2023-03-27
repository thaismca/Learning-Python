class QuizBrain:
    """Models the Quiz Brain"""
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        '''Prompts user with the next question'''
        # get reference to the question in the question list which index corresponds to question_number
        question = self.question_list[self.question_number]
        # increment question_number
        # this allows program to retrieve the questio from the next index the next time the function is called during program execution
        # it also corrects the number to be displayed for the current question
        self.question_number += 1
        # print question in the input request
        user_answer = input(f"Q.{self.question_number}: {question.text} (True / False?): ").lower()
        self.is_correct_answer(user_answer, question.answer)

    def still_has_questions(self):
        '''Returns True if there are still questions available in the quiz, and False if there aren't.'''
        return self.question_number < len(self.question_list)
    
    def is_correct_answer(self, user_answer, correct_answer):
        if correct_answer.lower() == user_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"Your current score is {self.score}/{self.question_number}\n")
