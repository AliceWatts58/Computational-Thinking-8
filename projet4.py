import turtle 
t = turtle.Turtle()

import turtle 
t2 = turtle.Turtle()
#added more colors
t2.penup()
t2.goto(-350,200)
t2.color("yellow")
t2.pendown()
t2.speed(20)

t.goto(100,0)
t.color("white")
#background
turtle.Screen().bgcolor("crimson")

for i in range(4):
    t.forward(100)
    t.left(72)
t.left(-107)
t.forward(60)
t.setheading(72)
for i in range (4):
    t.left(72)
    t.forward(100)
t.forward(25)
#eyes of monster
t.left(-90)
t.forward(25)
t.left(90)
t.forward(40)
t.left(90)
t.forward(26)
# 2nd tooth
t.left(-90)
t.forward(35)
t.left(-90)
t.forward(25)
t.left(90)
t.forward(40)
t.left(90)
t.forward(27)
#rest of head and body
t.left(-90)
t.forward(83)
t.left(80)
t.forward(-120)
t.left(100)
t.forward(280)
t.left(90)
t.forward(200)
t.left(-90)
t.forward(70)
t.left(-90)
t.forward(150)
t.left(90)
t.forward(190)
t.left(90)
t.forward(-165)
t.left(90)
t.forward(565)


for i in range (670):
    t2.forward(200)
    t2.left(195)

turtle.exitonclick()