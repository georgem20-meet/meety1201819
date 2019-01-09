import turtle
from turtle import *

class Ball(Turtle):
	def __init__(self, x, y, dx, dy, r, color):
		Turtle.__init__(self)
		self.x=x
		self.y=y
		self.color(color)
		self.dx=dx
		self.dy=dy
		self.r=r
		self.shape("circle")
		turtle.penup()
		self.r=r
		self.shapesize(r/10)
	def move (self, screen_width, screen_height):
		current_x = xcor()
		new_x = current_x + self.dx
		current_y = ycor()
		new_y = current_y + self.dy
		right_side_ball = new_x + self.r
		bottom_side_ball = new_y - self.r
		left_side_ball = new_x - self.r
		upper_side_ball = new_y + self.r
		self.goto(new_x, new_y)
		self.screen_width = screen_width
		if new_x >= screen_width or new_x <= screen_width:
			self.dx = -self.dx
		if new_y >= screen_height or new_y <= screen_height:
			self.dy = -self.dy
		








