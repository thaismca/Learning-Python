import requests
from question_model import Question


class QuizData:
    def __init__(self, params):
        self.params = params
        self.quiz_data = requests.get(url="https://opentdb.com/api.php", params=self.params)
        self.question_data = self.quiz_data.json()["results"]
        
        self.generate_questions()


    def generate_questions(self):
        self.question_bank = []
        for question in self.question_data:
            question_text = question["question"]
            question_category = question["category"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_category, question_answer)
            self.question_bank.append(new_question)

