# def my_function():
#     print("Holla")
#
#
#   my_function()
#
#
# while not at_goal():
#     print(front_is_clear())
#     print(wall_in_front())
#     print(at_goal())
#     if front_is_clear == True:
#       move()
#         if wall_in_front == True:
#             jump()
#         else:
#             move()
#     else:
#         jump()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

#MAZE
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

        if not wall_in_front() and wall_on_right():
            move()
        elif not wall_on_right() and wall_in_front():
            turn_right()
        elif wall_on_right() and wall_in_front():
            turn_left()
        elif not wall_in_front() and not wall_on_right():
            turn_right()
        else:
            move()
