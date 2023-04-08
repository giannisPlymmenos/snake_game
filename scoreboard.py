# Import module
from turtle import Turtle
from turtle import Screen


# Create class Scoreboard that inherits from the class Turtle.
class Scoreboard(Turtle):

    # Initialize the class Scoreboard.
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 265)
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=("arial", 24, "normal"))
        self.hideturtle()
        self.update_scoreboard()

    # Create increase_score method.
    def increase_score(self):
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("arial", 24, "normal"))
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode= "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("arial", 24, "normal"))
