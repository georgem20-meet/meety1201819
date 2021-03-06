from turtle import *
import turtle
import time
import random
from ball import Ball
import math
import time


def game():
	screen = turtle.Screen()
	screen.title("George's benevolent game")
	
	def game_mode1():
		#variables
		turtle.tracer(0,0)
		turtle.hideturtle()
		
		RUNNING = True
		SLEEP = 0.0077  
		SCREEN_WIDTH = turtle.getcanvas() . winfo_width()/2
		SCREEN_HEIGHT = turtle.getcanvas() . winfo_height()/2
		player = Ball(0, 0, 25, 25, 15, "blue")
		NUMBER_OF_BALLS = 25
		MINIMUM_BALL_RADIUS = 5
		MAXIMUM_BALL_RADIUS = 25
		MINIMUM_BALL_DX = -3
		MAXIMUM_BALL_DX = 3
		MINIMUM_BALL_DY = -3
		MAXIMUM_BALL_DY = 3
		BALLS = []
		points = 3
		timer = turtle.Turtle()
		timer.hideturtle()
		timer.penup()
		timer.goto(0,300)
		global score
		score = 0
		
		#creating the circles
		for i in range(NUMBER_OF_BALLS):
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
			new_ball = Ball(x,y,dx,dy,r,color)
			BALLS.append(new_ball)








		#checking collisions between 2 balls
		def collide(ball_a, ball_b):
			if ball_a == ball_b:
				return False
			current_x1 = ball_a.xcor()
			current_y1 = ball_a.ycor()

					
			current_x2 = ball_b.xcor()
			current_y2 = ball_b.ycor()

			D = math.sqrt(math.pow((current_x2-current_x1),2) + math.pow((current_y2 - current_y1),2))	
			if D >= ball_a.r + ball_b.r:
				return False
			if D < ball_a.r + ball_b.r:
				return True 

			
		def check_all_balls():
				for ball_a in BALLS:			
					for ball_b in BALLS:
						collide(ball_a, ball_b)
						
						if collide(ball_a,ball_b) == True:
							r1 = ball_a.r
							r2 = ball_b.r

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
							if r1 > r2:
								if r1 < 250:
									ball_a.r = ball_a.r + 4
									
								
									ball_b.goto(x,y)
									ball_b.color(color)
									ball_b.r = r

									ball_a.shapesize(ball_a.r/10)
									ball_b.shapesize(ball_b.r/10)
									
									


							

		points2 = turtle.Turtle()
		points2.hideturtle()
		points2.penup()
		def myball_collision():
				global score
				for ball_a in BALLS:
					collide(ball_a, player)
					if collide(ball_a, player) == True:
						if ball_a.r > player.r:
							quit()
						
						if ball_a.r < player.r:
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


		#making the game move 
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
			



	


		#creating the circles
		for i in range(NUMBER_OF_BALLS):
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
			new_ball = Ball(x,y,dx,dy,r,color)
			BALLS.append(new_ball)








	
		def collide(ball_a, ball_b):
			if ball_a == ball_b:
				return False
			current_x1 = ball_a.xcor()
			current_y1 = ball_a.ycor()

					
			current_x2 = ball_b.xcor()
			current_y2 = ball_b.ycor()

			D = math.sqrt(math.pow((current_x2-current_x1),2) + math.pow((current_y2 - current_y1),2))	
			if D >= ball_a.r + ball_b.r:
				return False
			if D < ball_a.r + ball_b.r:
				return True 

		

							


		def myball_collision():
				for ball_a in BALLS:
					collide(ball_a, player)
					if collide(ball_a, player) == True:
						if ball_a.r > player.r or  ball_a.r < player.r:
							quit()

						
						


		#making the game move 
		def move_all_balls():
			for i in BALLS:
				i.move(SCREEN_WIDTH, SCREEN_HEIGHT)
					
		def movearound(event):
			player.goto(event.x - SCREEN_WIDTH, SCREEN_HEIGHT - event.y)

		turtle.getcanvas() .bind("<Motion>", movearound)

		
		while RUNNING:
			move_all_balls()
			myball_collision()

			turtle.update()
			time.sleep(SLEEP)
			
			while points >= 0:
				timer.write(str("GAME STARTS IN : " + str(points) + " SECONDS"), move = True, align = "center", font = ("Arial", 20, "normal"))
				points -= 1
				time.sleep(1)
				timer.clear()
				timer.goto(0, 300)



	


	
	def clicked(x,y):
		
		if x > 0:
			
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