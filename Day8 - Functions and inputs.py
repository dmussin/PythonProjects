# def greet():
#     print("Hello darkness, my old friend")
#     print("I've come to talk with you again")
#     print("Because a vision softly creeping")
#
# greet()
#
# def greet_with_name(name):
#     print(f"Hello darkness, my old friend {name}")
#     print("I've come to talk with you again")
#     print("Because a vision softly creeping")
#
# greet_with_name("Dani")

#
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"Are you from {location}?")
#
# greet_with(name="Dani", location="KZ")


#Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height * width) / cover)
    print(f"You will need {number_of_cans} cans of paint.")


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)