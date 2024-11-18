from turtle import Turtle

class Range(Turtle):
	def __init__(self , position):
		super().__init__()
		self.color('dark blue')
		self.shape('square')
		self.penup()
		self.goto(position)
