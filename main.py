# Import modules.
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Create screen and set dimensions.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

# Create snake, food, scoreboard objects.
snake = Snake()
food = Food()
score = Scoreboard()

# Bind arrow keys to movements.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        score.clear()
        snake.extend()
        score.increase_score()

    # Detect collision with walls.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
