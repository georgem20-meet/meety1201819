from turtle import *
import random
import turtle

class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius=radius
		self.color(color)
		self.speed(speed)
ball = Ball(30, "Blue", 100)
ball2 = Ball(10, "Green", 100)
def check_collision(self, radius =, colour, speed):
	position1=ball.position
	position2=ball2.position

turtle.mainloop()