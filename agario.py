import turtle
import time
import random
from ball import Ball 
import math
import time


turtle.tracer(0)
turtle.hideturtle()
RUNNING = True 
STARTSLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
match_ball = Ball(1, 1, 20, 20, 30, "blue")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []
for i in range (NUMBER_OF_BALLS):
	color1 = random.random()
	color2 = random.random()
	color3 = random.random()
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DX)
	r = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	while dx == 0:
		dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	while dy == 0:
		dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)

		BALLS.append(Ball(x, y, dx, dy, r,(color1, color2, color3)))

	def move_all_balls(balls):
		for ball in balls:
			ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)

	def collide(ball_a, ball_b):
		if ball_a == ball_b:
			return False
		current_x1 = ball_a.xcor()
		current_y1 = ball_a.ycor()

					
		current_x2 = ball_b.xcor()
		current_y2 = ball_b.ycor()


		d = ((ball_a,xcor()-ball_b.xcor())**2 + (ball_a.ycor()-ball_b.ycor()**2))**0.5
		if (d< ball_a.r + ball_b.r):
			return True
		else:
			return False
	def check_all_balls_collision():
		for ball_a in BALLS:
			for ball_b in BALLS:
				collide(ball_a, ball_b)

		if collide(ball_a, ball_b)== True:
			r1 = ball_a.r
			r2 = ball_b.r



		x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
		y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
		dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
		dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
		r = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
		while dx == 0:
			dx = random.randit(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
		while dy == 0:
			dy = random.randit(MINIMUM_BALL_DY, MINIMUM_BALL_DY)
		if r1 > r2:
			if r1 < 250:
				ball_a.r = ball_a.r + 4

				ball_b.goto(x,y)
				ball_b.color(color)
				ball_b.r = r

				ball_a.shapesize(ball_a.r/10)
				ball_b.shapesize(ball_b.r/10)
	

	def check_myball_collision():
		global score
		for ball_a in BALLS:
			if collide(ball_a, player) == True:
				if ball_a.r > player.r:
					quit()
					if ball_a.r<player.r:
						if player.r < 250:
									x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
									y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
									dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
									dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
									r  = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
									color = (random.random(),random.random(),random.random())
									while dx == 0:
										dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
									while dy == 0:
										dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
									ball_a.goto(x,y)
									player.r = player.r + 2
								
									ball_a.color(color)
									ball_a.r = r
									player.shapesize(player.r/10)
									ball_a.shapesize(ball_a.r/10)
									
								







									return True
		def move_all_balls():
			for i in BALLS:
				i.move(SCREEN_WIDTH, SCREEN_HEIGHT)



	def movearound(event):
		player.goto(event.x - SCREEN_WIDTH, SCREEN_HEIGHT - event.y)

	turtle.getcanvas() .bind("<Motion>", movearound)


	while RUNNING:
					move_all_balls(BALLS)
					check_myball_collision()
					check_all_balls_collision()
					turtle.update()
					time.sleep(SLEEP)
turtle.onescreenclick(clicked)

turtle.mainloop()



















			






