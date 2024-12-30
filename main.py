from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
# snake = Turtle()
screen = Screen()
screen.title("SNAKE GAME")
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
game_is_on = True
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.move_forward,"Up")
screen.onkeypress(snake.move_backward,"Down")
screen.onkeypress(snake.turn_right,"Right")
screen.onkeypress(snake.turn_left,"Left")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.updated_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on= False
        scoreboard.game_end()

    #detect collision with tail
    for segments in snake.segments:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            game_is_on = False
            scoreboard.game_end()

screen.exitonclick()