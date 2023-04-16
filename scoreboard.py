from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")

######################## Using inheritance made Scoreboard on the screen ######################################


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            content = data.read()
            self.high_score = int(content)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

################################# Saved the high score in a seperate text file ################################

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()

    def increase(self):
        self.score += 1
        self.update()

