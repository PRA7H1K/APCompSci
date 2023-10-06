import turtle as trtl

painter = trtl.Turtle()
painter.speed('normal')

# Stem
painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)

#  leaf
painter.setheading(270)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)

#  leaf
painter.setheading(270)
painter.right(180)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)

# Stem Continued
painter.forward(60)
painter.setheading(0)


painter.penup()
painter.shape("circle")
painter.turtlesize(2)

# Outer Ring of Petals
painter.color("yellow")
painter.goto(20,190)

for petal in range(18):
  painter.right(20)
  painter.forward(30)
  painter.stamp()

# Middle Ring of Petals
painter.goto(20,160)
painter.color("orange")

for petal in range(12):
  painter.right(30)
  painter.forward(30)
  painter.stamp()

# Inner Ring of Petals
painter.goto(20,130)
painter.color("brown")

for petal in range(6):
  painter.right(60)
  painter.forward(30)
  painter.stamp()
  
wn = trtl.Screen()
wn.mainloop()