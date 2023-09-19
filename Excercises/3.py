# import turtle module
import turtle as turtle

# create turtle object
painter = turtle.Turtle()

radius = int(input("What radius would you like me to use? "))

painter.pensize(3)

painter.pencolor("blue")

# square
painter.fillcolor("blue")
painter.begin_fill()
painter.circle(radius, 360, 4)
painter.end_fill()

painter.right(180)

# semi circle
painter.pencolor("green")
painter.fillcolor("green")
painter.begin_fill()
painter.circle(radius, 180)
painter.end_fill()

painter.penup()
painter.home()
painter.pendown()

painter.pencolor("red")

painter.fillcolor("red")

# triangle
painter.begin_fill()
painter.forward(2 * radius)
painter.right(90)
painter.forward(radius)
painter.home()
painter.end_fill()

painter.hideturtle()


# create screen object and make it persist
wn = turtle.Screen()
wn.mainloop()