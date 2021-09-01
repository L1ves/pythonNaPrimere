import turtle


#1)рисуем 3 квадрата 2) и делаем невидимый отступ между ними
turtle.right(90)
turtle.color("black", "white")
turtle.begin_fill()
for i in range(0,4):
	turtle.forward(70)
	turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("black", "blue")
turtle.begin_fill()
for i in range(0,4):
	turtle.forward(70)
	turtle.right(90)
turtle.penup()
turtle.forward(100)
turtle.end_fill()

turtle.pendown()
turtle.color("black", "red")
turtle.begin_fill()
for i in range(0,4):
	turtle.forward(70)
	turtle.right(90)
turtle.end_fill()
turtle.exitonclick()
