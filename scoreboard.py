from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Copperplate", 17, "normal")

class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.penup()
		self.goto(0, 275)
		self.pencolor("white")
		self.score = 0
		with open("data.txt") as high:
			self.high_score = int(high.read())
		self.post()

	def post(self):
		self.clear()
		self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

	def increase(self):
		self.score += 1
		self.post()

	def reset(self):
		if self.score > self.high_score:
			with open("data.txt", "w") as high:
				high.write(f"{self.score}")
			with open("data.txt") as high:
				self.high_score = int(high.read())
		self.score = 0
		self.post()

	# def game_over(self):
	# 	self.home()
	# 	self.write("Game Over.", align=ALIGNMENT, font=FONT)

