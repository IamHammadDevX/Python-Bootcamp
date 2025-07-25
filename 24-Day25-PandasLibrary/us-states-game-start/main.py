import turtle
import pandas


screen = turtle.Screen()
screen.title("US States Game")

img = "blank_states_img.gif"
screen.bgpic(img)  # This sets the background image

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)} / 50 correct State", prompt="What's other state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guess_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)



screen.mainloop()