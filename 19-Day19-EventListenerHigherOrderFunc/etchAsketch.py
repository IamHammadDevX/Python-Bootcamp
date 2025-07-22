from turtle import Turtle, Screen


tim = Turtle()
tim.shape("classic")
tim.color("RoyalBlue")
tim.speed(0)


def move_forward():
    tim.fd(10)
def move_backward():
    tim.bk(10)
def turn_left():
    tim.left(10)
def turn_right():
    tim.right(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

window = Screen()
window.listen()
window.onkey(key="f", fun=move_forward)
window.onkey(key="b", fun=move_backward)
window.onkey(key="l", fun=turn_left)
window.onkey(key="r", fun=turn_right)
window.onkey(key="c", fun=clear)
window.exitonclick()