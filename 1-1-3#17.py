import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

# Stem
painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)

# Leaf
painter.setheading(270)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)

# Stem Continued
painter.forward(60)
painter.setheading(0)

# Change Pen
painter.penup()
painter.shape("circle")
painter.turtlesize(2)

# Flower
painter.goto(20,180)

for petal in range(18):
    painter.right(20)
    painter.forward(30)
    painter.color("lightblue")
    remainder_teal = petal % 2
    remainder_purple = petal % 4
    if remainder_teal == 0:
        painter.color("teal")
    if remainder_purple == 0:
        painter.color("purple")
    painter.stamp()
  
wn = trtl.Screen()
wn.mainloop()