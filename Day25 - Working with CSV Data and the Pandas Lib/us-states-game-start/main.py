import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=730, height=500)
screen.title("U.S. States Game")

# Adding image as a turtle shape(BG)
image = "blank_states_img.gif"
turtle.addshape(image)

turtle.shape(image)

# Guessed states for while loop
guessed_states = []

# Open a csv file via pandas
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
print(all_states)



while len(guessed_states) < 50:
    # Prompt to ask a state from user
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states guessed", prompt="What's another state's name").title()

    if answer_state == "Exit":

        missing_states = [state for state in all_states if state not in guessed_states]

        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # print(missing_states)

        df = pandas.DataFrame(missing_states)
        df.to_csv('missing_states.csv')
        break
    # #Checking if the guess in the list
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    else:
        print("Nah")
