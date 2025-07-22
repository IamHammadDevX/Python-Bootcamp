from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        with open("data.txt") as data:
            self.highScore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highScore}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.highScore}")
        self.score = 0
        self.update_scoreboard()

    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
