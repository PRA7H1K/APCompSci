import turtle as trtl

painter = trtl.Turtle()
painter.speed('fastest')

painter.penup()
painter.goto(0, 200)
painter.pendown()

# Draw Circle
painter.forward(200)
painter.right(90)
painter.forward(400)
painter.right(90)
painter.forward(400)
painter.right(90)
painter.forward(400)
painter.right(90)
painter.forward(200)

# Go to first row of seats
painter.penup()
painter.goto(175, 175)
painter.pendown()

# Draw first row of seats
for line in range(35):
    painter.fillcolor('blue')
    alternate = line % 6
    if (alternate < 3):
        painter.fillcolor("red")
    painter.begin_fill()
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(180)

    painter.end_fill()

    painter.penup()

    painter.forward(10)
    painter.left(90)
    painter.pendown()

# Go to second row of seats
painter.penup()
painter.goto(150, 150)
painter.pendown()

# Draw second row of seats
for line in range(30):
    painter.fillcolor('blue')
    alternate = line % 6
    if (alternate < 3):
        painter.fillcolor("red")
    painter.begin_fill()
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(180)

    painter.end_fill()

    painter.penup()

    painter.forward(10)
    painter.left(90)
    painter.pendown()

# Go to third row of seats
painter.penup()
painter.goto(125, 125)
painter.pendown()

# Draw third row of seats
for line in range(25):
    painter.fillcolor('blue')
    alternate = line % 6
    if (alternate < 3):
        painter.fillcolor("red")
    painter.begin_fill()
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(180)

    painter.end_fill()

    painter.penup()

    painter.forward(10)
    painter.left(90)
    painter.pendown()

# Go to third row of seats
painter.penup()
painter.goto(100, 100)
painter.pendown()

# Draw third row of seats
for line in range(20):
    painter.fillcolor('blue')
    alternate = line % 6
    if (alternate < 3):
        painter.fillcolor("red")
    painter.begin_fill()
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(180)

    painter.end_fill()

    painter.penup()

    painter.forward(10)
    painter.left(90)
    painter.pendown()
    




# Go to first row of seats
painter.penup()
painter.goto(-175, 175)
painter.pendown()

# Draw first row of seats
for line in range(35):
    painter.fillcolor('blue')
    alternate = line % 6
    if (alternate < 3):
        painter.fillcolor("red")
    painter.begin_fill()
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(180)

    painter.end_fill()

    painter.penup()

    painter.forward(10)
    painter.left(90)
    painter.pendown()

# Go to second row of seats
painter.penup()
painter.goto(-150, 150)
painter.pendown()

# Draw second row of seats
for line in range(30):
    painter.fillcolor('blue')
    alternate = line % 6
    if (alternate < 3):
        painter.fillcolor("red")
    painter.begin_fill()
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(180)

    painter.end_fill()

    painter.penup()

    painter.forward(10)
    painter.left(90)
    painter.pendown()

# Go to third row of seats
painter.penup()
painter.goto(-125, 125)
painter.pendown()

# Draw third row of seats
for line in range(25):
    painter.fillcolor('blue')
    alternate = line % 6
    if (alternate < 3):
        painter.fillcolor("red")
    painter.begin_fill()
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(180)

    painter.end_fill()

    painter.penup()

    painter.forward(10)
    painter.left(90)
    painter.pendown()

# Go to third row of seats
painter.penup()
painter.goto(-100, 100)
painter.pendown()

# Draw third row of seats
for line in range(20):
    painter.fillcolor('blue')
    alternate = line % 6
    if (alternate < 3):
        painter.fillcolor("red")
    painter.begin_fill()
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(90)
    painter.forward(10)
    painter.right(180)

    painter.end_fill()

    painter.penup()

    painter.forward(10)
    painter.left(90)
    painter.pendown()


# Draw court
painter.penup()
painter.goto(-75, 100)
painter.pendown()
painter.forward(155)
painter.right(90)
painter.forward(200)
painter.right(90)
painter.forward(155)
painter.right(90)
painter.forward(200)


wn = trtl.Screen()
wn.mainloop()