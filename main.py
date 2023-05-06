from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(screen.bye, "Escape")

alive = True


while alive:
	screen.update()
	time.sleep(0.07)
	snake.move()
	if snake.head.distance(food) < 17:
		food.set_random_location()
		snake.extend()
		score.increase()

	if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
		score.reset()
		snake.reset()
	for part in snake.body_parts[1:]:
		if snake.head.distance(part) < 10:
			score.reset()
			snake.reset()

screen.exitonclick()
