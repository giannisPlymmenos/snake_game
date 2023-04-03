
# Import module
from turtle import Turtle
from turtle import Screen
# Create class Scoreboard that inherits from the class Turtle.
class Scoreboard(Turtle):

    # Initialize the class Scoreboard.
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 265)
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=("arial", 24, "normal"))
        self.hideturtle()

    # Create game_over method.
    def game_over(self):
        self.goto(0, 0)
        self.screen.clear()
        self.screen.bgcolor("Black")
        self.goto(0, 100)
        self.write(f"GAME OVER", align="center", font=("arial", 24, "normal"))
        self.goto(0, 0)
        self.write(f"Final Score: {self.score}", align="center", font=("arial", 24, "normal"))

    # Create increase_score method.
    def increase_score(self):
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("arial", 24, "normal"))