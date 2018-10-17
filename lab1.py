name = "George"
print (name*5)
print ("George"*100)
number1 = 1
print (number1)
number2 = .5
print (number2)
ls = [1,2,3]
for i in ls:
	print i	
	print i*2
b = sum(ls)	
print (b)

import turtle
turtle.begin_fill()
turtle.fillcolor ("blue")
turtle.goto(0,100)
turtle.goto(100,100)
turtle.goto(100,0)
turtle.goto(0,0)

turtle.end_fill()
turtle.mainloop()
