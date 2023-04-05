from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        # self.canvas.grid(column=0, row=1, columnspan=2)

        # Button images
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        # Text
        self.quiz_text = self.canvas.create_text(150, 125, text="Some Question Text", font=("Arial", 20, "italic"),
                                                 fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons
        self.true_button = Button(image=true_img,highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        # Label
        self.score_label = Label(text=f"Score: 0", font=("Arial", 20, "bold"),
                                 highlightthickness=0, highlightbackground=THEME_COLOR,
                                 highlightcolor=THEME_COLOR, fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz")
            self.canvas.config(bg="yellow")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


