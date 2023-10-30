# import turtle module
import turtle as turtle

# create turtle object
painter = turtle.Turtle()

painter.pensize(3)

painter.pencolor("blue")

segment = 50
angle = 50
while segment == 50:
    painter.forward(50)
    painter.right(angle)
    angle = angle + 10

while segment == 51:
    painter.forward(60)

# create screen object and make it persist
wn = turtle.Screen()
wn.mainloop()