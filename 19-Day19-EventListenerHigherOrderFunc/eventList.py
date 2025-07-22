from turtle import Turtle, Screen


tim = Turtle()
tim.shape("turtle")
tim.color("RoyalBlue")



def move_forward():
    tim.fd(10)



window = Screen()
window.listen()
window.onkey(key="space", fun=move_forward)
window.exitonclick()