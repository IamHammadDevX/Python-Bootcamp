import turtle as turtle_module
import random

tim = turtle_module.Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()
turtle_module.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


tim.setheading(225)
tim.fd(300)
tim.setheading(0)
num_of_dots = 101

for dot_count in range(1, num_of_dots):
    tim.dot(20, random_color())
    tim.fd(50)
    if dot_count % 10 == 0:    
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)



















turtle_module.Screen().exitonclick()