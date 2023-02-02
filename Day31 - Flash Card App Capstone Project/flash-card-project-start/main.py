from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict = {}

# Read data from csv using pandas
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/czech_words.csv')
    data_dict = data.to_dict(orient='records')
else:
    data_dict = data.to_dict(orient='records')


# Random word into the flashcard
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(title, text=f"Czech", fill="black")
    canvas.itemconfig(card_text, text=current_card["Czech"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")

def is_known():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()

# UI SETUP
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# 3 second delay
flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=card_front_img)


# Text
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
card_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"), fill="black")

canvas.grid(column=0, row=0, columnspan=2)

# Buttons
correct_button = Button(image=right_img, highlightthickness=0,
                        highlightbackground=BACKGROUND_COLOR, command=is_known)
correct_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_img, highlightthickness=0,
                      highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()

