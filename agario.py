import turtle
import time
import random
from ball import Ball 
import math
import time

def game():
	turtle.tracer(0)
	turtle.hideturtle()
	RUNNING = True 
	STARTSLEEP = 0.0077
	SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
	SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

	matchy_ball = Ball(1, 1, 20, 20, 30, "blue")
	NUMBER_OF_BALLS = 5
	MINIMUM_BALL_RADIUS = 10
	MAXIMUM_BALL_RADIUS = 100
	MINIMUN_BALL_DX = -5
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
		d = ((ball_a,xcor()-ball_b.xcor())**2 + (ball_a.ycor()-ball_b.ycor()**2))**0.5
		if (d< ball_a.r + ball_b.r):
			return True
		else:
			return False
	def check_all_balls_collision():
		for ball_a in BALLS:
			for ball_b in BALLS:
				collide(ball_a, ball_b)

	if collide(ball_a,ball_b)== True:
		r1 = ball_a.r
		r2 = ballb.r

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
	points2 = turtle.Turtle()
	points.hideturtle()
	pints2.penup()

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
									
									points2.goto(0,300)
									score += 1
									points2.clear()
									points2.write(str("Your score is : " + str(score)), move = True, align = "center", font = ("Arial", 20, "normal"))







									return True
		def move_all_balls():
			for i in BALLS:
				i.move(SCREEN_WIDTH, SCREEN_HEIGHT)



	def movearound(event):
		player.goto(event.x - SCREEN_WIDTH, SCREEN_HEIGHT - event.y)

	turtle.getcanvas() .bind("<Motion>", movearound)


	while RUNNING:
		move_all_balls()
		myball_collision()
		check_all_balls()
		turtle.update()
		time.sleep(SLEEP)
		while points >= 0:
			timer.write(str("GAME STARTS IN : " + str(points) + " SECONDS"), move = True, align = "center", font = ("Arial", 20, "normal"))
		points -= 1
		time.sleep(1)
		timer.clear()
		timer.goto(0, 300)



		line = turtle.Turtle()
		left = turtle.Turtle()
		right = turtle.Turtle()
		left2 = turtle.Turtle()
		right2 = turtle.Turtle()
		left3 = turtle.Turtle()

		line.hideturtle()
		line.speed(0)
		line.penup()
		line.pensize(5)
		line.goto(0,-800)
		line.pendown()
		line.goto(0,800)
		


		left.hideturtle()
		left.speed(0)
		left.penup()
		left.goto(-300,0)
		left.write(str('Game Mode 1'), move = True, align = "center", font = ("Arial", 20, "normal"))

		left2.hideturtle()
		left2.speed(0)
		left2.penup()
		left2.goto(-300,-50)
		left2.write(str('Dodge the balls!'), move = True, align = "center", font = ("Arial", 20, "normal"))

		left3.hideturtle()
		left3.speed(0)
		left3.penup()
		left3.goto(-450,200)
		left3.write(str("""Choose the Game Mode you want by clicking 
	its side of the screen using the mouse!"""), move = True, align = "left", font = ("Arial", 15, "normal"))






		right.hideturtle()
		right.speed(0)
		right.penup()
		right.goto(300,0)
		right.write(str('Game Mode 2'), move = True, align = "center", font = ("Arial", 20, "normal"))

		right2.hideturtle()
		right2.speed(0)
		right2.penup()
		right2.goto(300,-50)
		right2.write(str('Agar.io!'), move = True, align = "center", font = ("Arial", 20, "normal"))
		


		
		def clicked(x,y):
			
			if x > 0:
				
				line.clear()
				left.clear()
				right.clear()
				left2.clear()
				right2.clear()
				left3.clear()

				
				line.hideturtle()
				left.hideturtle()
				right.hideturtle()
				left2.hideturtle()
				right2.hideturtle()
				left3.hideturtle()

				game_mode1()
			
			if x < 1:
			
				line.clear()
				left.clear()
				right.clear()
				left2.clear()
				right2.clear()
				left3.clear()

				line.hideturtle()
				left.hideturtle()
				right.hideturtle()
				left2.hideturtle()
				right2.hideturtle()
				left3.hideturtle()

				game_mode2()


		turtle.onscreenclick(clicked)


	turtle.mainloop()
game()



















			






