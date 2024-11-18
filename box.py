from turtle import Turtle

class Box(Turtle):
	def __init__(self,position):
		super().__init__()
		self.color('dark gray')
		self.shape('square')
		self.shapesize(1.4,21.1)
		self.penup()
		self.goto(position)
