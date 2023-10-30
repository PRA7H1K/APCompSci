import turtle as trtl

painter = trtl.Turtle()
wn = trtl.Screen()

painter.speed('fastest')
painter.pencolor('white')
# wn.tracer(0)

# Desert
height = 200
for line in range(6):
    painter.fillcolor('#f2d2a9')
    alternate_color = line % 2
    if alternate_color < 1:
        painter.fillcolor('#dec099')
    painter.begin_fill()
    painter.penup()
    painter.goto(0, height)
    painter.pendown()
    painter.forward(250)
    painter.right(90)
    painter.forward(75)
    painter.right(90)
    painter.forward(500)
    painter.right(90)
    painter.forward(75)
    painter.right(90)
    painter.forward(250)
    painter.end_fill()
    height = height - 75
    painter.penup()
    painter.goto(0, 200)
    painter.pendown()

length = 250
space_from_top = 0
painter.pencolor('darkgrey')
for line in range(13):
    painter.fillcolor('#e6e6e6')
    alternate_color = line % 13
    if alternate_color == 11:
        painter.fillcolor('gold')
    if alternate_color == 12:
        painter.fillcolor('gold')
    painter.begin_fill()
    painter.penup()
    painter.goto(0, space_from_top + 100)
    painter.pendown()
    painter.forward(length / 2)
    painter.right(90)
    painter.forward(length)
    painter.right(90)
    painter.forward(length)
    painter.right(90)
    painter.forward(length)
    painter.right(90)
    painter.forward(length / 2)
    length = length - 20
    space_from_top = space_from_top - 2
    painter.end_fill()

# Lines
painter.penup()
painter.goto(-5, 66)
painter.pendown()
painter.right(119)
painter.forward(248)

painter.penup()
painter.goto(5, 66)
painter.pendown()
painter.left(58)
painter.forward(248)

painter.penup()
painter.goto(5, 76)
painter.pendown()
painter.left(72)
painter.forward(122)

painter.penup()
painter.goto(-5, 76)
painter.pendown()
painter.left(158)
painter.forward(122)

painter.hideturtle()

wn.mainloop()