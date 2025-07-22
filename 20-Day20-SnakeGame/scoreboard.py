from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
    
    def game_end(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGN, font=FONT)

    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
