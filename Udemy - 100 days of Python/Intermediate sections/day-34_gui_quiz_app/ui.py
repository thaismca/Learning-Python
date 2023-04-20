from tkinter import *
from quiz_brain import QuizBrain
from data import QuizData

# --- STYLING CONSTANTS --- #
# backgrounds
BG_COLOR = "#375362"
CATEGORY_BG_COLOR = "#799982"
QUESTION_BG_COLOR = 'white'
CORRECT_ANSWER_BG_COLOR = "#AFFFCF"
WRONG_ANSWER_BG_COLOR = "#FF8F8F"
START_POPUP_BG_COLOR = "#EEF5EB"
START_BUTTON_BG_COLOR = "#C5FCB1"
# fonts
FONT_NAME = 'Consolas'
SCORE_FONT = (FONT_NAME, 12, 'normal')
SCORE_FONT_COLOR = 'white'
CATEGORY_LABEL_FONT = (FONT_NAME, 9, 'bold')
CATEGORY_NAME_FONT = (FONT_NAME, 14, 'normal')
CATEGORY_FONT_COLOR = 'white'
QUESTION_FONT = (FONT_NAME, 18, 'normal')
QUESTION_FONT_COLOR = 'black'
START_POPUP_BIG_FONT = (FONT_NAME, 14, 'bold')
START_POPUP_SMALL_FONT = (FONT_NAME, 9, 'normal')

# settings values
MIN_QUESTIONS = 5
MAX_QUESTIONS = 30
DEFAULT_QUESTIONS = 10
DIFFICULTY_OPTIONS = ["easy", "medium", "hard"]


class QuizzInterface():
    def __init__(self):
        '''Generates the window for the Quiz App and displays the game settings pop up to.'''
        # app window
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(background=BG_COLOR, padx=20, pady=20)
        self.true_bg = PhotoImage(file="./images/true.png")
        self.false_bg = PhotoImage(file="./images/false.png")

        # start settings pop up
        self.start_popup = Toplevel(self.window)
        self.start_popup.attributes('-topmost',True)
        self.start_popup.focus_force()
        self.start_popup.protocol("WM_DELETE_WINDOW", self.close_quiz)
        self.start_popup.config(padx=20, pady=20, bg=START_POPUP_BG_COLOR)
        Label(self.start_popup, text='Welcome to the Quiz Game!', justify='center', pady='15px', font=START_POPUP_BIG_FONT, bg=START_POPUP_BG_COLOR).grid(row=0, column=0, columnspan=2)
        
        # number of questions
        Label(self.start_popup, text='Number of questions', pady='2px', padx='10px', font=START_POPUP_SMALL_FONT, bg=START_POPUP_BG_COLOR).grid(row=1, column=0)
        self.amount_select = IntVar()
        self.amount_select.set(DEFAULT_QUESTIONS)
        Spinbox(self.start_popup, textvariable= self.amount_select, width=10, from_=MIN_QUESTIONS, to=MAX_QUESTIONS).grid(row=2, column=0)
        
        # difficulty level
        Label(self.start_popup, text='Difficulty level', pady='2px', padx='10px', font=START_POPUP_SMALL_FONT, bg=START_POPUP_BG_COLOR).grid(row=1, column=1)
        self.difficulty_select = StringVar()
        self.difficulty_select.set(DIFFICULTY_OPTIONS[0])
        OptionMenu(self.start_popup, self.difficulty_select, *DIFFICULTY_OPTIONS).grid(row=2, column=1)
        
        # start button
        Label(self.start_popup, text='', pady='3px').grid(row=3, column=0)
        Button(self.start_popup, text='START', command= self.start_quiz, bg=START_BUTTON_BG_COLOR, font=START_POPUP_BIG_FONT, padx='15px', pady='3px').grid(row=4, column=0, columnspan=2)

        
        self.window.mainloop()


    
    def start_quiz(self):
        # get params
        amount = self.amount_select.get()
        difficulty = self.difficulty_select.get()
        params = {'amount': amount, 'difficulty': difficulty, 'type': 'boolean'}
        # get Quiz Data
        quiz_data = QuizData(params)
        # generate Quiz Brain
        self.quiz_brain = QuizBrain(quiz_data.question_bank)
        
        # question canvas
        self.question_canvas = Canvas(width=350, height=360, highlightthickness=0, background=BG_COLOR)
        self.question_bg = self.question_canvas.create_rectangle(0, 30, 350, 350, fill=QUESTION_BG_COLOR, outline=QUESTION_BG_COLOR)
        self.question_text = self.question_canvas.create_text(175, 190, text="", width=300, font=QUESTION_FONT, fill=QUESTION_FONT_COLOR, justify='center')
        self.question_canvas.create_rectangle(30, 0, 320, 60, fill=CATEGORY_BG_COLOR, outline=CATEGORY_BG_COLOR)
        self.category_label =self.question_canvas.create_text(175, 15, text='CATEGORY', font=CATEGORY_LABEL_FONT, fill=CATEGORY_FONT_COLOR, justify='center')
        self.category_text = self.question_canvas.create_text(175, 38, text="", width=300, font=CATEGORY_NAME_FONT, fill=CATEGORY_FONT_COLOR, justify='center')
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=25)

        # score label
        self.score_label = Label(text=f'Score: {self.quiz_brain.score}', bg=BG_COLOR, fg=SCORE_FONT_COLOR, font=SCORE_FONT)
        self.score_label.grid(row=0, column=1, sticky="E")

        # true and false buttons
        self.true_button = Button(image=self.true_bg, highlightthickness=0, command=lambda answer='True': self.check_answer(answer))
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=self.false_bg, highlightthickness=0, command=lambda answer='False': self.check_answer(answer))
        self.false_button.grid(row=2,column=1)

        self.start_popup.destroy()
        self.window.focus_force()
        self.generate_next_question()

    
    
    def check_answer(self, user_answer: str):
        '''Called when player clicks either 'true' or 'false' button to answer to the current question, and passes the user answer to the QuizBrain
        to check if that's correct. Calls the method that gives feedback to the player passing the result of this check.'''
        is_correct_answer = self.quiz_brain.is_correct_answer(user_answer)
        self.give_feedback(is_correct_answer)


    def give_feedback(self, is_correct_answer: bool):
        '''Gives feedbck on the player's answer, by coloring the question card background with either green if player guessed it right,
        or red if player guessed it wrong. It also updates the score label and calls the next question after one second.'''
        self.false_button.config(state='disabled')
        self.true_button.config(state='disabled')
        if is_correct_answer:
            self.question_canvas.itemconfig(self.question_bg, fill=CORRECT_ANSWER_BG_COLOR)
            self.score_label.config(text=f'Score: {self.quiz_brain.score}')
        else:
            self.question_canvas.itemconfig(self.question_bg, fill=WRONG_ANSWER_BG_COLOR)
        self.window.after(1000, self.generate_next_question)


    def generate_next_question(self):
        '''Uses the QuizBrain to get the next question and displays it in the canvas, if that are still questions left.'''
        self.question_canvas.itemconfig(self.question_bg, fill=QUESTION_BG_COLOR)
        if self.quiz_brain.still_has_questions():
            self.false_button.config(state='normal')
            self.true_button.config(state='normal')
            next_question = self.quiz_brain.next_question()
            self.question_canvas.itemconfig(self.category_text, text=next_question.category)
            self.question_canvas.itemconfig(self.question_text, text=next_question.text)
        else:
            self.end_game()

    
    def end_game(self):
        self.question_canvas.itemconfig(self.question_text, text="You completed the quiz!")
        self.question_canvas.itemconfig(self.category_text, text='')
        self.false_button.config(state='disabled')
        self.true_button.config(state='disabled')

    
    def close_quiz(self):
        self.window.destroy()