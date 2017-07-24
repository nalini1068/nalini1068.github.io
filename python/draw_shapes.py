from turtle import *
import math

# Name your Turtle.
shelly = Turtle()

# Set Up your screen and starting position.
setup(500,500)
x_pos = 0
y_pos = 0
shelly.setposition(x_pos, y_pos)
shelly.setposition(0,0)
### Write your code below:
pendown ()
for x in range(0,4):
	print ("I did it %d" % (x,))
	shelly.right(45)
	shelly.forward(100)

'''
forward(100)
right(90)
forward(100)
right(90)
forward(100)
goto(0,10)
right(90)
penup()
x_pos = 50
y_pos = 50
pendown()
right(45)
forward(100)
right(45)
forward(100)
left(45)
forward(-100)
right(45)
forward(-100)
left(45)
forward(-100)
left(45)
forward(100)
right(-45)
goto(0,10)

'''
# Close window on click.
exitonclick()
