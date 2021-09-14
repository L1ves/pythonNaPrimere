import turtle
import random

#colour = random.choice(["red", "blue", "green", "white", "pink"])
turtle.begin_fill()
for i in range(0,8):
	colour = random.choice(["red", "blue", "green", "white", "pink"])
	turtle.color(colour, colour)
	turtle.forward(100)
	turtle.right(45)
turtle.end_fill()
turtle.exitonclick()
	#turtle.left()