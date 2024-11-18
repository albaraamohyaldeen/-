from turtle import Turtle

class Writ(Turtle):
	def __init__(self ,position):
		super().__init__()
		self.color('white')
		self.penup()
		self.hideturtle()
		self.goto(position)
