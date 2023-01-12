# from turtle import Turtle, Screen
#
# timmy = Turtle()
# screen = Screen()
#
# def move_forwards():
#     timmy.forward(10)
#
# def move_backwards():
#     timmy.backward(10)
#
# def move_right():
#     timmy.rt(10)
#
# def move_left():
#     timmy.lt(10)
#
# def clear_display():
#     timmy.penup()
#     timmy.clear()
#     timmy.home()
#     timmy.pendown()
#
# screen.listen()
# screen.onkey(key='w', fun=move_forwards)
# screen.onkey(key='s', fun=move_backwards)
# screen.onkey(key='d', fun=move_right)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key='c', fun=clear_display)
#
# screen.exitonclick()
import turtle
#Turtle RASE

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "SeaGreen", "SlateGray"]
y_position = [-150, -100, -50, 0, 50, 100]
all_turtles = []

print(user_bet)

for turtle_index in range(6):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.fillcolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lose. The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)

screen.exitonclick()