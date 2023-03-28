from tkinter import *
from quiz_brain import QuizBrain

# --- STYLING CONSTANTS --- #
# backgrounds
BG_COLOR = "#375362"
CATEGORY_BG_COLOR = "#799982"
QUESTION_BG_COLOR = 'white'
CORRECT_ANSWER_BG_COLOR = "#AFFFCF"
WRONG_ANSWER_BG_COLOR = "#FF8F8F"
# fonts
FONT_NAME = 'Consolas'
SCORE_FONT = (FONT_NAME, 12, 'normal')
SCORE_FONT_COLOR = 'white'
CATEGORY_LABEL_FONT = (FONT_NAME, 9, 'bold')
CATEGORY_NAME_FONT = (FONT_NAME, 14, 'normal')
CATEGORY_FONT_COLOR = 'white'
QUESTION_FONT = (FONT_NAME, 18, 'normal')
QUESTION_FONT_COLOR = 'black'


class QuizzInterface():
    def __init__(self, quiz_brain: QuizBrain):
        '''Generates the user interface for the Quiz App. Receives a QuizBrain object.'''
        # QuizBrain object
        self.quiz = quiz_brain

        # app window
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(background=BG_COLOR, padx=20, pady=20)

        # score label
        self.score_label = Label(text=f'Score: {self.quiz.score}', bg=BG_COLOR, fg=SCORE_FONT_COLOR, font=SCORE_FONT)
        self.score_label.grid(row=0, column=1, sticky="E")

        # question canvas
        self.question_canvas = Canvas(width=350, height=360, highlightthickness=0, background=BG_COLOR)
        self.question_bg = self.question_canvas.create_rectangle(0, 30, 350, 350, fill=QUESTION_BG_COLOR, outline=QUESTION_BG_COLOR)
        self.question_text = self.question_canvas.create_text(175, 190, text="Question goes here", width=300, font=QUESTION_FONT, fill=QUESTION_FONT_COLOR, justify='center')
        self.question_canvas.create_rectangle(30, 0, 320, 60, fill=CATEGORY_BG_COLOR, outline=CATEGORY_BG_COLOR)
        self.question_canvas.create_text(175, 15, text='CATEGORY', font=CATEGORY_LABEL_FONT, fill=CATEGORY_FONT_COLOR, justify='center')
        self.category_text = self.question_canvas.create_text(175, 38, text="Name of The Category", font=CATEGORY_NAME_FONT, fill=CATEGORY_FONT_COLOR, justify='center')
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=25)

        # true and false buttons
        true_bg = PhotoImage(file="./images/true.png")
        false_bg = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=true_bg, highlightthickness=0, command=lambda answer='True': self.answer_question(answer))
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_bg, highlightthickness=0, command=lambda answer='False': self.answer_question(answer))
        self.false_button.grid(row=2,column=1)

        self.generate_next_question()
        self.window.mainloop()


    def answer_question(self, user_answer: str):
        '''Called when player clicks either 'true' or 'false' button to answer to the current question, and passes the user answer to the QuizBrain
        to check if that's correct. Calls the method that gives feedback to the player passing the result of this check.'''
        is_correct_answer = self.quiz.is_correct_answer(user_answer)
        self.give_feedback(is_correct_answer)


    def give_feedback(self, is_correct_answer: bool):
        '''Gives feedbck on the player's answer, by coloring the question card background with either green if player guessed it right,
        or red if player guessed it wrong. It also updates the score label and calls the next question after one second.'''
        if is_correct_answer:
            self.question_canvas.itemconfig(self.question_bg, fill=CORRECT_ANSWER_BG_COLOR)
            self.score_label.config(text=f'Score: {self.quiz.score}')
        else:
            self.question_canvas.itemconfig(self.question_bg, fill=WRONG_ANSWER_BG_COLOR)
        self.window.after(1000, self.generate_next_question)


    def generate_next_question(self):
        '''Uses the QuizBrain to get the next question and displays it in the canvas, if that are still questions left.'''
        self.question_canvas.itemconfig(self.question_bg, fill=QUESTION_BG_COLOR)
        if self.quiz.still_has_questions():
            next_question = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=next_question)
        else:
            self.question_canvas.itemconfig(self.question_text, text='You completed the quiz!') 