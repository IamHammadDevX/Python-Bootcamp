from turtle import Turtle, Screen
import random


is_race_on = False
window = Screen()
window.setup(width=500, height=400)
user_bet = window.textinput(title="Make your bet", prompt="Which turtle win the race? Enter a color: ")
window.title("Welcome to the turtle Race!")

colors = ["red", "orange", "green", "blue", "yellow", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True



while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle win the race.")
            else:
                print(f"You've lost! The {winning_color} turtle win the race.")

        rand_dist = random.randint(0, 10)
        turtle.fd(rand_dist)

window.exitonclick()