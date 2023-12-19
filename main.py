import turtle
import pandas as pd

screen = turtle.Screen()
correct_guesses_count = 0
screen.title("Name the States")
image = 'blank_states_img.gif'
screen.addshape(image)


turtle.shape(image)
states = pd.read_csv('50_states.csv')
list_correct_guesses = []
drawing_turtle = turtle.Turtle()
drawing_turtle.hideturtle()
drawing_turtle.speed(50)

while correct_guesses_count != 50:
    answer_state = screen.textinput(title=f'{correct_guesses_count}/50 States Correct', prompt="What's another state's name?")
    answer_state = answer_state.title()
    is_value_in_column = answer_state in states['state'].values
    if answer_state == 'Exit':
        break
    if is_value_in_column and answer_state not in list_correct_guesses:
        correct_guesses_count += 1
        list_correct_guesses.append(answer_state)
        x_coor = (states[states['state'] == answer_state].x).tolist()
        y_coor = (states[states['state'] == answer_state].y).tolist()
        x_coor = x_coor[0]
        y_coor = y_coor[0]
        drawing_turtle.penup()
        drawing_turtle.goto(x_coor, y_coor)
        drawing_turtle.write(answer_state, align="center", font=("Arial", 12, "normal"))
        drawing_turtle.pendown()


states_missing = states[~states['state'].isin(list_correct_guesses)]
states_missing.to_csv("states_to_learn.csv")
screen.exitonclick()

