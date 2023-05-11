# Quiz Game

This project implements a Quiz Game. It's a revamp of the Quiz Game implemented on day 17. Instead of running the program in the terminal and working with questions from a JSON file, this new version implements a GUI using Tkinter and works with questions randomly retrieved from the Open Trivia Database API each time the program is ran.

This game was implemented as part of the day 34 of the course 100 days of Python. All implementation was taken care of prior to watch the solution videos.

## Key difference from course solution

- Number of questions and difficulty level: in this implementation, player sees a pop up when the game is launched, where the number of questions and the difficulty level can be customized. In the solution, this pop-up does not exist. The number of questions is hard coded to 10, and the difficulty level is not set when making the request to the API, so it always runs with questions of all levels.

- Question category: in this implementation, the name of the category of each question is displayed. The course implementation doesn't display this information to the player.

- Disabling answer buttons: in this implementation, the buttons that record player's answers are disabled while the feedback is being provided and after the game is over. This avoid all the issues that can arrise from player spamming those buttons. This was not covered by the course solution.

## How it works

1 - When game starts, the player is prompted with a Start po-up where they are asked to set the number of question and the level of difficulty. All questions will be of "True or False" type.

The screenshot below demonstrate how the game start pop-up looks like:

![start game screenshot](https://github.com/thaismca/Python-Practices/blob/810c5ac6f4ffbab2b4c2dda0cfddf0ae89ff36e6/Udemy%20-%20100%20days%20of%20Python/Intermediate%20sections/day-34_gui_quiz_app/quiz_start.png?raw=true)

2 - After player confirms the settings for that game, the pop up is closed and the main window displays the first question.

3 - Player can click the _green_ button if they believe the correct answer fot the current question is "True", or the _red_ one if they think that the correct answer is "False".

4 - If player's guess is correct, the question card background will temporarily turn _green_. If the player guess is incorrect, the question card background will temporarily turn _red_. While this feedback is being provided, the answer button will be disabled. for each cirrect guess, the score will register one point to the player.

5 - After a couple seconds, the next question is displayed. The question card background will be neutral again, and the answer buttons will be enabled, so player can register the next guess.

The screenshot below demonstrates how the question and the respective right and wrong feedbacks look like:

![game states screenshots](https://github.com/thaismca/Python-Practices/blob/810c5ac6f4ffbab2b4c2dda0cfddf0ae89ff36e6/Udemy%20-%20100%20days%20of%20Python/Intermediate%20sections/day-34_gui_quiz_app/quiz_gameplay.png?raw=true)


6 - Steps 3, 4 and 5 are repeated until the game reaches the total number of questions that was set by the player in the starting pop-up.

7 - After all questions are answered, the screen displays a game over message.


## Implementation notes

The code for this project was divided into the folowing files:

### question_model.py
- It defines a class Question, which models a question that can be used in a quiz.
  - It receives a text, a category and a answer so the object can be contructed with these respective properties.

### data.py
- It defines a class QuizData, which models a list of questions that can be used to generate a QuizBrain.
  - It receives a *params* object, that is passed in the arguments to make a request to the Open Trivia API and store the request result to a property *quiz_data*.
  - The result in *quiz_data* is parsed into a json that is stored into a *question_data* property of the QuizData object.

- The ***generate_question()*** method is called so it can instantiate Question objects passing the _text_, _category_ and answer_ properties from each one of the items in *question_data*.
  - Each Question will be appended to a *question_bank* property, that will contain an array of questions that will be passed in the argument to instantiate a QuizBrain object.

### quiz_brain.py
- It defines a class QuizBrain, which models a quiz game brain.
  - It receives a list of Question objects.
  - It keeps track of the player's score.
  - It keeps track of the number of the current question.

- The ***next_question()*** method returns the next Question dictionary.
  - The question text is treated to display the question's number and all its html entities are unescaped.

- The ***still_has_questions()*** method returns *True* if there are still questions available in the quiz, and *False* if there aren't.

- The ***is_correct_answer(user_answer)*** receives a string containing the player's answer.
  - It returns *True* if the answer matches the current question correct answer, and *False* if it doesn't.

### ui.py
- It defines a class QuizInterface, which generates the window for the Quiz App and the starting settings pop up.

- The ***start_quiz()*** method is called when the player click the _Start_ button on the starting settings pop up.
  - It takes the settings from the pop up inputs for both number of questions and difficulty level and generates a _params_ object.
  - This object is passed in the arguments to instantiate a QuizData object, which will make a request to the Open Trivia API and store the request result to a property *question_bank*.
  - This *question_bank* property will contain an array of questions that will be passed in the argument to instantiate a QuizBrain object.
  - This method also generates all the Tkinter elements in the main window of the game, destroys the starting setting pop-up and calls method to generate the first question.

- The ***check_answer(user_answer: str)*** method receives a string that contains user answer.
  - It's called when player clicks either 'true' or 'false' button to answer to the current question, and passes the user answer to the QuizBrain to check if that's correct.
  - It also calls the method that gives feedback to the player passing the result of this check.

- The ***give_feedback(is_correct_answer: bool)*** method receives a boolean representing the result of the check for a correct answer. 
  - It gives feedback on the player's answer, by coloring the question card background with either green if player guessed it right, or red if player guessed it wrong.
  - It also updates the score label and calls the next question after one second.

- The ***generate_next_question()*** method uses the QuizBrain object that was instatiated at *start_quiz()* to get the next question and displays it in the canvas, if that are still questions left.

- The ***end_game()*** method changes the text elements in the canvas to display a game over message, and disables the answer buttons.

- The ***close_quiz()*** method only destroys the main window. It was defined only to be called when player clics to close the starting settings pop-up, so this action cascades to also close the main window.

### main.py

This is the file that must be executed in order to run the game. It instantiates a QuizzInterface object, which renders the window where the whole game will run.