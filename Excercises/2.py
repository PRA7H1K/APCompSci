# import turtle module
import turtle as turtle

# create turtle object
painter = turtle.Turtle()

painter.pensize(3)

# then draw a circle
painter.fillcolor("turquoise")
painter.begin_fill()
painter.circle(90)
painter.end_fill()

# move the turtle to another part of the screen


# change both the pen and fill colors
# then draw a polygon of your choice


# create screen object and make it persist
wn = turtle.Screen()
wn.mainloop()