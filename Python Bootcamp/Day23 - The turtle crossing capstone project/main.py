from turtle import Screen
from scoreboard import Scoreboard
from player import Player
from car_manager import CarManager
import time
import random

# Game window setting
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('SlateGray')
screen.title('Turtle Crossing')
screen.tracer(0)

# Calling var from class
scoreboard = Scoreboard()
car_manager = CarManager()
player = Player()


# Turtle moving while pressing the key
screen.listen()
screen.onkey(player.up, 'Up')

game_is_on = True
while game_is_on:
    car_manager.create_car()
    car_manager.move_car()
    time.sleep(car_manager.car_speed)
    screen.update()

    #Detecting collision with car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    #Cross road
    if player.ycor() > 280:
        scoreboard.increase_score()
        player.reset_position()
        car_manager.new_lvl()

screen.exitonclick()
