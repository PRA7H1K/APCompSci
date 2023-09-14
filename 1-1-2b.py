# import turtle module
import turtle as turtle

# create turtle object
painter = turtle.Turtle()

# add code here for a circle
painter.circle(20)

# move the turtle to another part of the screen
painter.penup()
painter.forward(100)

# add code here for an arc
painter.pendown()
painter.circle(100, 180)

# move the turtle to another part of the screen
painter.penup()
painter.home()
painter.right(180)
painter.forward(200)

# add code here for an arc that is greater than 90 degrees and has 5 steps
painter.pendown()
painter.circle(100, 90, 5)

# move the turtle to another part of the screen
painter.penup()
painter.left(90)
painter.forward(200)
painter.right(90)
painter.forward(50)

# add code here to create a polygon of your choice using the circle method
painter.pendown()
painter.circle(100, 360, 6)

painter.hideturtle()

# create screen object and make it persist
wn = turtle.Screen()
wn.mainloop()