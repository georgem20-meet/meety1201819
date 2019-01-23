import turtle
import time
import random
from ball import Ball 

turtle.tracer(0)
turtle.hideturtle()
RUNNING = True 
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = TURTLE.GETCANVAS().WONFO_HEIGHT()/2

my_ball = Ball(1, 1, 20, 20, 30, "blue")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MAXIMUN_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []
for i in range (NUMBER_OF_BALLS):
	color1 = random.random()
	color2 = random.random()
	color3 = random.random()
	x = random.randit(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randit(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy = random.randit(MINIMUM_BALL_DY, MAXIMUM_BALL_DX)
	r = random.randit(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	while dx == 0:
		dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	while dy == 0:
		dy = random.randit(MINIMUM_BALL_DY, MAXIMUM_BALL_DX)

	BALLS.append(Ball(x, y, dx, dy, r,(color1, color2, color3)))

def move_all_balls(balls):
	for ball in balls:
		ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def collide(ball_a, ball_b):
	if ball_a == ball_b:
		return False
	d = ((ball_a,xcor()-ball_b.xcor())**2 + (ball_a.ycor()-ball_b.ycor()**2))**0.5
	if (d< ball_a.r + ball_b.r):
		return True
	else:
		return False
def check_all_balls_collision():
	for a in BALLS:
		for b in BALLS:
			if a != b:
				d = ((a.xcor()-b.xcor())**2 + (a.ycor()-b.ycor()**2))**0.5






