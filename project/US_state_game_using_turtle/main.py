# import turtle
import turtle
from turtle import Turtle
import pandas as pd

screen = turtle.Screen()
turtle = turtle.Turtle()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
t = Turtle()
t.hideturtle()

guessed_states = []
data = pd.read_csv("50_states.csv")

# # Alternative way to find the value in specific row and their column values
# data = data[data['state'] == 'Ohio']
# state_x = data['x'].values[0]      # gets value in relevant column
# state_y = data['y'].values[0]      # gets value in relevant column

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # missed_states = []
        # states_dict = {"missed_stated": missed_states}
        # for m_s in data['state']:
        #     if m_s not in guessed_states:
        #         missed_states.append(m_s)
        missing_states = [m_s for m_s in data['state'] if m_s not in guessed_states]
        missed_states_data = pd.DataFrame(missing_states)
        missed_states_data.to_csv("missed_states_data.csv")
        break
    for s in data['state']:
        if s == answer_state:
            guessed_states.append(answer_state)
            state_data = data[data['state'] == answer_state]
            state_x = state_data.x
            state_y = state_data.y
            # state_x = state_data['x'].values[0]      # gets value in relevant column
            # state_y = state_data['y'].values[0]      # gets value in relevant column
            t.hideturtle()
            t.penup()
            t.goto(int(state_x), int(state_y))
            t.write(f"{answer_state}", align="center", font=('Arial', 8, 'normal'))
            # t.write(state_data.state.item()) # Alternative option to above line to pick the state name using panda

# List of state that's not identified by user


