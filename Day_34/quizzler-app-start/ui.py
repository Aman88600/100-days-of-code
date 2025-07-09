from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain
from time import sleep

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Making a question counter(When this 10 we exit out of GUI)
        self.question_number:int = 0
        # Making a score
        self.score_count:int = 0
        
        # Makinf the score label
        self.score = Label(self.window, text=f"Score : {self.score_count}", bg=THEME_COLOR)
        self.score.grid(row=0, column=0)
        # Making the white canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        # Creating text on canvas
        self.question_text = self.canvas.create_text(150, 125,width=200, text="Hello, World!", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Creating Buttons
        cross = PhotoImage(file = "images/false.png")
        self.cross_button = Button(self.window, image=cross, padx=0, highlightthickness=0, command=self.cross_button_function)
        self.cross_button.grid(row=2, column=0)

        tick = PhotoImage(file = "images/true.png")
        self.tick_button = Button(self.window, image=tick, padx=0, highlightthickness=0, command=self.tick_button_function)
        self.tick_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.window['bg'] = THEME_COLOR
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You Have reached the end of the Quiz!")
            self.cross_button.config(state="disabled")
            self.tick_button.config(state="disabled")

    # Cross Button Function
    def cross_button_function(self):
        if self.quiz.check_answer("False"):
            self.window['bg'] = 'green'
            self.score_count += 1
            self.score.config(text=f"Score : {self.score_count}")
        else:
            self.window['bg'] = 'red'
        self.window.after(1000,self.get_next_question)
    # Tick Button Function
    def tick_button_function(self):
        if self.quiz.check_answer("True"):
            self.window['bg'] = 'green'
            self.score_count += 1
            self.score.config(text=f"Score : {self.score_count}")
        else:
            self.window['bg'] = 'red'
        self.window.after(1000,self.get_next_question)