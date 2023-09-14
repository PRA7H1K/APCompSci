import turtle as trtl

painter = trtl.Turtle()

painter.turtlesize(1.5)
painter.pensize(3)
painter.pencolor("grey")

painter.penup()
painter.goto(-100, 100)
painter.pendown()

# Large Square
painter.forward(100)
painter.right(90)
painter.forward(100)
painter.right(90)
painter.forward(100)
painter.right(90)
painter.forward(100)
painter.right(90)

# Preparing for Line to Small Square
painter.penup()
painter.home()
painter.backward(50)
painter.pendown()

painter.right(90)

# Line Connecting Big Square to Small Square
painter.forward(100)

# Small Square
painter.left(90)
painter.forward(25)
painter.right(90)
painter.forward(50)
painter.right(90)
painter.forward(50)
painter.right(90)
painter.forward(50)
painter.right(90)
painter.forward(25)

# Preparing for Line to Circle
painter.penup()
painter.forward(25)
painter.right(90)
painter.forward(25)
painter.pendown()

# Line Connecting Small Square to Circle
painter.left(90)
painter.forward(100)

# Circle
painter.penup()
painter.forward(1)
painter.right(90)
painter.forward(1)
painter.pendown()
painter.circle(25)

# Preparing for Line to Triangle
painter.penup()
painter.left(90)
painter.forward(25)
painter.left(90)
painter.forward(25)
painter.pendown()

# Line Connecting Circle to Triangle
painter.forward(100)

# Triangle
painter.right(90)
painter.forward(50)
painter.left(120)
painter.forward(100)
painter.left(120)
painter.forward(100)
painter.left(120)
painter.forward(50)

# Preparing for Line to Big Square
painter.penup()
painter.left(90)
painter.forward(50)
painter.left(90)
painter.forward(24)
painter.pendown()
painter.forward(75)

painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()