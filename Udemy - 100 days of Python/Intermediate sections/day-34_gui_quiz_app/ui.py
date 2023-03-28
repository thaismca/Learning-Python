from tkinter import *

# --- STYLING CONSTANTS --- #
# backgrounds
BG_COLOR = "#375362"
CATEGORY_BG_COLOR = "#799982"
QUESTION_BG_COLOR = 'white'
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
    def __init__(self):
        # app window
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(background=BG_COLOR, padx=20, pady=20)

        # score label
        self.score_label = Label(text="Score: 0", bg=BG_COLOR, fg=SCORE_FONT_COLOR, font=SCORE_FONT)
        self.score_label.grid(row=0, column=1, sticky="E")

        # question canvas
        self.question_canvas = Canvas(width=350, height=360, highlightthickness=0, background=BG_COLOR)
        self.question_canvas.create_rectangle(0, 30, 350, 350, fill=QUESTION_BG_COLOR, outline=QUESTION_BG_COLOR)
        self.question_text = self.question_canvas.create_text(175, 190, text="Question goes here", width=300, font=QUESTION_FONT, fill=QUESTION_FONT_COLOR, justify='center')
        self.question_canvas.create_rectangle(30, 0, 320, 60, fill=CATEGORY_BG_COLOR, outline=CATEGORY_BG_COLOR)
        self.question_canvas.create_text(175, 15, text='CATEGORY', font=CATEGORY_LABEL_FONT, fill=CATEGORY_FONT_COLOR, justify='center')
        self.category_text = self.question_canvas.create_text(175, 38, text="Name of The Category", font=CATEGORY_NAME_FONT, fill=CATEGORY_FONT_COLOR, justify='center')
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=25)

        # true and false buttons
        true_bg = PhotoImage(file="./images/true.png")
        false_bg = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=true_bg, highlightthickness=0).grid(row=2, column=0)
        self.false_button = Button(image=false_bg, highlightthickness=0).grid(row=2,column=1)


        self.window.mainloop()

        
        

quiz = QuizzInterface()
