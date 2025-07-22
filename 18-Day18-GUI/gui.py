from turtle import Turtle, Screen
import turtle as turtle_module
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("green")

# for _ in range(4):
#     timmy_the_turtle.fd(200)
#     timmy_the_turtle.right(90)


# for _ in range(15):
#     timmy_the_turtle.fd(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.fd(10)
#     timmy_the_turtle.pendown()


colors = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "Violet", "DeepSkyBlue", "wheat", "SeaGreen", "SlateGrey"]


# def draw_shape(num_of_sides):
#     angle = 360 / num_of_sides
#     for _ in range(num_of_sides):
#         timmy_the_turtle.fd(100)
#         timmy_the_turtle.right(angle)



# for num_of_shapes in range(3, 11):
#     timmy_the_turtle.color(random.choice(colors))
#     draw_shape(num_of_shapes)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

timmy_the_turtle.pensize(15)
turtle_module.colormode(255)
timmy_the_turtle.speed(0)
directions = [0, 90, 180, 270] 
for _ in range(200):
    timmy_the_turtle.color(random_color())
    # timmy_the_turtle.color(random.choice(colors))
    timmy_the_turtle.fd(30)
    timmy_the_turtle.setheading(random.choice(directions))

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         timmy_the_turtle.color(random.choice(colors))
#         timmy_the_turtle.circle(100)
#         timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)

# draw_spirograph(2)





Screen().exitonclick()