import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")

timmy.color("red")

#Square Drawing
# for _ in range(4):
#     timmy.fd(100)
#     timmy.rt(90)
#

# Dash Lines Drawing
# for _ in range(20):
#     timmy.pendown()
#     timmy.fd(10)
#     timmy.penup()
#     timmy.fd(10)

#Different Shapes Drawing

# angle = 3
#
# turtle.colormode(255)
#
# while angle <= 10:
#     color1 = random.randint(0, 255)
#     color2 = random.randint(0, 255)
#     color3 = random.randint(0, 255)
#     for item in range(angle):
#         timmy.fd(100)
#         timmy.rt(360 / angle)
#     angle += 1
#     timmy.color(color1, color2, color3)
#
#
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "wheat", "SlateGray", "SeaGreen"]
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.fd(100)
#         timmy.rt(angle)
#
# for shape_side_n in range(3, 11):
#     timmy.color(random.choice(colours))
#     draw_shape(shape_side_n)
#

#Generate a Random Walk



# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "wheat", "SlateGray", "SeaGreen"]

# angles = [0, 90, 180, 270]
#
#
# def random_walk():
#     timmy.shape('arrow')
#     timmy.fd(20)
#     timmy.setheading(random.choice(angles))
#     timmy.pensize(15)
#     timmy.speed(8)
#
# for _ in range (200):
#     timmy.color(random.choice(colours))
#     random_walk()



#Random RGB Colors

# angles = [0, 90, 180, 270]
# turtle.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb = (r, g, b)
#     return rgb
#
# def random_walk():
#     timmy.shape('arrow')
#     timmy.fd(20)
#     timmy.setheading(random.choice(angles))
#     timmy.pensize(15)
#     timmy.speed(8)
#
# for _ in range (200):
#     timmy.color(random_color())
#     random_walk()



#Drawing a Spirograph
#
# turtle.colormode(255)
# timmy.speed('fastest')
# timmy.pensize(3)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb = (r, g, b)
#     return rgb
#
# def draw_spirograaph(size_of_gap):
#     for angle in range(int(360 / size_of_gap)):
#         timmy.color(random_color())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + size_of_gap)
#
# draw_spirograaph(3)
#
#
#






#Daring a paint







screen = Screen()
screen.exitonclick()

