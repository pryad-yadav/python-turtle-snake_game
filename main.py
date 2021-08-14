from snake import Snake
from food import Food
from scoreboard import Score
from turtle import Screen
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()

screen.onkey(key='Up',fun=snake.up)
screen.onkey(key='Down',fun=snake.down)
screen.onkey(key='Left',fun=snake.left)
screen.onkey(key='Right',fun=snake.right)


gameOn = True

while gameOn:
    screen.update()
    time.sleep(.1)
    snake.move()

    # detect collision with food
    if snake.segments[0].distance(food) <15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        gameOn = False
        score.gameOver()

    # detect tail collision
    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) <10:
            gameOn = False
            score.gameOver()

screen.exitonclick()