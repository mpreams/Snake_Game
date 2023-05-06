from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 14
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

	def __init__(self):
		self.body_parts = []
		self.create_snake()

	def create_snake(self):
		for position in STARTING_POSITIONS:
			self.add_part(position)
		self.head = self.body_parts[0]

	def add_part(self, position):
		part = Turtle(shape="square")
		part.penup()
		part.color("white")
		part.goto(position)
		self.body_parts.append(part)

	def reset(self):
		for part in self.body_parts:
			part.hideturtle()
		self.body_parts.clear()
		self.create_snake()

	def extend(self):
		self.add_part(self.body_parts[-1].position())

	def move(self):
		for part in range(len(self.body_parts) - 1, 0, -1):
			next_x = self.body_parts[part - 1].xcor()
			next_y = self.body_parts[part - 1].ycor()
			self.body_parts[part].goto(next_x, next_y)
		self.head.forward(MOVE_DISTANCE)

	def up(self):
		if self.head.heading() != DOWN:
			self.head.setheading(90)

	def down(self):
		if self.head.heading() != UP:
			self.head.setheading(270)

	def left(self):
		if self.head.heading() != RIGHT:
			self.head.setheading(180)

	def right(self):
		if self.head.heading() != LEFT:
			self.head.setheading(0)